import RPi.GPIO as GPIO
from screen import Screen

HOME_inactive = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
HOME_active = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
MESSAGE_inactive = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
MESSAGE_active = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

VOLUME_HIGH = [
    ]

VOLUME_MED = [
    ]

VOLUME_LOW = [
    ]

SILENT = [
    ]
BUTTON_ICONS = {
        'home_active': HOME_active,
        'home_inactive': HOME_inactive,
        'message_active': MESSAGE_active,
        'message_inactive': MESSAGE_inactive
}

class Buttons:
    GPIO.setwarnings(False)

    def power_callback(self, channel):
        #shut down screen
        print ("power ")  #button actions  
    def ptt_callback(self, channel):
        #self.screen
        print ("ptt ")  #button actions  
    def up_callback(self, channel):
        self.isButtonSelected = True
        print ("up ")  #button actions  
    def down_callback(self, channel):
        self.isButtonSelected = False
        print ("down ")  #button actions  
    def left_callback(self, channel):
        self.isHomeSelected = False
        print ("left ")  #button actions  
    def right_callback(self, channel):
        self.isHomeSelected = True
        print ("right ")  #button actions  
    def center_callback(self, channel):
        # check which bools 
        # silent mode/switch screen
        print ("center ")  #button actions  
    def vol_up_callback(self, channel):
        print ("volume up ")  #button actions  
    def vol_down_callback(self, channel):
        print ("volume down ")  #button actions  
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.screen = Screen()
        self.ptt = 3        #GPIO = PTT button
        self.power = 5      #GPIO = power button
        self.up = 22        #GPIO = up button
        self.left = 18      #GPIO = down button
        self.center = 15    #GPIO = left button
        self.down = 16      #GPIO = right button
        self.right = 11     #GPIO = center button
        #vol_up = 8         #GPIO = volume up button
        #vol_down = 10      #GPIO = volume down button

        # no buttons selected when false
        # home selected when both true
        # silent selected when button true home false
        self.isButtonSelected = False
        self.isHomeSelected = False

        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP
        GPIO.add_event_detect(self.right, GPIO.RISING, callback=self.right_callback, bouncetime=500)




        #set each button pin as input pulled low
#        GPIO.setup(self.power, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        #check for rising edge trigger and perform event
#        GPIO.add_event_detect(self.power, GPIO.RISING, callback=self.power_callback, bouncetime=500)
        
#        GPIO.setup(self.ptt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.ptt, GPIO.RISING, callback=self.ptt_callback, bouncetime=500)

#        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.up, GPIO.RISING, callback=self.up_callback, bouncetime=500)
       
#        GPIO.setup(self.down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.down, GPIO.RISING, callback=self.down_callback, bouncetime=500)

#        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.left, GPIO.RISING, callback=self.left_callback, bouncetime=500)

#        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.right, GPIO.RISING, callback=self.right_callback, bouncetime=500)

#        GPIO.setup(self.center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.center, GPIO.RISING, callback=self.center_callback, bouncetime=500)

        #GPIO.setup(self.vol_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(self.vol_up, GPIO.RISING, callback=self.vol_up_callback, bouncetime=500)

        #GPIO.setup(self.vol_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(self.vol_down, GPIO.RISING, callback=self.vol_down_callback, bouncetime=500)
        
        #speaker?
        #microphone?
        #rumbler?
        #mode switch?
        raw_input("Hit enter to turn off screen")
        GPIO.cleanup()