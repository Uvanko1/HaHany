import pygame
import pygame_menu

from settings import *
from map import Map
from game_data import mangolia_1

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
menu = pygame_menu.Menu('Татаро-монголы', screen_width, screen_height, theme=pygame_menu.themes.THEME_GREEN)
menu.add.image('../graphics/menu/menu.png')
dialog = pygame.image.load('../graphics/Диалоги/ramka.png')


class Dialog:
    def __init__(self, name):
        self.name = name

    def draw_window(self):
        window.blit(dialog, (0, 500), pygame.Rect(0, 0, screen_width, screen_height * (2 / 3)))

    def draw_text(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Khan: Hello, people!", True, (255, 255, 255))
        window.blit(text, (70, 570))


def start_the_game():
    menu.close()
    generate_map = Map(mangolia_1)
    size = [screen_width, screen_height]
    res = [screen_width // 1.5, screen_height // 1.5]
    screen = pygame.transform.scale(window, res)
    clock = pygame.time.Clock()
    shift = 10
    frame = 0
    map_zoom = 1
    zoom_count = 0
    khan_view = 'top'
    dialogs = Dialog('Loshok')
    flag = False
    count = 0
    while 1:
        menu.close()
        key = pygame.key.get_pressed()
        cam_x = 0
        cam_y = 0
        if key[pygame.K_ESCAPE] and count == 2:
            flag = False
            count = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                res = [res[0] - map_zoom, res[1] - map_zoom]
                screen = pygame.transform.scale(window, res)
            if not flag:
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
                khan_view = 'stop' + khan_view
                if key[pygame.K_e] and count != 1:
                    dialogs.draw_window()
                    dialogs.draw_text()
                    flag = True
                    count = 2
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
        if not flag:
            screen.fill('grey')
            generate_map.run(screen, cam_x, cam_y, khan_view)
            pygame.display.update()
            window.blit(pygame.transform.scale(screen, size), (0, 0))
            clock.tick(480)
            frame += 1
            if frame % 100 == 0:
                pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))


menu.add.button('Играть', start_the_game)
menu.mainloop(window)
