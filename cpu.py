import sys 

FONTSET = [
    0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
    0x20, 0x60, 0x20, 0x20, 0x70,  # 1
    0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
    0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
    0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
    0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
    0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
    0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
    0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
    0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
    0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
    0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
    0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
    0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
    0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
    0xF0, 0x80, 0xF0, 0x80, 0x80   # F
]

class CPU:
    def __init__(self, display, keypad):
        self.memory = bytearray(4096)
        self.v = bytearray(16)
        self.i = 0
        self.pc = 0x200
        self.stack = [0] * 16
        self.sp = 0

        self.delay_timer = 0
        self.sound_timer = 0

        self.display = display
        self.keypad = keypad

        # Load fontset into memory at 0x50
        self.memory[0x50:0x50 + len(FONTSET)] = FONTSET

    def load_room(self, filename):
        with open(filename, "rb") as f:
            rom_data = f.read()
            self.memory[0x200:0x200 + len(rom_data)] = rom_data

    def emulate_cycle(self):
        # Stop execution if Program Counter goes beyond memory bounds
        if self.pc >= len(self.memory) - 1:
            return

        # Fetch 2-byte opcode
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        self.pc += 2
        # Fetch 2-byte opcode
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        self.pc += 2

        # Decode opcode categories based on the first nibble
        # Extract common nibbles/values for convenience
        nnn = opcode & 0x0FFF
        nn = opcode & 0x00FF
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        n = opcode & 0x000F

        # Match opcodes
        if opcode == 0x00E0:
            # 00E0: Clear the display
            self.display.clear()

        elif opcode == 0x00EE:
            # 00EE: Return from a subroutine
            self.sp -= 1
            self.pc = self.stack[self.sp]

        elif (opcode & 0xF000) == 0x1000:
            # 1NNN: Jump to address NNN
            self.pc = nnn

        elif (opcode & 0xF000) == 0x2000:
            # 2NNN: Call subroutine at NNN
            self.stack[self.sp] = self.pc
            self.sp += 1
            self.pc = nnn

        elif (opcode & 0xF000) == 0x6000:
            # 6XNN: Set register VX to NN
            self.v[x] = nn

        elif (opcode & 0xF000) == 0x7000:
            # 7XNN: Add NN to register VX (without carrying VF)
            self.v[x] = (self.v[x] + nn) & 0xFF

        elif (opcode & 0xF000) == 0xA000:
            # ANNN: Set index register I to NNN
            self.i = nnn

        elif (opcode & 0xF000) == 0x3000:
            # 3XNN: Skip next instruction if VX equals NN
            if self.v[x] == nn:
                self.pc += 2

        elif (opcode & 0xF000) == 0x4000:
            # 4XNN: Skip next instruction if VX does not equal NN
            if self.v[x] != nn:
                self.pc += 2

        elif (opcode & 0xF000) == 0x5000:
            # 5XY0: Skip next instruction if VX equals VY
            if self.v[x] == self.v[y]:
                self.pc += 2

        elif (opcode & 0xF000) == 0x9000:
            # 9XY0: Skip next instruction if VX does not equal VY
            if self.v[x] != self.v[y]:
                self.pc += 2

        elif (opcode & 0xF000) == 0xD000:
            # DXYN: Draw a sprite at coordinate (VX, VY) with height N
            x_coord = self.v[x]
            y_coord = self.v[y]
            height = n
            
            # Reset VF (collision flag) to 0
            self.v[0xF] = 0
            
            # Fetch sprite data from memory starting at index I
            sprite_bytes = self.memory[self.i : self.i + height]
            
            # Pass data to display module and check for pixel collision
            pixel_collision = self.display.draw_sprite(x_coord, y_coord, sprite_bytes)
            if pixel_collision:
                self.v[0xF] = 1

        else:
            print(f"Unimplemented opcode: {hex(opcode)}")
