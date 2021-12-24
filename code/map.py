import pygame
from support import import_csv_layout
from settings import tile_size
from tiles import Tile


class Map:
    def __init__(self, map_data, surface):
        self.display_surface = surface
        self.world_shift = 0
        green_layout = import_csv_layout(map_data['green'])
        self.yellow_sprites = self.create_tile_group(green_layout, 'green')
        print(green_layout)

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    if type == 'green':
                        yellow_tile_list = import_cut_graphics('../graphics/mongolia_tiles/buch-outdoor.png')
                        sprite = Tile(tile_size, x, y)
                        sprite_group.add(sprite)

        return sprite_group

    def run(self):
        self.yellow_sprites.draw(self.display_surface)
        self.yellow_sprites.update(-4)
