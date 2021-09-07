import RPi.GPIO as GPIO

#need to define GPIOs
#need to define button actions
#need to check on extra inputs

class Buttons:
    def power_callback(self, channel):
        print ("power ")  #button actions  
    def ptt_callback(self, channel):
        print ("ptt ")  #button actions  
    def up_callback(self, channel):
        print ("up ")  #button actions  
    def down_callback(self, channel):
        print ("down ")  #button actions  
    def left_callback(self, channel):
        print ("left ")  #button actions  
    def right_callback(self, channel):
        print ("right ")  #button actions  
    def center_callback(self, channel):
        print ("center ")  #button actions  
    def vol_up_callback(self, channel):
        print ("volume up ")  #button actions  
    def vol_down_callback(self, channel):
        print ("volume down ")  #button actions  
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.power = 5#GPIO = power button
        self.ptt = 3#GPIO = PTT button
        self.up = 7#GPIO = up button
        self.down = 15#GPIO = down button
        self.left = 11#GPIO = left button
        self.right = 19#GPIO = right button
        self.center = 13#GPIO = center button
        #vol_up = #GPIO = volume up button
        #vol_down = #GPIO = volume down button
        
        #set each button pin as input pulled low
        GPIO.setup(self.power, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        #check for rising edge trigger and perform event
        GPIO.add_event_detect(self.power, GPIO.RISING, callback=self.power_callback)
        
        GPIO.setup(self.ptt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.ptt, GPIO.RISING, callback=self.ptt_callback)

        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.up, GPIO.RISING, callback=self.up_callback)
        
        GPIO.setup(self.down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.down, GPIO.RISING, callback=self.down_callback)

        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.left, GPIO.RISING, callback=self.left_callback)

        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.right, GPIO.RISING, callback=self.right_callback)

        GPIO.setup(self.center, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.center, GPIO.RISING, callback=self.center_callback)

        #GPIO.setup(self.vol_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(self.vol_up, GPIO.RISING, callback=self.vol_up_callback)

        #GPIO.setup(self.vol_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(self.vol_down, GPIO.RISING, callback=self.vol_down_callback)

        
        #speaker?
        #microphone?
        #rumbler?
        #mode switch?
        message = input ("Press enter to quit")
        GPIO.cleanup()