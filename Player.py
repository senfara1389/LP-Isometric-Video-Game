import pygame
import math


class Player(pygame.sprite.Sprite):

    def __init__(self, DISPLAY_SURF, map, tiles):
        pygame.sprite.Sprite.__init__(self)
        self.disp_surf = DISPLAY_SURF
        self.map = map
        self.tiles = tiles
        self.image = pygame.image.load('assets/images/forklift_up_left.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.row = map.start[0]
        self.col = map.start[1]
        self.rect.x = map.player_pos[0]
        self.rect.y = map.player_pos[1]
        self.orn = "W"
        self.currentx = self.rect.x
        self.currenty = self.rect.y
        self.speedx = 0
        self.speedy = 0
        self.state = False

    def update(self, x):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            if self.state == False:
                self.image = pygame.image.load('assets/images/forklift_up_left.png').convert_alpha()
            elif self.state == True:
                self.image = pygame.image.load('assets/images/forklift_left_box.png').convert_alpha()
            sub_x = self.rect.x % 32
            cen_x, cen_y = self.get_pos(self.col, self.row)
            if self.orn == "N" or self.orn == "S":
                if self.orn == "N":
                    if 24 >= sub_x > 4 and self.map.map_data[self.row - 1][self.col] == 0:
                        self.row = self.row - 1
                        self.rect.x = cen_x + 32
                        self.rect.y = cen_y - 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    else:
                        self.rect.x = cen_x
                        self.rect.y = cen_y
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                elif self.orn == "S":
                    if (sub_x >= 24 or sub_x < 12) and self.map.map_data[self.row + 1][self.col] == 0:
                        self.row = self.row + 1
                        self.rect.x = cen_x - 32
                        self.rect.y = cen_y + 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    else:
                        self.rect.x = cen_x
                        self.rect.y = cen_y
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                self.orn = "W"
            elif self.orn == "E":
                self.orn = "W"
                if (4 < sub_x <= 24) and self.map.map_data[self.row][self.col + 1] == 0:
                    self.col = self.col + 1
                    self.rect.x = cen_x + 32
                    self.rect.y = cen_y + 16
                    self.currentx = self.rect.x
                    self.currenty = self.rect.y
            else:
                self.orn = "W"
                if self.map.map_data[self.row][self.col - 1] == 0:
                    xdif = abs(self.rect.x - self.currentx)
                    if xdif == 32:
                        self.col = self.col - 1
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    self.speedx -= 2 * math.cos(math.radians(30))
                    self.speedy -= 2 * math.sin(math.radians(30))
                else:
                    self.speedy = 0
                    self.speedx = 0

        elif keystate[pygame.K_RIGHT]:
            if self.state == False:
                self.image = pygame.image.load('assets/images/forklift_down_right.png').convert_alpha()
            elif self.state == True:
                self.image = pygame.image.load('assets/images/forklift_right_box.png').convert_alpha()
            sub_x = self.rect.x % 32
            cen_x, cen_y = self.get_pos(self.col, self.row)
            if self.orn == "N" or self.orn == "S":
                if self.orn == "N":
                    if 24 >= sub_x > 4 and self.map.map_data[self.row - 1][self.col] == 0:
                        self.row = self.row - 1
                        self.rect.x = cen_x + 32
                        self.rect.y = cen_y - 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    else:
                        self.rect.x = cen_x
                        self.rect.y = cen_y
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                elif self.orn == "S":
                    if (sub_x >= 24 or sub_x < 12) and self.map.map_data[self.row + 1][self.col] == 0:
                        self.row = self.row + 1
                        self.rect.x = cen_x - 32
                        self.rect.y = cen_y + 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    else:
                        self.rect.x = cen_x
                        self.rect.y = cen_y
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y

                self.orn = "E"
            elif self.orn == "W":
                self.orn = "E"
                if (sub_x < 12 or sub_x >= 24) and self.map.map_data[self.row][self.col - 1] == 0:
                    self.col = self.col - 1
                    self.rect.x = cen_x - 32
                    self.rect.y = cen_y - 16
                    self.currentx = self.rect.x
                    self.currenty = self.rect.y
            else:
                self.orn = "E"
                if self.map.map_data[self.row][self.col + 1] == 0:
                    xdif = abs(self.rect.x - self.currentx)
                    if xdif == 32:
                        self.col = self.col + 1
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                    self.speedx += 2 * math.cos(math.radians(30))
                    self.speedy += 2 * math.sin(math.radians(30))
                else:
                    self.speedy = 0
                    self.speedx = 0

        elif keystate[pygame.K_UP]:
                if self.state == False:
                    self.image = pygame.image.load('assets/images/forklift_up_right.png').convert_alpha()
                elif self.state == True:
                    self.image = pygame.image.load('assets/images/forklift_up_box.png').convert_alpha()
                sub_x = self.rect.x % 32
                cen_x, cen_y = self.get_pos(self.col, self.row)
                if self.orn == "W" or self.orn == "E":
                    if self.orn == "E":
                        if (4 < sub_x <= 24) and self.map.map_data[self.row][self.col + 1] == 0:
                            self.col = self.col + 1
                            self.rect.x = cen_x + 32
                            self.rect.y = cen_y + 16
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        else:
                            self.rect.x = cen_x
                            self.rect.y = cen_y
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                    elif self.orn == "W":
                        if (sub_x < 12 or sub_x > 24) and self.map.map_data[self.row][self.col - 1] == 0:
                            self.col = self.col - 1
                            self.rect.x = cen_x - 32
                            self.rect.y = cen_y - 16
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        else:
                            self.rect.x = cen_x
                            self.rect.y = cen_y
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                    self.orn = "N"
                elif self.orn == "S":
                    self.orn = "N"
                    if (sub_x >= 24 or sub_x < 12) and self.map.map_data[self.row + 1][self.col] == 0:
                        self.row = self.row + 1
                        self.rect.x = cen_x - 32
                        self.rect.y = cen_y + 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                else:
                    self.orn = "N"
                    if self.map.map_data[self.row-1][self.col] == 0:
                        ydif = abs(self.rect.y - self.currenty)
                        if ydif == 16:
                            self.row = self.row - 1
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        self.speedx += 2 * math.cos(math.radians(30))
                        self.speedy -= 2 * math.sin(math.radians(30))
                    else:
                        self.speedy = 0
                        self.speedx = 0

        elif keystate[pygame.K_DOWN]:
                if self.state == False:
                    self.image = pygame.image.load('assets/images/forklift_down_left.png').convert_alpha()
                elif self.state == True:
                    self.image = pygame.image.load('assets/images/forklift_down_box.png').convert_alpha()
                cen_x, cen_y = self.get_pos(self.col, self.row)
                sub_x = self.rect.x % 32
                if self.orn == "E" or self.orn == "W":
                    if self.orn == "E":
                        if (4 < sub_x <= 24) and self.map.map_data[self.row][self.col + 1] == 0:
                            self.col = self.col + 1
                            self.rect.x = cen_x + 32
                            self.rect.y = cen_y + 16
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        else:
                            self.rect.x = cen_x
                            self.rect.y = cen_y
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                    elif self.orn == "W":
                        if (sub_x < 12 or sub_x > 24) and self.map.map_data[self.row][self.col - 1] == 0:
                            self.col = self.col - 1
                            self.rect.x = cen_x - 32
                            self.rect.y = cen_y - 16
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        else:
                            self.rect.x = cen_x
                            self.rect.y = cen_y
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                    self.orn = "S"
                elif self.orn == "N":
                    self.orn = "S"
                    if 24 >= sub_x > 4 and self.map.map_data[self.row - 1][self.col] == 0:
                        self.row = self.row - 1
                        self.rect.x = cen_x + 32
                        self.rect.y = cen_y - 16
                        self.currentx = self.rect.x
                        self.currenty = self.rect.y
                else:
                    self.orn = "S"
                    if self.map.map_data[self.row+1][self.col] == 0:
                        ydif = abs(self.rect.y - self.currenty)
                        if ydif == 16:
                            self.row = self.row + 1
                            self.currentx = self.rect.x
                            self.currenty = self.rect.y
                        self.speedx -= 2 * math.cos(math.radians(30))
                        self.speedy += 2 * math.sin(math.radians(30))
                    else:
                        self.speedy = 0
                        self.speedx = 0

        self.rect.x += round(self.speedx)
        self.rect.y += round(self.speedy)

        if self.map.map_data[self.row+1][self.col] == 2 and self.orn == "S":
            if keystate[pygame.K_e] and self.state == False:
                self.map.map_data[self.row + 1][self.col] = 0
                self.tiles.empty()
                self.tiles = self.map.render_to_iso()
                self.state = True
                self.image = pygame.image.load('assets/images/forklift_down_box.png').convert_alpha()

        if self.map.map_data[self.row-1][self.col] == 2 and self.orn == "N":
            if keystate[pygame.K_e] and self.state == False:
                self.map.map_data[self.row - 1][self.col] = 0
                self.tiles.empty()
                self.tiles = self.map.render_to_iso()
                self.state = True
                self.image = pygame.image.load('assets/images/forklift_up_box.png').convert_alpha()

        if self.map.map_data[self.row][self.col - 1] == 2 and self.orn == "W":
            if keystate[pygame.K_e] and self.state == False:
                self.map.map_data[self.row][self.col - 1] = 0
                self.tiles.empty()
                self.tiles = self.map.render_to_iso()
                self.state = True
                self.image = pygame.image.load('assets/images/forklift_left_box.png').convert_alpha()

        if self.map.map_data[self.row][self.col + 1] == 2 and self.orn == "E":
            if keystate[pygame.K_e] and self.state == False:
                self.map.map_data[self.row][self.col + 1] = 0
                self.tiles.empty()
                self.tiles = self.map.render_to_iso()
                self.state = True
                self.image = pygame.image.load('assets/images/forklift_right_box.png').convert_alpha()

        if self.map.map_data[self.row + 1][self.col] == 3 and self.orn == "S":
            if keystate[pygame.K_e] and self.state == True:
                self.state = False
                self.map.elements = self.map.elements - 1
                self.image = pygame.image.load('assets/images/forklift_down_left.png').convert_alpha()

        if self.map.map_data[self.row - 1][self.col] == 3 and self.orn == "N":
            if keystate[pygame.K_e] and self.state == True:
                self.state = False
                self.map.elements = self.map.elements - 1
                self.image = pygame.image.load('assets/images/forklift_up_right.png').convert_alpha()

        if self.map.map_data[self.row][self.col - 1] == 3 and self.orn == "W":
            if keystate[pygame.K_e] and self.state == True:
                self.state = False
                self.map.elements = self.map.elements - 1
                self.image = pygame.image.load('assets/images/forklift_up_left.png').convert_alpha()

        if self.map.map_data[self.row][self.col + 1] == 3 and self.orn == "E":
            if keystate[pygame.K_e] and self.state == True:
                self.state = False
                self.map.elements = self.map.elements - 1
                self.image = pygame.image.load('assets/images/forklift_down_right.png').convert_alpha()


    def get_x(self):
        return self.rect.x * math.cos(math.radians(30))

    def get_y(self):
        return self.rect.y * math.sin(math.radians(30))

    TILEWIDTH = 64
    TILEHEIGHT = 64
    TILEHEIGHT_HALF = TILEHEIGHT / 2
    TILEWIDTH_HALF = TILEWIDTH / 2

    def get_pos(self, row, col):
        cart_x = row * self.TILEWIDTH_HALF
        cart_y = col * self.TILEHEIGHT_HALF
        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y) / 2
        centered_x = self.disp_surf.get_rect().centerx + iso_x - self.TILEWIDTH_HALF
        centered_y = self.disp_surf.get_rect().centery / 2 + iso_y
        return centered_x, centered_y

    def set_map(self, map):
        self.map = map

