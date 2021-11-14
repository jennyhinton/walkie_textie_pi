import spidev
import RPi.GPIO as GPIO
import time

#figure out why/where spidev changes list to 0s

class Screen:
    def __init__(self):
        
        GPIO.setwarnings(False)
        self.spi0 = spidev.SpiDev()
        self.spi0.open(0,0)                #spi bus 0 with chip select 0
        self.spi0.max_speed_hz = 31200000  #speeds up to 33 MHz. This is 31.2MHz
        GPIO.setmode(GPIO.BOARD) #Use pin numbers to identify gpio
        self.CD = 10
        self.RST = 33 
        GPIO.setup(self.CD,GPIO.OUT)   #set pin 3 (GPIO 2) as output for CD pin
        GPIO.setup(self.RST,GPIO.OUT)   #reset pin

        #Screen commands as uint16        
        display_start_line = int("40", 16)    #start line at 0
        set_SEG_bottom = int("A1", 16)        #bottom (normal) view
        set_direction_normal = int("C0", 16)  #com0-com63
        disable_all_pixels = int("A4",16)
        enable_all_pixels = int("A5",16)
        disable_inverse_display = int("A6",16)
        set_bias = int("A2",16)                 # bias 1/9 (duty 1/65)
        set_power_control = int("2F",16)        #set power control, booster, regulator and follower on
        set_contrast1 = int("27", 16)
        set_contrast2 = int("81", 16)
        set_contrast3 = int("10", 16)
        set_temp_comp_curve1 = int("FA", 16)     #set to -0.11 %/C
        set_temp_comp_curve2 = int("90", 16)
        enable_display = int("AF", 16)
        disable_display = int("AE", 16)
        
        
        self.startup_commands = [
            display_start_line,
            set_SEG_bottom,
            set_direction_normal,
            
            disable_all_pixels,
            disable_inverse_display,
            
            set_bias,
            set_power_control,
            set_contrast1,
            set_contrast2,
            set_contrast3,
            
            set_temp_comp_curve1,
            set_temp_comp_curve2,
            
            enable_display
        ]
        self.sleep_commands = [
            disable_display,
            enable_all_pixels
        ]
        self.wakeup_commands = [
            disable_all_pixels,
            enable_display
        ]

        #power on, set reset low and wait a sec then set reset high and wait 5 sec
        GPIO.output(self.RST, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.RST, GPIO.HIGH)
        time.sleep(5)
        
        #issue commands and wait a second
        GPIO.output(self.CD, GPIO.LOW)    #set CD pin low for command mode
        self.spi0.xfer3(self.startup_commands) #send initialization commands
        GPIO.output(self.CD, GPIO.HIGH)   #set CD pin high for data mode
        
        
    def sleep_mode(self):
        GPIO.output(self.CD, GPIO.LOW)
        self.spi0.xfer3(self.sleep_commands) 
        GPIO.output(self.CD, GPIO.HIGH)
    
    def wake_up(self):
        GPIO.output(self.CD, GPIO.LOW)
        self.spi0.xfer3(self.wakeup_commands) 
        GPIO.output(self.CD, GPIO.HIGH)

    def turn_off(self):
        raw_input("Hit enter to turn off screen")
        GPIO.output(self.RST, GPIO.LOW)
        time.sleep(1)
        print "unplug now"
        GPIO.cleanup()
        
    def letters(self):
        page1 = int("B0",16)
        page2 = int("B1",16)
        page3 = int("B2",16)
        page4 = int("B3",16)
        page5 = int("B4",16)
        page6 = int("B5",16)
        page7 = int("B6",16)
        page8 = int("B7",16)
            
        all_pages = [
            page1,
            page2,
            page3,
            page4,
            page5,
            page6,
            page7,
            page8
        ]
        
        collsb = [0]*132
        colmsb = [0]*132
        for x in range(132):
            index = x
            if x in range(16):
                x = hex(x)
                collsb[index] = x[-1]
                colmsb[index] = '0'
            else:
                x = hex(x)
                collsb[index] = x[-1]
                colmsb[index] = x[-2]
        
        pixeloff_commands = [
            int("00",16)
        ]
        pixelon_commands = [
            11100000
        ]
        
        for y in range(8):
            for x in range(132):
                temp1 = collsb[x]
                var1 = '0' + temp1
                temp = colmsb[x]
                var = '1' + temp
                location_commands = [
                    int(var1,16),  #set LSB col address
                    int(var,16),  #set MSB col address
                    all_pages[y]  #set page address
                ]
                GPIO.output(self.CD, GPIO.LOW)
                self.spi0.xfer3(location_commands)
                GPIO.output(self.CD, GPIO.HIGH)
                self.spi0.xfer3(pixelon_commands)
        
    
    

                