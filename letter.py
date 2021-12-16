from pynput.keyboard import Key

A = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    ]
B = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    ]
C = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
]
D = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
]
E = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
]
F = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
G = [
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
H = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
]
I = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
]
J = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
]
K = [
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
]
L = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
]
M = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
]
N = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
]
O = [
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
]
P = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]
Q = [
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
R = [
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
]
S = [
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
]
T = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
U = [
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
V = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
W = [
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
]
X = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
]
Y = [
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]
Z = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
]

SPACE = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
PERIOD = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]
COMMA = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
]
EXCLAMATION = [
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 0],
    [1, 0],
]
QUESTION = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
]
OPEN_PARENTHESIS = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
]
CLOSE_PARENTHESIS = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 0, 0],
]

NOTHING = [
    [],
    [],
    [],
    [],
    [],
]
ZERO = [
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
]
ONE = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
]
TWO = [
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
]
THREE = [
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
FOUR = [
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
]
FIVE = [
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
SIX = [
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
SEVEN = [
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
]
EIGHT = [
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]
NINE = [
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0],
]


Alphabet = {
        'a': A,
        'A': A,
        'b': B,
        'B': B,
        'c': C,
        'C': C,
        'd': D,
        'D': D,
        'e': E,
        'E': E,
        'f': F,
        'F': F,
        'g': G,
        'G': G,
        'h': H,
        'H': H,
        'i': I,
        'I': I,
        'j': J,
        'J': J,
        'k': K,
        'K': K,
        'l': L,
        'L': L,
        'm': M,
        'M': M,
        'n': N,
        'N': N,
        'o': O,
        'O': O,
        'p': P,
        'P': P,
        'q': Q,
        'Q': Q,
        'r': R,
        'R': R,
        's': S,
        'S': S,
        't': T,
        'T': T,
        'u': U,
        'U': U,
        'v': V,
        'V': V,
        'w': W,
        'W': W,
        'x': X,
        'X': X,
        'y': Y,
        'Y': Y,
        'z': Z,
        'Z': Z,
        'Space': SPACE,
        '.': PERIOD,
        ',': COMMA,
        '!': EXCLAMATION,
        '?': QUESTION,
        '(': OPEN_PARENTHESIS,
        ')': CLOSE_PARENTHESIS,
        '': NOTHING,
        '0': ZERO,
        '1': ONE,
        '2': TWO,
        '3': THREE,
        '4': FOUR,
        '5': FIVE,
        '6': SIX,
        '7': SEVEN,
        '8': EIGHT,
        '9': NINE
    }

Special = {
        Key.space : 'Space',
        Key.backspace : 'Backspace',
        Key.enter : 'Enter',
        Key.tab : '',
        Key.delete : '',
        Key.tab : '',
        Key.end : '',
        Key.esc : '',
        Key.home : '',
        Key.insert : '',
        Key.caps_lock : '',
        Key.shift : '',
        Key.alt : '',
        Key.alt_gr : '',
        Key.alt_l : '',
        Key.alt_r : '',
        Key.menu : '',
        Key.num_lock : '',
        Key.page_down : '',
        Key.page_up : '',
        Key.pause : '',
        Key.shift_l : '',
        Key.shift_r : '',
        Key.up : '',
        Key.down : '',
        Key.left : '',
        Key.right : '',
        Key.cmd : '',
        Key.cmd_l : '',
        Key.cmd_r : '',
        Key.ctrl : '',
        Key.ctrl_l : '',
        Key.ctrl_r : '',      
}