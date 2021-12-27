import pygame
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile, StaticTile
import numba


def create_tile_group(layout, type):
    sprite_group = pygame.sprite.Group()
    for row_index, row in enumerate(layout):
        for col_index, val in enumerate(row):
            if val != '-1':
                x = col_index * tile_size
                y = row_index * tile_size
                if type == 'test':
                    test_tile_list = import_cut_graphic('../graphics/mongolia_tiles/test2.png')
                    tile_surface = test_tile_list[int(val)]
                    sprite = StaticTile(tile_size, x, y, tile_surface)
                    sprite_group.add(sprite)

    return sprite_group


class Map:
    def __init__(self, map_data, surface):
        self.display_surface = surface
        self.world_shift = -1
        test_layout = import_csv_layout(map_data['test'])
        self.test_sprites = create_tile_group(test_layout, 'test')

    def run(self):
        self.test_sprites.draw(self.display_surface)
        self.test_sprites.update(self.world_shift)
