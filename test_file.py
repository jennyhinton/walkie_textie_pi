import RPi.GPIO as GPIO

def power_callback(self, channel):
        print ("power pushed")  #button actions
        
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING, callback=self.power_callback)

        
        
GPIO.cleanup()
        