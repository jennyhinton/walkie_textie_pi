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
        'home_active': {
            'row': 1,
            'col': 1,
            'icon': HOME_active
        },
        'home_inactive': {
            'row': 1,
            'col': 1,
            'icon': HOME_inactive
        },
        'message_active': {
            'row': 1,
            'col': 85,
            'icon': MESSAGE_active
        },
        'message_inactive': {
            'row': 1,
            'col': 85,
            'icon': MESSAGE_inactive
        }
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
        print ("up ")
        self.isButtonSelected = True

        if self.isHomeSelected:
            icon = BUTTON_ICONS['home_active']['icon']
            row = BUTTON_ICONS['home_active']['row']
            col = BUTTON_ICONS['home_active']['col']
            self.screen.insert_icon(icon, row, col)
        else:
            icon = BUTTON_ICONS['message_active']['icon']
            row = BUTTON_ICONS['message_active']['row']
            col = BUTTON_ICONS['message_active']['col']
            self.screen.insert_icon(icon, row, col)

    def down_callback(self, channel):
        print ("down ") 
        self.isButtonSelected = False
        icon = BUTTON_ICONS['home_inactive']['icon']
        row = BUTTON_ICONS['home_inactive']['row']
        col = BUTTON_ICONS['home_inactive']['col']
        self.screen.insert_icon(icon, row, col)
            
        icon = BUTTON_ICONS['message_inactive']['icon']
        row = BUTTON_ICONS['message_inactive']['row']
        col = BUTTON_ICONS['message_inactive']['col']
        self.screen.insert_icon(icon, row, col)
         
    def left_callback(self, channel):
        print ("left ")  
        self.isHomeSelected = False
        if self.isButtonSelected:
            icon = BUTTON_ICONS['home_active']['icon']
            row = BUTTON_ICONS['home_active']['row']
            col = BUTTON_ICONS['home_active']['col']
            self.screen.insert_icon(icon, row, col)
            
            icon = BUTTON_ICONS['message_inactive']['icon']
            row = BUTTON_ICONS['message_inactive']['row']
            col = BUTTON_ICONS['message_inactive']['col']
            self.screen.insert_icon(icon, row, col)
        
    def right_callback(self, channel):
        print ("right ")
        self.isHomeSelected = True
        if self.isButtonSelected:
            icon = BUTTON_ICONS['home_inactive']['icon']
            row = BUTTON_ICONS['home_inactive']['row']
            col = BUTTON_ICONS['home_inactive']['col']
            self.screen.insert_icon(icon, row, col)
            
            icon = BUTTON_ICONS['message_active']['icon']
            row = BUTTON_ICONS['message_active']['row']
            col = BUTTON_ICONS['message_active']['col']
            self.screen.insert_icon(icon, row, col)

    def center_callback(self, channel):
        # check which bools 
        # silent mode/switch screen
        print ("center ")  #button actions  
    def vol_up_callback(self, channel):
        print ("volume up ")
        if self.volume_level !=4:
            self.volume_level = self.volume_level+1

    def vol_down_callback(self, channel):
        print ("volume down")
        if self.volume_level !=0:
            self.volume_level = self.volume_level-1
    
    def __init__(self, screen):
        GPIO.setmode(GPIO.BOARD)
        self.screen = screen
        self.volume_level = 1

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
        self.isHomeSelected = True


        #set each button pin as input pulled low
#        GPIO.setup(self.power, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        #check for rising edge trigger and perform event
#        GPIO.add_event_detect(self.power, GPIO.RISING, callback=self.power_callback, bouncetime=500)
        
#        GPIO.setup(self.ptt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#        GPIO.add_event_detect(self.ptt, GPIO.RISING, callback=self.ptt_callback, bouncetime=500)

        GPIO.setup(self.up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.up, GPIO.RISING, callback=self.up_callback, bouncetime=500)
       
        GPIO.setup(self.down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.down, GPIO.RISING, callback=self.down_callback, bouncetime=500)

        GPIO.setup(self.left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.left, GPIO.RISING, callback=self.left_callback, bouncetime=500)

        GPIO.setup(self.right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.right, GPIO.RISING, callback=self.right_callback, bouncetime=500)

        GPIO.setup(self.center, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.center, GPIO.RISING, callback=self.center_callback, bouncetime=500)

        #GPIO.setup(self.vol_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(self.vol_up, GPIO.RISING, callback=self.vol_up_callback, bouncetime=500)

        #GPIO.setup(self.vol_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.add_event_detect(self.vol_down, GPIO.RISING, callback=self.vol_down_callback, bouncetime=500)