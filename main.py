from screen import Screen
from buttons import BUTTON_ICONS, Buttons
#from keyboard import Keyboard
from letter import Alphabet, Special
from pynput import keyboard
#from pynput.keyboard import Key

import time

buttons = Buttons()
screen = Screen(buttons)

#pip install pynput
def on_press (key):
    try:
        if key in Special:
            character = Special[key]
            if character == 'backspace':
                screen.insert_backspace()
        else: 
            character = key.char 
        if not buttons.isHomeSelected:
            screen.insert_character(Alphabet[character])
    except AttributeError:
        print("Key not defined yet/ keyboard error")
        print('Special: ' + str(Special[key]))
        print('character: ' + str(key.char))
    
    except Exception as e:
        print("Other Error: keeping program running")

def on_release (key):
    if key == keyboard.Key.esc:
        return False

# Add the listeners
listener = keyboard.Listener(
        on_press = on_press,
        on_release = on_release) 
listener.start()

def main():
    screen.all_pixels_off()

    icon = BUTTON_ICONS['home_inactive']['icon']
    row = BUTTON_ICONS['home_inactive']['row']
    col = BUTTON_ICONS['home_inactive']['col']
    screen.insert_icon(icon, row, col)
            
    icon = BUTTON_ICONS['message_inactive']['icon']
    row = BUTTON_ICONS['message_inactive']['row']
    col = BUTTON_ICONS['message_inactive']['col']
    screen.insert_icon(icon, row, col)

    icon = BUTTON_ICONS['vol_low']['icon']
    row = BUTTON_ICONS['vol_low']['row']
    col = BUTTON_ICONS['vol_low']['col']
    screen.insert_icon(icon, row, col)

    time.sleep(18000)

if __name__ == "__main__":
    main()
