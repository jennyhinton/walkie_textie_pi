from screen import Screen
from buttons import BUTTON_ICONS, Buttons
#from keyboard import Keyboard
from letter import Alphabet, Special
from pynput import keyboard
#from pynput.keyboard import Key

import time


screen = Screen()

#pip install pynput
def on_press (key):
    try:
        if key in Special:
            character = Special[key]
        else: 
            character = key.char 
        screen.insert_character(Alphabet[character])
    except AttributeError:
        print("Key not defined yet/ keyboard error")
    
    except Exception as e:
        print(e)

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
    screen.insert_icon(BUTTON_ICONS['message_inactive'],1,1)

    time.sleep(300)

if __name__ == "__main__":
    main()
