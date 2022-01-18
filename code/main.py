import pygame
import pygame_menu

from settings import *
from map import Map
from game_data import mangolia_1
from saves import save_position
from map_static import MapSprite
from sounds import horse, all

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
menu = pygame_menu.Menu('Татаро-монголы', screen_width, screen_height, theme=pygame_menu.themes.THEME_GREEN)
menu.add.image('../graphics/menu/menu.png')
menu_exit = pygame_menu.Menu('Татаро-монголы', screen_width // 2, screen_height // 2,
                             theme=pygame_menu.themes.THEME_GREEN)
map_sprite = MapSprite()


def start_the_game():
    menu.close()
    all()
    generate_map = Map(mangolia_1)
    size = [screen_width, screen_height]
    res = [screen_width // 4, screen_height // 4]
    res_zoom = res
    screen = pygame.transform.scale(window, res)
    interface = pygame.transform.scale(window, res)
    clock = pygame.time.Clock()
    shift = 2
    frame = 0
    map_zoom_x = 16
    map_zoom_y = 9
    zoom_count = 0
    khan_view = 'top'
    flag_dialog = False
    dialog_part = 0

    while 1:
        play_music = False
        menu.close()
        cam_x = 0
        cam_y = 0
        khan_x = 0
        khan_y = 0
        cam_zoom_x = 0
        cam_zoom_y = 0
        key = pygame.key.get_pressed()
        pos = map_sprite.get_rect_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    pos_x, pos_y = map_sprite.get_rect_pos()
                    save_position(pos_x, pos_y)
                elif event.key == pygame.K_e:
                    flag_dialog = True
                elif event.key == pygame.K_ESCAPE and flag_dialog:
                    flag_dialog = False
                elif event.key == pygame.K_ESCAPE:
                    menu_exit.mainloop(window)
                # map demo
                elif event.key == pygame.K_m:
                    image = pygame.image.load('../maps/map_data/map.png')
                    window.blit(image, (0, 0))
            # увеличение изображения
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if zoom_count < 10:
                    zoom_count += 1
                    res_zoom = [res_zoom[0] - map_zoom_x, res_zoom[1] - map_zoom_y]
                    cam_zoom_x -= map_zoom_x // 2
                    cam_zoom_y -= map_zoom_y // 2
                    khan_x -= map_zoom_x // 2
                    khan_y -= map_zoom_y // 2
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if zoom_count > 0:
                    zoom_count -= 1
                    res_zoom = [res_zoom[0] + map_zoom_x, res_zoom[1] + map_zoom_y]
                    cam_zoom_x += map_zoom_x // 2
                    cam_zoom_y += map_zoom_y // 2
                    khan_x += map_zoom_x // 2
                    khan_y += map_zoom_y // 2
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if flag_dialog:
                    dialog_part += 1
        khan_view = 'stop_' + khan_view
        if not flag_dialog:
            if key[pygame.K_a]:
                cam_x += shift
                khan_view = 'left'
                play_music = True
            if key[pygame.K_d]:
                cam_x -= shift
                khan_view = 'right'
                play_music = True
            if key[pygame.K_w]:
                cam_y += shift
                khan_view = 'bottom'
                play_music = True
            if key[pygame.K_s]:
                cam_y -= shift
                khan_view = 'top'
                play_music = True
            print(flag_dialog)
            horse(play_music)

        screen.fill('grey')
        generate_map.run(screen, interface,
                         cam_x, cam_y, cam_zoom_x, cam_zoom_y,
                         khan_view, khan_x, khan_y,
                         flag_dialog, dialog_part)
        pygame.display.update()
        window.blit(pygame.transform.scale(interface, size), (0, 0))
        interface.blit(
            pygame.transform.scale(screen, res),
            (0, 0))
        screen = pygame.transform.scale(window, res_zoom)
        clock.tick(120)
        frame += 1
        if frame % 100 == 0:
            pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))


def quit():
    exit()


def close_menu():
    menu_exit.close()
    start_the_game()


menu.add.button('Играть', start_the_game)
menu_exit.add.label('Вы уверены что хотите выйти?')
menu_exit.add.button('Да', quit)
menu_exit.add.button('Нет', close_menu)
menu.mainloop(window)
