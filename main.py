from screen import Screen
from buttons import Buttons
from keyboard import Keyboard

def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen = Screen()
    
    message = input("Hit enter to end")
    
    GPIO.output(RST, GPIO.LOW)
    time.sleep(1)
    print "unplug now"
    GPIO.cleanup()

    
if __name__ == "__main__":
    main()
