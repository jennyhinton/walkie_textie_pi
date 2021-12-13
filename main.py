from screen import Screen
from buttons import Buttons
#from keyboard import Keyboard
from letter import Alphabet
from pynput import keyboard
import time

screen = Screen()

#pip install pynput
def on_press (key):
    try:
        screen.insert_character(Alphabet[key.char])
    except AttributeError:
        print("Key not defined yet/ keyboard error")

def on_release (key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(
        on_press = on_press,
        on_release = on_release) 
listener.start()


def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen.all_pixels_off()

    time.sleep(5)
    print ("5 secs")
    time.sleep(5)
    time.sleep(100)
    
if __name__ == "__main__":
    main()
