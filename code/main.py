import sys

import pygame
from settings import *
from generate_map import MapStatic, map_sprite
from map import Map
from game_data import mangolia_1

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
map = Map(mangolia_1, screen)
map_static = MapStatic()
shift = 10
frame = 0

while 1:
    key = pygame.key.get_pressed()
    cam_x = 0
    cam_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if key[pygame.K_a]:
            cam_x += shift
        if key[pygame.K_d]:
            cam_x -= shift
        if key[pygame.K_w]:
            cam_y += shift
        if key[pygame.K_s]:
            cam_y -= shift
    screen.fill('grey')
    # map_static.render(screen)
    map_sprite.update(cam_x, cam_y)
    map_sprite.draw(screen)
    map.run()

    pygame.display.update()
    clock.tick(60)
    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
