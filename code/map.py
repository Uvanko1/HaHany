import pygame

from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile, HorseTile


def create_tile_group(layout, type):
    sprite_group = pygame.sprite.Group()
    for row_index, row in enumerate(layout):
        for col_index, val in enumerate(row):
            if val != '-1':
                x = col_index * tile_size
                y = row_index * tile_size
                if type == 'лошади':
                    test_tile_list = import_cut_graphic('../graphics/лошади/horse.png')
                    tile_surface = test_tile_list[int(val)]
                    sprite = HorseTile(tile_size, x, y, tile_surface)
                    sprite_group.add(sprite)
    return sprite_group


class Map:
    def __init__(self, map_data):
        self.world_shift = 0
        test_layout = import_csv_layout(map_data['лошади'])
        self.test_sprites = create_tile_group(test_layout, 'лошади')

    def run(self, surface):
        self.test_sprites.draw(surface)
        self.test_sprites.update(self.world_shift)
