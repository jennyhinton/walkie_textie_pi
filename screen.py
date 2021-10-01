import spidev
import RPi.GPIO as GPIO
import time

#figure out why/where spidev changes list to 0s

class Screen:
    def __init__(self):
        spi0 = spidev.SpiDev()
        spi0.open(0,0)                #spi bus 0 with chip select 0
        spi0.max_speed_hz = 31200000  #speeds up to 33 MHz. This is 31.2MHz
        #spi0.mode = 0                #not sure what the modes are. Some examples have this, some dont
        GPIO.setmode(GPIO.BOARD) #Use pin numbers to identify gpio
        GPIO.setup(21,GPIO.OUT)   #set pin 3 (GPIO 2) as output for CD pin
        GPIO.setup(33,GPIO.OUT)   #reset pin
        
        #send commands
        
        display_start_line = int("40", 16)    #start line at 0
        set_SEG_bottom = int("A1", 16)        #bottom (normal) view
        set_direction_normal = int("C0", 16)  #com0-com63
        disable_all_pixels = int("A4",16)       
        disable_inverse_display = int("A6",16)
        set_bias = int("A2",16)                 # bias 1/9 (duty 1/65)
        set_power_control = int("2F",16)        #set power control, booster, regulator and follower on
        set_contrast1 = int("27", 16)
        set_contrast2 = int("81", 16)
        set_contrast3 = int("10", 16)
        set_temp_comp_curve1 = int("FA", 16)     #set to -0.11 %/C
        set_temp_comp_curve2 = int("90", 16)
        enable_display = int("AF", 16)
        
        #
        
        
        startup_commands = [
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

        GPIO.output(33, GPIO.LOW)
        time.sleep(1)
        GPIO.output(33, GPIO.HIGH)
        time.sleep(5)
        
        
        
        GPIO.output(21, GPIO.LOW)    #set CD pin low for command mode
        print(startup_commands)
        spi0.xfer3(startup_commands) #send initialization commands
        print(startup_commands)
        GPIO.output(21, GPIO.HIGH)   #set CD pin high for data mode
        
        GPIO.cleanup()