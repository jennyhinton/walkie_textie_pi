from screen import Screen
from buttons import Buttons
from keyboard import Keyboard

def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen = Screen()
    
    print "Hit enter to end"
    message = input()
    
    GPIO.output(RST, GPIO.LOW)
    time.sleep(1)
    print "unplug now"
    GPIO.cleanup()

    
if __name__ == "__main__":
    main()
