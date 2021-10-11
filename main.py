from screen import Screen
from buttons import Buttons
from keyboard import Keyboard

def main():
    keyboard = Keyboard()
    #buttons = Buttons()
    #screen = Screen()
    
    button = Keyboard.key_scan()
    
    
    Keyboard.update_message(Keyboard.key_scan())
    Keyboard.update_message(Keyboard.key_scan())
    Keyboard.update_message(Keyboard.key_scan())
    Keyboard.update_message(Keyboard.key_scan())

    print(message)
    
    print "Hit enter to end"
    input()
    GPIO.cleanup()

    
if __name__ == "__main__":
    main()
