import pygame
import math


class Tile(pygame.sprite.Sprite):

    def __init__(self, row, col, x, y, imag, type, disp_surf):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.image = imag
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.disp_surf = disp_surf

    def get_x(self):
        return self.rect.x * math.cos(math.radians(30))

    def get_y(self):
        return self.rect.y * math.sin(math.radians(30))
