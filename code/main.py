import pygame
import pygame_menu

from dialog import Dialog
from settings import *
from map import Map
from game_data import mangolia_1
from saves import save_position
from map_static import MapSprite

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
menu = pygame_menu.Menu('Татаро-монголы', screen_width, screen_height, theme=pygame_menu.themes.THEME_GREEN)
menu.add.image('../graphics/menu/menu.png')
map_sprite = MapSprite()


def start_the_game():
    menu.close()
    generate_map = Map(mangolia_1)
    size = [screen_width, screen_height]
    res = [screen_width // 2, screen_height // 2]
    screen = pygame.transform.scale(window, res)
    clock = pygame.time.Clock()
    shift = 15
    frame = 0
    map_zoom = 1
    zoom_count = 0
    khan_view = 'top'
    flag = False
    while 1:
        menu.close()
        key = pygame.key.get_pressed()
        cam_x = 0
        cam_y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    pos_x, pos_y = map_sprite.get_rect_pos()
                    save_position(pos_x, pos_y)
                elif event.key == pygame.K_e:
                    flag = True
                elif event.key == pygame.K_ESCAPE:
                    flag = False
        if key[pygame.K_1]:
            if zoom_count < 100:
                zoom_count += 1
                print(zoom_count)
                res = [res[0] - map_zoom, res[1] - map_zoom]
                screen = pygame.transform.scale(window, res)
        if key[pygame.K_2]:
            if zoom_count > 0:
                zoom_count -= 1
                print(zoom_count)
                res = [res[0] + map_zoom, res[1] + map_zoom]
                screen = pygame.transform.scale(window, res)
        khan_view = 'stop_' + khan_view
        if key[pygame.K_a]:
            cam_x += shift
            khan_view = 'left'
        if key[pygame.K_d]:
            cam_x -= shift
            khan_view = 'right'
        if key[pygame.K_w]:
            cam_y += shift
            khan_view = 'bottom'
        if key[pygame.K_s]:
            cam_y -= shift
            khan_view = 'top'
        screen.fill('grey')
        generate_map.run(screen, cam_x, cam_y, khan_view, flag)
        pygame.display.update()
        window.blit(pygame.transform.scale(screen, size), (0, 0))
        clock.tick(120)
        frame += 1
        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))


menu.add.button('Играть', start_the_game)
menu.mainloop(window)
