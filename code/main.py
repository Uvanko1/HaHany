import pygame
from settings import *
from generate_map import MapStatic, map_sprite
from map import Map
from game_data import mangolia_1

size = [screen_width, screen_height]
res = [screen_width // 1.5, screen_height // 1.5]

pygame.init()
window = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.transform.scale(window, res)
clock = pygame.time.Clock()
map = Map(mangolia_1, screen)
map_static = MapStatic()
shift = 10
frame = 0
map_zoom = 1
zoom_count = 0

while 1:
    key = pygame.key.get_pressed()
    cam_x = 0
    cam_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            res = [res[0] - map_zoom, res[1] - map_zoom]
            screen = pygame.transform.scale(window, res)
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
    if key[pygame.K_a]:
        cam_x += shift
    if key[pygame.K_d]:
        cam_x -= shift
    if key[pygame.K_w]:
        cam_y += shift
    if key[pygame.K_s]:
        cam_y -= shift
    screen.fill('grey')
    map_sprite.update(cam_x, cam_y)
    map_sprite.draw(screen)
    map.run()
    pygame.display.update()
    window.blit(pygame.transform.scale(screen, size), (0, 0))
    clock.tick(60)
    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
