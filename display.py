class display:
    def __init__(self):
        # 64 columns by 32 rows, initialized to 0 (off)
        self.screen = [[0 for _ in range(64)] for _ in range(32)]
    
    def clear(self):
        self.screen = [[0 for _ in range(64)] for _ in range(32)]

    def set_pixel(self, x, y):
        #Draws a pixel using XOR. Returns True if a pixel is erased 
        #wrap around edges if coordinates exceed boundaries
        x %= 64
        y %=32

        self.screen[y][x] ^= 1
        return self.screen[y][x] == 0 #True if colison occured
    