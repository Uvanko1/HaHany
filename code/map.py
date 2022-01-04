import pygame

from map_static import MapSprite, map_sprite
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import Tile, HorseTile, ForestTile

MapSprite()


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
                if type == 'animation_forest':
                    forest_tile_list = import_cut_graphic('../graphics/les/Tree/tree96x96transparentanimated1.png')
                    tile_surface = forest_tile_list[int(val)]
                    sprite = ForestTile(tile_size, x, y, tile_surface)
                    sprite_group.add(sprite)
    return sprite_group


class Map:
    def __init__(self, map_data):
        test_layout = import_csv_layout(map_data['лошади'])
        self.test_sprites = create_tile_group(test_layout, 'лошади')
        # forest_layout = import_csv_layout(map_data['animation_forest'])
        # self.forest_sprites = create_tile_group(forest_layout, 'animation_forest')
        self.map_sprite = map_sprite

    def run(self, surface, cam_x, cam_y):
        self.map_sprite.draw(surface)
        self.map_sprite.update(cam_x, cam_y)
        self.test_sprites.draw(surface)
        self.test_sprites.update(cam_x, cam_y)
        # self.forest_sprites.draw(surface)
        # self.forest_sprites.update(cam_x, cam_y)
