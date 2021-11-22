import RPi.GPIO as GPIO


def power_callback(channel):
        print ("pushed")  #button actions
        
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(8, GPIO.RISING, callback=power_callback)#, bouncetime=500)

raw_input("Hit enter to end")

GPIO.cleanup()

        
                
                