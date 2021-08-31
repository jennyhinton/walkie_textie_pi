import RPi.GPIO as GPIO

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
        
        #Configure rows/cols with each pin
        row1 =  #GPIO  = row 1
        row2 =  #GPIO  = row 2
        row3 =  #GPIO  = row 3
        row4 =  #GPIO  = row 4
        row5 =  #GPIO  = row 5
        row6 =  #GPIO  = row 6
        row7 =  #GPIO  = row 7
        
        col1 =  #GPIO  = col 1
        col2 =  #GPIO  = col 2
        col3 =  #GPIO  = col 3
        col4 =  #GPIO  = col 4
        col5 =  #GPIO  = col 5
        
        #configure rows active low input and colums output
        #pull col low and check which row is low. get corresponding
        #key then reset col and move on
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(row1 , GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.setup(row2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(row3 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(row4 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(row5 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(row6 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(row7 , GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(col1 , GPIO.OUT)
        GPIO.setup(col2 , GPIO.OUT)
        GPIO.setup(col3 , GPIO.OUT)
        GPIO.setup(col4 , GPIO.OUT)
        GPIO.setup(col5 , GPIO.OUT)
    
    def key_scan(self):
        sym = False        #character vs symbol
        current_char = 0   #current character
        current_symb = 0   #current symbol
        
        shift = False      #track shift key
        alt = False        #track alt key...idk the purpose of this yet
        mic = False        #I dont think were using this but track anyway
        backspace = False  #track backspace
        shiftl = False     #1/2 capslock
        shiftr = False     #1/2 capslock
        ret = False        #track return key
        
        #set col low
        GPIO.output(col1, GPIO.LOW)
        # check which row is low and get each char/symbol for key
        if GPIO.input(row1) == LOW:
            current_char = "q"
            current_symb = "#"
        if GPIO.intput(row2) == LOW:
            current_char = "w"
            current_symb = "1"
        if GPIO.intput(row3) == LOW:
            sym = True
        if GPIO.intput(row4) == LOW:
            current_char = "a"
            current_symb = "*"
        if GPIO.intput(row5) == LOW:
            alt = True
        if GPIO.intput(row6) == LOW:
            current_char = " "
            current_symb = " "
        if GPIO.intput(row7) == LOW:
            current_char = "mic"
            current_symb = "0"
        #reset col high and move through each col
        GPIO.output(col1, GPIO.High)
        
        GPIO.output(col2, GPIO.LOW)
        if GPIO.input(row1) == LOW:
            current_char = "e"
            current_symb = "2"
        if GPIO.intput(row2) == LOW:
            current_char = "s"
            current_symb = "4"
        if GPIO.intput(row3) == LOW:
            current_char = "d"
            current_symb = "5"
        if GPIO.intput(row4) == LOW:
            current_char = "p"
            current_symb = "@"
        if GPIO.intput(row5) == LOW:
            current_char = "x"
            current_symb = "8"
        if GPIO.intput(row6) == LOW:
            current_char = "z"
            current_symb = "7"
        if GPIO.intput(row7) == LOW:
            shift = True
            shiftl = True
        GPIO.output(col2, GPIO.High)

        GPIO.output(col3, GPIO.LOW)
        if GPIO.input(row1) == LOW:
            current_char = "r"
            current_symb = "3"
        if GPIO.intput(row2) == LOW:
            current_char = "g"
            current_symb = "/"
        if GPIO.intput(row3) == LOW:
            current_char = "t"
            current_symb = "("
        if GPIO.intput(row4) == LOW:
            shift = True
            shiftr = True
        if GPIO.intput(row5) == LOW:
            current_char = "v"
            current_symb = "?"
        if GPIO.intput(row6) == LOW:
            current_char = "c"
            current_symb = "9"
        if GPIO.intput(row7) == LOW:
            current_char = "f"
            current_symb = "6"
        GPIO.output(col3, GPIO.High)       
        
        GPIO.output(col4, GPIO.LOW)
        if GPIO.input(row1) == LOW:
            current_char = "u"
            current_symb = "_"
        if GPIO.intput(row2) == LOW:
            current_char = "h"
            current_symb = ":"
        if GPIO.intput(row3) == LOW:
            current_char = "y"
            current_symb = ")"
        if GPIO.intput(row4) == LOW:
            ret = True
        if GPIO.intput(row5) == LOW:
            current_char = "b"
            current_symb = "!"
        if GPIO.intput(row6) == LOW:
            current_char = "n"
            current_symb = ","
        if GPIO.intput(row7) == LOW:
            current_char = "j"
            current_symb = ";"
        GPIO.output(col4, GPIO.High) 

        GPIO.output(col3, GPIO.LOW)
        if GPIO.input(row1) == LOW:
            current_char = "o"
            current_symb = "+"
        if GPIO.intput(row2) == LOW:
            current_char = "l"
            current_symb = "\""
        if GPIO.intput(row3) == LOW:
            current_char = "i"
            current_symb = "-"
        if GPIO.intput(row4) == LOW:
            backspace = True
        if GPIO.intput(row5) == LOW:
            current_char = "$"
            current_symb = ""
        if GPIO.intput(row6) == LOW:
            current_char = "m"
            current_symb = "."
        if GPIO.intput(row7) == LOW:
            current_char = "k"
            current_symb = "\'"
        GPIO.output(col5, GPIO.High)
        
        
        #idk what im doing with alt or mic yet so rn nothing
        if alt:
            return ""
        if current_char = "mic":
            return ""
         
        if backspace:
            return "backspace"
        if ret:
            return "\n"
        if shiftl and shiftr:
            capslock = not capslock
            return ""
        if capslock:
            shift = True
        if shift:
            current_char = current_char - 32
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
            
        if input == "backspace":
            if index == 0:
                return
            else:
                message[index - 1] = '\0'
                return
        
        if index == 160:
            pass         #this will need taken care of

        if index != 160:
            message[index] = input
    
    