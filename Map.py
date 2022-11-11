import pygame
import random
import Tile


class Map(pygame.sprite.Sprite):

    TILEWIDTH = 64
    TILEHEIGHT = 64
    TILEHEIGHT_HALF = TILEHEIGHT / 2
    TILEWIDTH_HALF = TILEWIDTH / 2

    def __init__(self, DISPLAYSURF):
        pygame.sprite.Sprite.__init__(self)
        self.tiles = pygame.sprite.Group()
        self.map_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
        self.rows = self.map_data.__len__()
        self.cols = self.map_data[0].__len__()
        self.box_list = []
        self.exit = ()
        self.start = ()
        self.disp_surf = DISPLAYSURF
        self.elements = 4
        self.add_elements(self.elements)
        self.clean_map()
        self.render_to_iso()
        self.player_pos = self.get_pos(self.start[1], self.start[0])

    def render_to_iso(self):
        wall = pygame.image.load('assets/images/wall.png').convert_alpha()
        grass = pygame.image.load('assets/images/grass.png').convert_alpha()
        box = pygame.image.load('assets/images/box.png').convert_alpha()

        if self.exit[0] == 0:
            truck = pygame.image.load('assets/images/truck_up.png').convert_alpha()
        elif self.exit[0] == len(self.map_data)-1:
            truck = pygame.image.load('assets/images/truck_down.png').convert_alpha()
        elif self.exit[1] == 0:
            truck = pygame.image.load('assets/images/truck_left.png').convert_alpha()
        elif self.exit[1] == len(self.map_data[0])-1:
            truck = pygame.image.load('assets/images/truck_right.png').convert_alpha()

        for col_nb, col in enumerate(self.map_data):
            for row_nb, tile in enumerate(col):
                if tile == 1:
                    t = self.new_tile(row_nb, col_nb, wall, "obs")
                    self.tiles.add(t)
                elif tile == 2:
                    t = self.new_tile(row_nb, col_nb, box, "box")
                    self.tiles.add(t)
                elif tile == 3:
                    t = self.new_tile(row_nb, col_nb, truck, "goal")
                    self.tiles.add(t)
                else:
                    t = self.new_tile(row_nb, col_nb, grass, "path")
                    self.tiles.add(t)

        return self.tiles

    def new_tile(self, row, col, imag, type):
        x, y = self.get_pos(row, col)
        t = Tile.Tile(row, col, x, y, imag, type, self.disp_surf)
        self.tiles.add(t)
        return t

    def draw_tile(self):
        self.tiles.draw(self.disp_surf)

    def get_pos(self, row, col):
        cart_x = row * self.TILEWIDTH_HALF
        cart_y = col * self.TILEHEIGHT_HALF
        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y) / 2
        centered_x = self.disp_surf.get_rect().centerx + iso_x - self.TILEWIDTH_HALF
        centered_y = self.disp_surf.get_rect().centery / 2 + iso_y
        return centered_x, centered_y

    def add_elements(self, box_number):
        exit_start_coord = self.add_exit()
        self.exit = exit_start_coord[0], exit_start_coord[1], exit_start_coord[2]
        self.start = exit_start_coord[3], exit_start_coord[4]
        element_counter = 0
        while element_counter < box_number:
            randx = random.randrange(1, len(self.map_data) - 1)
            randy = random.randrange(1, len(self.map_data[0]) - 1)
            if self.map_data[randx][randy] == 0 and random.randrange(100) < 7 and randx != self.start[0] and randy != self.start[1]:
                self.map_data[randx][randy] = 2
                element_counter += 1
                self.box_list.append((randx, randy))

        for i in range(len(self.map_data)):
            for count_j, j in enumerate(self.map_data[i]):
                if j == 0 and random.randrange(100) < 48:
                    self.map_data[i][count_j] = 1

    def clean_map(self):
        no_path = []
        for i in self.box_list:
            vis = [[False for x in range (len(self.map_data[0]))]
                      for y in range (len(self.map_data))]
            res = self.check_path(vis, i[0], i[1])
            if not res:
                no_path.append(i)

        for i in no_path:
            if len(no_path) == len(self.box_list):
                self.make_path(i[0], i[1])
                no_path = no_path[1:]
            else:
                vis = [[False for x in range(len(self.map_data[0]))]
                       for y in range(len(self.map_data))]
                res = self.check_path(vis, i[0], i[1])
                if not res:
                    self.make_path(i[0], i[1])

    def is_safe(self, i, j):
        if (i == 0 or j == 0 or i == len(self.map_data)-1 or j == len(self.map_data[0])-1) and self.map_data[i][j] == 3:
            return True
        elif 0 < i < len(self.map_data)-1 and 0 < j < len(self.map_data[0])-1:
            return True
        return False

    def check_path(self, vis, i, j):

        if self.is_safe(i, j) and self.map_data[i][j] != 1 and not vis[i][j]:
            vis[i][j] = True

            if self.map_data[i][j] == 3:
                return True

            up = self.check_path(vis, i-1, j)
            if up:
                return True

            left = self.check_path(vis, i, j-1)
            if left:
                return True

            down = self.check_path(vis, i+1, j)
            if down:
                return True

            right = self.check_path(vis, i, j+1)
            if right:
                return True
        return False

    def add_exit(self):
        randx = random.randrange(1, len(self.map_data)-1)
        randy = random.randrange(1, len(self.map_data[0])-1)
        rand_option = random.randrange(4)
        lex = len(self.map_data)-1
        ley = len(self.map_data[0])-1
        if rand_option == 0:        #gornja strana
            self.map_data[0][randy] = 3
            return 0, randy, "up", 1, randy
        elif rand_option == 1:      #leva strana
            self.map_data[randx][0] = 3
            return randx, 0, "left", randx, 1
        elif rand_option == 2:      #desna strana
            self.map_data[randx][ley] = 3
            return randx, ley, "right", randx, ley-1
        elif rand_option == 3:      #donja strana
            self.map_data[lex][randy] = 3
            return lex, randy, "down", lex-1, randy,

    def make_path(self, i, j):

        if self.is_safe(i, j):

            if i == self.exit[0] and j == self.exit[1]:
                return True

            if self.map_data[i][j] == 1:
                self.map_data[i][j] = 0

            if i != self.exit[0]:
                if i > self.exit[0]:
                    ypos = self.make_path(i-1, j)
                    if ypos:
                        return True
                elif i < self.exit[0]:
                    ypos = self.make_path(i+1, j)
                    if ypos:
                        return True

            if j != self.exit[1]:
                if j > self.exit[1]:
                    xpos = self.make_path(i, j-1)
                    if xpos:
                        return True
                elif j < self.exit[1]:
                    xpos = self.make_path(i, j+1)
                    if xpos:
                        return True

            return False

    def get_start_coord(self):
        return self.start