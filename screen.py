import spidev
import RPi.GPIO as GPIO
import time
from letter import Alphabet

#figure out why/where spidev changes list to 0s

class Screen:
    def __init__(self):
        self.width = 102
        self.height = 64
        self.screen = [[0] * self.width] * self.height
        
        GPIO.setwarnings(False)
        self.spi0 = spidev.SpiDev()
        self.spi0.open(0,0)                #spi bus 0 with chip select 0
        self.spi0.max_speed_hz = 31200000  #speeds up to 33 MHz. This is 31.2MHz
        GPIO.setmode(GPIO.BOARD) #Use pin numbers to identify gpio
        self.CD = 10
        self.RST = 33 
        GPIO.setup(self.CD,GPIO.OUT)   #set pin 3 (GPIO 2) as output for CD pin
        GPIO.setup(self.RST,GPIO.OUT)   #reset pin

        #Screen commands as uint16        
        display_start_line = int("40", 16)    #start line at 0
        set_SEG_bottom = int("A1", 16)        #bottom (normal) view
        set_direction_normal = int("C0", 16)  #com0-com63
        disable_all_pixels = int("A4",16)
        enable_all_pixels = int("A5",16)
        disable_inverse_display = int("A6",16)
        set_bias = int("A2",16)                 # bias 1/9 (duty 1/65)
        set_power_control = int("2F",16)        #set power control, booster, regulator and follower on
        set_contrast1 = int("27", 16)
        set_contrast2 = int("81", 16)
        set_contrast3 = int("10", 16)
        set_temp_comp_curve1 = int("FA", 16)     #set to -0.11 %/C
        set_temp_comp_curve2 = int("90", 16)
        enable_display = int("AF", 16)
        disable_display = int("AE", 16)
        
        
        self.startup_commands = [
            display_start_line,
            set_SEG_bottom,
            set_direction_normal,
            
            disable_all_pixels,
            disable_inverse_display,
            
            set_bias,
            set_power_control,
            set_contrast1,
            set_contrast2,
            set_contrast3,
            
            set_temp_comp_curve1,
            set_temp_comp_curve2,
            
            enable_display
        ]
        self.sleep_commands = [
            disable_display,
            enable_all_pixels
        ]
        self.wakeup_commands = [
            disable_all_pixels,
            enable_display
        ]

        #power on, set reset low and wait a sec then set reset high and wait 5 sec
        GPIO.output(self.RST, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.RST, GPIO.HIGH)
        time.sleep(5)
        
        #issue commands and wait a second
        GPIO.output(self.CD, GPIO.LOW)    #set CD pin low for command mode
        self.spi0.xfer3(self.startup_commands) #send initialization commands
        GPIO.output(self.CD, GPIO.HIGH)   #set CD pin high for data mode
        
        self.page1 = int("B0",16)
        self.page2 = int("B1",16)
        self.page3 = int("B2",16)
        self.page4 = int("B3",16)
        self.page5 = int("B4",16)
        self.page6 = int("B5",16)
        self.page7 = int("B6",16)
        self.page8 = int("B7",16)
            
        self.all_pages = [
            self.page1,
            self.page2,
            self.page3,
            self.page4,
            self.page5,
            self.page6,
            self.page7,
            self.page8
        ]
        
        #starting location for pixels
        self.colptr = 0
        self.rowptr = 0
  
    def sleep_mode(self):
        GPIO.output(self.CD, GPIO.LOW)
        self.spi0.xfer3(self.sleep_commands) 
        GPIO.output(self.CD, GPIO.HIGH)
    
    def wake_up(self):
        GPIO.output(self.CD, GPIO.LOW)
        self.spi0.xfer3(self.wakeup_commands) 
        GPIO.output(self.CD, GPIO.HIGH)

    def turn_off(self):
        raw_input("Hit enter to turn off screen")
        GPIO.output(self.RST, GPIO.LOW)
        time.sleep(1)
        print("unplug now")
        GPIO.cleanup()
        
    def get_page_and_bit(self, row):
        page = row // 8
        bit = row % 8
        return page, bit
    
    def read_binary_from_screen(self):
        for page_id in range(8): #[0, 1, 2, 3, 4, 5, 6, 7]
            start_idx = page_id * 8
            end_idx = start_idx + 7
            page = self.screen[start_idx:end_idx]
            for pixel_group in range(102):
                bin_number = []      

    def render_pixels(self):
        for row in range(0,64,8): 
            for col in range(132):
                dummy_screen_cols = []
                dummy_screen_cols.append([str(r[col]) for r in self.screen[row:row + 8]])
                dummy_screen_cols[-1] = ''.join(dummy_screen_cols[-1])
                bits = int(dummy_screen_cols[0], 2)
                self.set_pixel(row, col, bits)

    def set_pixel(self, row, col, bits):     #bits is decimal value of bits to set
        #bottom -> top : [0-F][0-F]
        page, bit = self.get_page_and_bit(row)
        
        pixelon_commands = [
            bits
        ]
        
        col = hex(col)
        colL = '0' + col[-1]
        colM = '1' + col[-2]
        location_commands = [
            self.all_pages[page-1],
            int(colL,16),
            int(colM,16)
            ]
        GPIO.output(self.CD, GPIO.LOW)
        self.spi0.xfer3(location_commands)
        GPIO.output(self.CD, GPIO.HIGH)
        self.spi0.xfer3(pixelon_commands)
    
    def all_pixels_off(self):
        pixeloff_commands = [
            int("00",16)
        ]
        collsb = [0]*132
        colmsb = [0]*132
        for x in range(132):
            index = x
            if x in range(16):
                x = hex(x)
                collsb[index] = x[-1]
                colmsb[index] = '0'
            else:
                x = hex(x)
                collsb[index] = x[-1]
                colmsb[index] = x[-2]
        for y in range(8):
            for x in range(102):
                temp1 = collsb[x]
                var1 = '0' + temp1
                temp = colmsb[x]
                var = '1' + temp
                location_commands = [
                    int(var1,16),  #set LSB col address
                    int(var,16),  #set MSB col address
                    self.all_pages[y]  #set self.page address
                ]
                GPIO.output(self.CD, GPIO.LOW)
                self.spi0.xfer3(location_commands)
                GPIO.output(self.CD, GPIO.HIGH)
                self.spi0.xfer3(pixeloff_commands)
        
    def insert_character(self, character):
        char_width = len(character[0])
        char_height = len(character)
        
        # check horizontal bounds - push character to next row as needed
        if char_width + self.colptr > self.width:
            self.colptr = 0
            self.rowptr = self.rowptr + char_height + 1
        
        # check vertical bounds - push all rows up
        if self.rowptr + char_height > self.height:
            self.rowptr = self.rowptr - char_height - 1
            #for the whole screen move pixels up if valid then turn off old pixel...
            #play with self.height and self.width when end of text row is known
            for col in range(self.height): 
                for row in range(self.width):
                    if self.screen[col][row] == 1:
                        if row > char_height:
                            self.screen[col][row-char_height -1] = 1
                        self.screen[col][row] = 0
            
        for col in range(char_width): 
            for row in range(char_height):
                if character[row][col]:
                    #col ptr and row ptr are the top left position of character inserting
                    #col and row are the position of the specific character inserting
                    self.screen[self.colptr + col][self.rowptr + row] = 1
        self.colptr = self.colptr + char_width