import pygame
import sys
import Map
import Player
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200, 800), pygame.DOUBLEBUF)
pygame.display.set_caption("Ide sG4")
FPSCLOCK = pygame.time.Clock()

wall = pygame.image.load('assets/images/wall.png').convert_alpha()
wall_trans = pygame.image.load('assets/images/wall.png').convert_alpha()
wall_trans.set_alpha(64)


def set_transparent(tbt_tile):
    global wall_trans
    if tbt_tile.type == "obs":
        tbt_tile.image = wall_trans


def set_filled(tbf_tile):
    global wall
    if tbf_tile.type == "obs":
        tbf_tile.image = wall


def render_map(tiles, player, map_group_behind, map_group_front):
    map_group_behind.empty()
    map_group_front.empty()
    for tile in tiles:
        tile_x = tile.get_x()
        tile_y = tile.get_y()
        if tile.type == "path":
            player_x = player.get_x() + 16
            player_y = player.get_y() + 16
        else:
            player_x = player.get_x()
            player_y = player.get_y()
        if tile_y <= player_y:
            map_group_behind.add(tile)
        else:
            if (abs(tile_x - player_x)) <= 20 and (abs(tile_y - player_y)) <= 20:
                set_transparent(tile)
            else:
                set_filled(tile)
            map_group_front.add(tile)


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font_name = pygame.font.match_font('InsaneHours2')


def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def get_map():
    game_map = Map.Map(DISPLAYSURF)
    return game_map


def get_player(game_map, tiles):
    player = Player.Player(DISPLAYSURF, game_map, tiles)
    return player


def newgame():
    DISPLAYSURF.fill((0, 0, 0))
    game_map = get_map()
    tiles = game_map.render_to_iso()
    start_time = time.time()
    player = get_player(game_map, tiles)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    map_group_behind = pygame.sprite.Group()
    map_group_front = pygame.sprite.Group()
    st = game(game_map, tiles, player, all_sprites, map_group_behind, map_group_front, start_time)
    tiles.empty()
    all_sprites.empty()
    map_group_front.empty()
    map_group_behind.empty()
    gameover(st)

def gameover(st):
    while True:
        if st == False:
            draw_text(DISPLAYSURF, 'GAME OVER', 60, 600, 400, RED)
            draw_text(DISPLAYSURF, 'PRESS R TO RESTART OR ESC TO QUIT', 40, 600, 600, RED)
        if st == True:
            draw_text(DISPLAYSURF, 'YOU WIN', 60, 600, 400, GREEN)
            draw_text(DISPLAYSURF, 'PRESS R TO RESTART OR ESC TO QUIT', 40, 600, 600, GREEN)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    newgame()
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


def game(game_map, tiles, player, all_sprites, map_group_behind, map_group_front, start_time):
    time_string = "1:00"
    while True:
        draw_text(DISPLAYSURF, time_string, 60, 600, 100, WHITE)
        passed_time = time.time() - start_time
        time_value = round(60 - passed_time)
        if time_value < 60:
            time_string = "0:" + str(round(time_value))
        if time_value < 10:
            time_string = "0:0" + str(round(time_value))
        if passed_time >= 60:
            return False
        if game_map.elements == 0:
            return True
        render_map(tiles, player, map_group_behind, map_group_front)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        all_sprites.update(DISPLAYSURF)
        pygame.display.flip()
        DISPLAYSURF.fill((0, 0, 0))
        map_group_behind.draw(DISPLAYSURF)
        all_sprites.draw(DISPLAYSURF)
        map_group_front.draw(DISPLAYSURF)
        FPSCLOCK.tick(30)


newgame()




