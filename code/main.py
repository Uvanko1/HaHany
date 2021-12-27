import sys

import pygame
from settings import *
from map import Map
from game_data import mangolia_1

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
map = Map(mangolia_1, screen)
frame = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    map.run()

    pygame.display.update()
    clock.tick(60)
    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))

