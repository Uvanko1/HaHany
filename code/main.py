import pygame
import pygame_menu

from settings import *
from map import Map
from game_data import mangolia_1, get_dialog
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
    shift = 2
    frame = 0
    map_zoom = 5
    zoom_count = 0
    khan_view = 'top'
    flag_dialog = False
    dialog_part = 0
    while 1:
        menu.close()
        key = pygame.key.get_pressed()
        cam_x = 0
        cam_y = 0
        pos = map_sprite.get_rect_pos()
        dialog_pos = get_dialog(pos)
        if dialog_pos is not None:
            flag_hint = True
        else:
            flag_hint = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    pos_x, pos_y = map_sprite.get_rect_pos()
                    save_position(pos_x, pos_y)
                elif event.key == pygame.K_e:
                    if dialog_pos is not None:
                        flag_dialog = True
                elif event.key == pygame.K_ESCAPE:
                    flag_dialog = False
                    dialog_part = 0
            # увеличение изображения
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if zoom_count < 20:
                    zoom_count += 1
                    res = [res[0] - map_zoom, res[1] - map_zoom]
                    screen = pygame.transform.scale(window, res)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if zoom_count > 0:
                    zoom_count -= 1
                    res = [res[0] + map_zoom, res[1] + map_zoom]
                    screen = pygame.transform.scale(window, res)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if flag_dialog:
                    print(dialog_part)
                    dialog_part += 1

        khan_view = 'stop_' + khan_view
        if not flag_dialog:
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
        generate_map.run(screen, window,
                         cam_x, cam_y,
                         khan_view,
                         flag_dialog, dialog_pos, dialog_part,
                         flag_hint)
        pygame.display.update()
        window.blit(pygame.transform.scale(screen, size), (0, 0))
        clock.tick(120)
        frame += 1
        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))


menu.add.button('Играть', start_the_game)
menu.mainloop(window)
