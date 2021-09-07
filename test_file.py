import RPi.GPIO as GPIO

GPIO.cleanup()

def power_callback(channel):
        print ("power pushed")  #button actions
        
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while (True):
    GPIO.add_event_detect(16, GPIO.RISING, callback=power_callback)

        
                