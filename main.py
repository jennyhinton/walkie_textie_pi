from screen import Screen
from buttons import Buttons
from keyboard import Keyboard
from letter import Alphabet


def main():
    #keyboard = Keyboard()
    #buttons = Buttons()
    screen = Screen()
    screen.all_pixels_off()
    
    print("letters")

    for _ in range(50):
        screen.insert_character(Alphabet['A'])
        screen.insert_character(Alphabet['B'])
        screen.insert_character(Alphabet['C'])
    
if __name__ == "__main__":
    main()
