from screen import Screen
from buttons import Buttons
#from keyboard import Keyboard
from letter import Alphabet
from pynput import keyboard

screen = Screen()

#pip install pynput
def on_press (key):
    try:
        screen.insert_character(Alphabet[key.char])
    except AttributeError:
        print("Key not defined yet/ keyboard error")

with keyboard.Listener(
        on_press= on_press) as listener:
    listener.start()


def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen.all_pixels_off()

    
if __name__ == "__main__":
    main()
