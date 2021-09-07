import RPi.GPIO as GPIO


GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    buttonState = GPIO.input(16)
    if buttonsState == True:
        print("pressed")
        