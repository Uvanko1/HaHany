import pygame
from csv import reader
from settings import tile_size


def import_csv_layout(path):
    yellow_map = []
    with open(path) as map:
        map = reader(map, delimiter=',')
        for row in map:
            yellow_map.append(list(row))
        return yellow_map


def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(surface)