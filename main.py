from screen import Screen
from buttons import Buttons
from keyboard import Keyboard
from letter import Alphabet


def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen = Screen()
    screen.all_pixels_off()

    screen.insert_character(Alphabet['A'])
    screen.render_pixels()
    
if __name__ == "__main__":
    main()
