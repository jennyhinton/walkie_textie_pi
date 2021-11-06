import spidev
import RPi.GPIO as GPIO
import time

#figure out why/where spidev changes list to 0s

class Screen:
    def __init__(self):
        
        GPIO.setwarnings(False)

        spi0 = spidev.SpiDev()
        spi0.open(0,0)                #spi bus 0 with chip select 0
        spi0.max_speed_hz = 31200000  #speeds up to 33 MHz. This is 31.2MHz
        #spi0.mode = 0                #not sure what the modes are. Some examples have this, some dont
        GPIO.setmode(GPIO.BOARD) #Use pin numbers to identify gpio
        CD = 10
        RST = 33 
        GPIO.setup(CD,GPIO.OUT)   #set pin 3 (GPIO 2) as output for CD pin
        GPIO.setup(RST,GPIO.OUT)   #reset pin

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
        
        startup_commands = [
            display_start_line,
            set_SEG_bottom,
            set_direction_normal,
            
            enable_all_pixels,
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

        #power on, set reset low and wait a sec then set reset high and wait 5 sec
        GPIO.output(RST, GPIO.LOW)
        time.sleep(1)
        GPIO.output(RST, GPIO.HIGH)
        time.sleep(5)
        
        #issue commands and wait a second
        GPIO.output(CD, GPIO.LOW)    #set CD pin low for command mode
        spi0.xfer3(startup_commands) #send initialization commands
        GPIO.output(CD, GPIO.HIGH)   #set CD pin high for data mode
        
        time.sleep(5)
        print ("started")
        
        sleep_commands = [
            disable_display,
            enable_all_pixels
        ]
        wakeup_commands = [
            disable_all_pixels,
            enable_display
        ]
        
        #try sleep mode
        GPIO.output(CD, GPIO.LOW)
        spi0.xfer3(sleep_commands) 
        GPIO.output(CD, GPIO.HIGH)
        print("sleeping 5 secs")
        time.sleep(5)
        print ("wake up")
        GPIO.output(CD, GPIO.LOW)
        spi0.xfer3(wakeup_commands) 
        GPIO.output(CD, GPIO.HIGH)
        
        time.sleep(5)

        #trying rectangle thing
        GPIO.output(CD, GPIO.LOW)    #set CD pin low for command mode
        startcol = 0
        startpg = 1
        endcol = 50
        endpg = 7
        pattern = int("55", 16)
        pattern_commands = [
            pattern
        ]
        
        for y in range(startpg, endpg+1):
            for x in range(startcol, endcol+1):
                #spi0.xfer3(pattern_commands)
                pass
                
        GPIO.output(CD, GPIO.HIGH)   #set CD pin high for data mode
        
        print("anything?")
        
        time.sleep(5)
        
        raw_input("Hit enter to end")
        
        GPIO.output(RST, GPIO.LOW)
        time.sleep(1)
        print "unplug now"
                