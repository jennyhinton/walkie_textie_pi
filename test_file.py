import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    buttonState = GPIO.input(16)
    if buttonState == True:
        print("pressed")
    if buttonState == False:
        print ("not pressed")
        
        
GPIO.cleanup()
        