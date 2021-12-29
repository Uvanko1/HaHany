import pygame
from csv import reader
from settings import *


def import_csv_layout(path):
    test_map = []
    with open(path) as map:
        map = reader(map, delimiter=',')
        for row in map:
            test_map.append(list(row))
        return test_map


def import_cut_map_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    chunk_x = int(surface.get_size()[0] // screen_width)
    chunk_y = int(surface.get_size()[1] // screen_height)
    cut_map = []
    for row in range(chunk_y):
        for col in range(chunk_x):
            x = col * screen_width
            y = row * screen_height
            new_surf = pygame.Surface((screen_width, screen_height))
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, screen_width, screen_height))
            cut_map.append(new_surf)
    return cut_map


def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    # Make sure that the color depth (32) stays explicitly set else this will not work.
    tile_num_x = int(surface.get_size()[0] / tile_size) - 1
    tile_num_y = int(surface.get_size()[1] / tile_size) - 1
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surf)
    return cut_tiles
