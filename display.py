class Display:
    def __init__(self):
        # Create a 32-row by 64-column grid explicitly
        self.screen = []
        for _ in range(32):
            row = [0 for _ in range(64)]
            self.screen.append(row)

    def clear(self):
        self.screen = []
        for _ in range(32):
            row = [0 for _ in range(64)]
            self.screen.append(row)

    def set_pixel(self, x, y):
        """Draws a pixel using XOR. Returns True if a pixel is erased (collision/VF)."""
        x %= 64
        y %= 32
        
        self.screen[y][x] ^= 1
        return self.screen[y][x] == 0  # True if collision occurred