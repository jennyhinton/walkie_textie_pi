import RPi.GPIO as GPIO
import time
from letter import Alphabet
from screen import Screen


#need to assign GPIOs
#need to set up storing messages/deleting and such
#need to check col 5 row 5
#need to check all cols and rows
#check alt and mic functionality

class Keyboard:
    def __init__(self):
        # Keyboard initialization stuff goes here
        self.caps_lock = False       # track capslock
        self.message = ['\0'] * 160  # message array initialized
        self.screen = Screen()
        
    
    def key_scan(self):       
        sym = False        #character vs symbol
        current_char = "nothing"   #current character
        current_symb = None   #current symbol
        
        shift = False      #track shift key
        alt = False        #track alt key...idk the purpose of this yet
        mic = False        #I dont think were using this but track anyway
        backspace = False  #track backspace
        shiftl = False     #1/2 capslock
        shiftr = False     #1/2 capslock
        ret = False        #track return key
        
        if input == 'a':
            self.screen.insert_character(Alphabet['A'])
        


        
        #set col low
        GPIO.setup(self.col1, GPIO.OUT)
        GPIO.output(self.col1, GPIO.LOW)
        # check which row is low and get each char/symbol for key
        if GPIO.input(self.row1) == 0:
            current_char = "q"
            current_symb = "#"
        if GPIO.input(self.row2) == 0:
            current_char = "w"
            current_symb = "1"
        print("Col 1 Row 3 State: ", GPIO.input(self.row3))
        if GPIO.input(self.row3) == 0:
            sym = True
        if GPIO.input(self.row4) == 0:
            current_char = "a"
            current_symb = "*"
        if GPIO.input(self.row5) == 0:
            alt = True
        if GPIO.input(self.row6) == 0:
            current_char = " "
            current_symb = " "
        if GPIO.input(self.row7) == 0:
            current_char = "mic"
            current_symb = "0"
        #reset col HIGH and move through each col
        GPIO.setup(self.col1, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        
        GPIO.setup(self.col2, GPIO.OUT)
        GPIO.output(self.col2, GPIO.LOW)
        if GPIO.input(self.row1) == 0:
            current_char = "e"
            current_symb = "2"
        if GPIO.input(self.row2) == 0:
            current_char = "s"
            current_symb = "4"
        print("Col 2 Row 3 State: ", GPIO.input(self.row3))
        if GPIO.input(self.row3) == 0:
            current_char = "d"
            current_symb = "5"
        if GPIO.input(self.row4) == 0:
            current_char = "p"
            current_symb = "@"
        if GPIO.input(self.row5) == 0:
            current_char = "x"
            current_symb = "8"
        if GPIO.input(self.row6) == 0:
            current_char = "z"
            current_symb = "7"
        if GPIO.input(self.row7) == 0:
            shift = True
            shiftl = True
        GPIO.setup(self.col2, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

        GPIO.setup(self.col3, GPIO.OUT)
        GPIO.output(self.col3, GPIO.LOW)
        if GPIO.input(self.row1) == 0:
            current_char = "r"
            current_symb = "3"
        if GPIO.input(self.row2) == 0:
            current_char = "g"
            current_symb = "/"
        if GPIO.input(self.row3) == 0:
            current_char = "t"
            current_symb = "("
        if GPIO.input(self.row4) == 0:
            shift = True
            shiftr = True
        if GPIO.input(self.row5) == 0:
            current_char = "v"
            current_symb = "?"
        if GPIO.input(self.row6) == 0:
            current_char = "c"
            current_symb = "9"
        if GPIO.input(self.row7) == 0:
            current_char = "f"
            current_symb = "6"
        
        if GPIO.input(self.row1) == 0:
            current_char = "u"
            current_symb = "_"
        if GPIO.input(self.row2) == 0:
            current_char = "h"
            current_symb = ":"
        if GPIO.input(self.row3) == 0:
            current_char = "y"
            current_symb = ")"
        if GPIO.input(self.row4) == 0:
            ret = True
        if GPIO.input(self.row5) == 0:
            current_char = "b"
            current_symb = "!"
        if GPIO.input(self.row6) == 0:
            current_char = "n"
            current_symb = ","
        if GPIO.input(self.row7) == 0:
            current_char = "j"
            current_symb = ";"
        GPIO.setup(self.col4, GPIO.IN, pull_up_down=GPIO.PUD_OFF) 

        GPIO.setup(self.col5, GPIO.OUT)
        GPIO.output(self.col5, GPIO.LOW)
        if GPIO.input(self.row1) == 0:
            current_char = "o"
            current_symb = "+"
        if GPIO.input(self.row2) == 0:
            current_char = "l"
            current_symb = "\""
        if GPIO.input(self.row3) == 0:
            print("Row 3 Column 5")
            current_char = "i"
            current_symb = "-"
        if GPIO.input(self.row4) == 0:
            print("Row 4 Column 5")
            backspace = True
        if GPIO.input(self.row5) == 0:
            current_char = "$"
            current_symb = ""
        if GPIO.input(self.row6) == 0:
            current_char = "m"
            current_symb = "."
        if GPIO.input(self.row7) == 0:
            current_char = "k"
            current_symb = "\'"
        GPIO.setup(self.col5, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
        print("5 second wait")
        time.sleep(5)
        #idk what im doing with alt or mic yet so rn nothing
        
        #if alt:
        #    print("alt is set")
        #    return ""
        #if current_char = "mic":
        #    return ""
         
        #if backspace:
        #    return "backspace"
        #if ret:
        #    print("return")
        #    return "\n"
        #if shiftl and shiftr:
        #    print("shifts")
        #    self.capslock = not self.capslock
        #    return ""
        #if self.capslock:
        #    print("capslock")
        #    shift = True
        #if shift:
        #    print("capital")
        #    current_char = current_char - 32
        if sym:
            return current_symb
        else:
            return current_char
        
    def update_message(input):
        if input == "":   #do nothing
            pass
        
        index = 160
        for i in range(len(self.message)):
            if self.message[i] == '\0':
                index = i;
                break
            
        #if input == "backspace":
        #    if index == 0:
        #        return
        #    else:
        #        message[index - 1] = '\0'
        #        return
        
        if index == 160:
            pass         #this will need taken care of

        if index != 160:
            self.message[index] = input
    
    