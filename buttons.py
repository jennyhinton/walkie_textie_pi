import RPi.GPIO as GPIO

#need to define GPIOs
#need to define button actions
#need to check on extra inputs

class buttons:
    def power_callback(channel):
        pass #button actions  
    def ptt_callback(channel):
        pass #button actions 
    def up_callback(channel):
        pass #button actions 
    def down_callback(channel):
        pass #button actions
    def left_callback(channel):
        pass #button actions
    def right_callback(channel):
        pass #button actions
    def center_callback(channel):
        pass #button actions
    def vol_up_callback(channel):
        pass #button actions
    def vol_down_callback(channel):
        pass #button actions
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        power = #GPIO = power button
        PTT = #GPIO = PTT button
        up = #GPIO = up button
        down = #GPIO = down button
        left = #GPIO = left button
        right = #GPIO = right button
        center = #GPIO = center button
        vol_up = #GPIO = volume up button
        vol_down = #GPIO = volume down button
        
        #set each button pin as input pulled low
        GPIO.setup(power, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #check for rising edge trigger and perform event
        GPIO.add_event_detect(power,GPIO.RISING,callback=power_callback)
        
        GPIO.setup(ptt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=ptt_callback)

        GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=up_callback)
        
        GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=down_callback)

        GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=left_callback)

        GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=right_callback)

        GPIO.setup(center, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=center_callback)

        GPIO.setup(vol_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=vol_up_callback)

        GPIO.setup(vol_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(power,GPIO.RISING,callback=vol_down_callback)

        
        #speaker?
        #microphone?
        #rumbler?
        #mode switch?
        
        GPIO.cleanup()