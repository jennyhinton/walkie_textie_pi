from screen import Screen
from buttons import Buttons
from keyboard import Keyboard

def main():
    keyboard = Keyboard()
    #buttons = Buttons()
    #screen = Screen()
    print ("10 things")
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    print (Keyboard.key_scan())
    
    print("5 things before print")
    keyboard.update_message(Keyboard.key_scan())
    keyboard.update_message(Keyboard.key_scan())
    keyboard.update_message(Keyboard.key_scan())
    keyboard.update_message(Keyboard.key_scan())
    keyboard.update_message(Keyboard.key_scan())
    print (Keyboard.message)

    print "Hit enter to end"
    input()
    GPIO.cleanup()

    
if __name__ == "__main__":
    main()
