# CHIP-8 Emulator in Python

A clean, modular implementation of the classic **CHIP-8** virtual machine written in **Python** using **Pygame**. This project is built from scratch to simulate low-level computer architecture, including memory management, opcode execution, graphics rendering, and keyboard input handling.

## 🏗️ Project Architecture (4-File Modular Design)

To maintain clean code separation and follow software engineering best practices, the project is split into four core modules:

1. **`main.py` (The Driver)**

   * Initializes Pygame and sets up the scaled graphics window.

   * Runs the main application loop at 60 FPS, pacing CPU cycles and updating 60Hz timers (`delay_timer` and `sound_timer`).

   * Captures window events and keyboard inputs.

2. **`cpu.py` (The Core Logic)**

   * Manages the 4 KB ($4096$ bytes) memory array, sixteen 8-bit data registers (`V0` through `VF`), the 16-bit Index register (`I`), and the Program Counter (`PC` starting at `0x200`).

   * Manages the subroutine stack and implements the fetch-decode-execute cycle.

   * Embeds the standard CHIP-8 character font set into memory.

3. **`display.py` (Graphics)**

   * Manages the monochrome $64 \times 32$ pixel screen buffer.

   * Implements pixel collision detection and XOR drawing operations.

4. **`keypad.py` (Input Management)**

   * Maps standard computer keyboard keys to the CHIP-8's 16-key hexadecimal layout (`0x0` through `0xF`).

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your system. You will also need the **Pygame** library for rendering and input handling.

### Installation & Setup

1. Clone or download this repository to your local machine:

   ```
   git clone https://github.com/your-username/chip8-emulator.git
   cd chip8-emulator
   
   ```

2. Install the required dependencies via pip:

   ```
   pip install pygame
   
   ```

3. Run the emulator:

   ```
   python main.py
   
   ```

## 🎮 Controls

The CHIP-8 uses a 16-key hexadecimal keypad. This emulator maps them to standard QWERTY keyboards as follows:

| CHIP-8 Keypad | QWERTY Key Mapping | 
| ----- | ----- | 
| `1` `2` `3` `C` | `1` `2` `3` `4` | 
| `4` `5` `6` `D` | `Q` `W` `E` `R` | 
| `7` `8` `9` `E` | `A` `S` `D` `F` | 
| `A` `0` `B` `F` | `Z` `X` `C` `V` | 

## 📚 Resources & References

* [Tobias V. Langhoff's CHIP-8 Guide](https://tobiasvl.github.io/blog/write-a-chip-8-emulator/) — Excellent conceptual deep-dive.

* [Cowgod's Technical Reference v1.1](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM) — The authoritative instruction set cheat sheet.
