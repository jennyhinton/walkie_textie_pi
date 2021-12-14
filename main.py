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
        print(key)
        screen.insert_character(Alphabet[key.char])
    except AttributeError:
        print("key is:")
        print(key)
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

    time.sleep(300)

if __name__ == "__main__":
    main()
