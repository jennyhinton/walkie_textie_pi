class Keyboard:
    def __init__(self):
        # Keyboard initialization stuff goes here
        self.caps_lock = False       #track capslock
        self.message = ['\0'] * 160  # message array initialized
        #7 rows -> input with pullup
        #5 cols no pullup input (high Z)
    
    def key_scan(self):
        sym = False        #character vs symbol
        current_char = 0   #current character
        current_symb = 0   #current symbol
        
        shift = False      #track shift key
        alt = False        #track alt key...idk the purpose of this yet
        backspace = False  #track backspace
        shiftl = False     #1/2 capslock
        shiftr = False     #1/2 capslock
        ret = False        #track return key
        
        # col 1 low
        # row 1 low: q , #
        # row 2 low: w , 1
        # row 3 low: symbol key
        # row 4 low: a , *
        # row 5 low: alt key
        # row 6 low: space , space
        # row 7 low: mic , 0
        
        # col 2 low
        # row 1 low: e , 2
        # row 2 low: s , 4
        # row 3 low: d , 5
        # row 4 low: p , @
        # row 5 low: x , 8
        # row 6 low: z , 7
        # row 7 low: shift -> leftshift key
        
        # col 3 low
        # row 1 low: r , 3
        # row 2 low: g , /
        # row 3 low: t , (
        # row 4 low: shift -> right shift key
        # row 5 low: v , ?
        # row 6 low: c , 9
        # row 7 low: f , 6
        
        # col 4 low
        # row 1 low: u , _
        # row 2 low: h , :
        # row 3 low: y , )
        # row 4 low: return key
        # row 5 low: b , !
        # row 6 low: n , ,
        # row 7 low: j , ;
        
        # col 5 low
        # row 1 low: o , +
        # row 2 low: l , \"
        # row 3 low: i , -
        # row 4 low: backspace key
        # row 5 low: $ , ""
        # row 6 low: m , .
        # row 7 low: k , \'
        
        if alt:
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
    
    