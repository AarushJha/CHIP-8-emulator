import sys
import pygame
from display import Display
from keypad import Keypad
from cpu import CPU

def main():
    pygame.init()
    SCALE = 10
    screen = pygame.display.set_mode((64 * SCALE, 32 * SCALE))
    pygame.display.set_caption("Modular CHIP-8 Emulator in Python")
    clock = pygame.time.Clock()

    display = Display()
    keypad = Keypad()
    cpu = CPU(display, keypad)

    # cpu.load_rom("roms/IBM Logo.ch8")
    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keypad.update_key(event.key, True)
            elif event.type == pygame.KEYUP:
                keypad.update_key(event.key, False)

        #run CPU cycles per frame
        for i in range(10):
            cpu.emulate_cycle()

        #update timers
        if cpu.delay_timer > 0:
            cpu.delay_timer -= 1
        if cpu.sound_timer > 0:
            cpu.sound_timer -= 1

        #render display buffers to the screen
        screen.fill((0, 0, 0))      
        for y in range(32):
            for x in range(64):
                if display.screen[y][x] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x * SCALE, y * SCALE, SCALE, SCALE))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

