import pygame

class Keypad:
    def __init__(self):
        self.keys = [0] * 16 # 16 keys -> 0 to F

        self.key_map = {pygame.K_1: 0x1, pygame.K_2: 0x2, pygame.K_3: 0x3, pygame.K_4: 0xC,
            pygame.K_q: 0x4, pygame.K_w: 0x5, pygame.K_e: 0x6, pygame.K_r: 0xD,
            pygame.K_a: 0x7, pygame.K_s: 0x8, pygame.K_d: 0x9, pygame.K_f: 0xE,
            pygame.K_z: 0xA, pygame.K_x: 0x0, pygame.K_c: 0xB, pygame.K_v: 0xF
        }

    def update_key(self, pygame_key, is_pressed):
        if pygame_key in self.key_map:
            index = self.key_map[pygame_key]
            self.keys[index] = 1 if is_pressed else 0