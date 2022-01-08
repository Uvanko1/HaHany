import pygame

from stats import Stats, stats_sprite
from dialog import ramka_sprite, Dialog
from map_static import MapSprite, map_sprite
from support import import_csv_layout
from settings import tile_size
from tiles import AnimatedTile
from khan import Khan, khan_sprite

Khan()
dialog = Dialog()
stats = Stats()


def create_tile_group(layout, type):
    sprite_group = pygame.sprite.Group()
    for row_index, row in enumerate(layout):
        for col_index, val in enumerate(row):
            if val != '-1':
                x = col_index * tile_size
                y = row_index * tile_size
                if type == 'animation_forest':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/les/Tree')
                    sprite_group.add(sprite)
    return sprite_group


class Map:
    def __init__(self, map_data):
        test_layout = import_csv_layout(map_data['лошади'])
        self.test_sprites = create_tile_group(test_layout, 'лошади')
        forest_layout = import_csv_layout(map_data['animation_forest'])
        self.forest_sprites = create_tile_group(forest_layout, 'animation_forest')
        self.map_sprite = map_sprite
        self.khan_sprite = khan_sprite
        self.ramka_sprite = ramka_sprite
        self.stats_sprite = stats_sprite

    def run(self, surface, cam_x, cam_y, khan_view, flag):
        self.map_sprite.draw(surface)
        self.map_sprite.update(cam_x, cam_y)
        self.khan_sprite.draw(surface)
        self.khan_sprite.update(khan_view)
        self.test_sprites.draw(surface)
        self.test_sprites.update(cam_x, cam_y)
        self.forest_sprites.update(cam_x, cam_y)
        self.forest_sprites.draw(surface)
        stats.draw_stats_text(surface, 0, 4, '4/20')
        stats.draw_stats_text(surface, 60, 4, '5/20')
        stats.draw_stats_text(surface, 120, 4, '20/20')
        self.stats_sprite.draw(surface)
        if flag:
            self.ramka_sprite.draw(surface)
            dialog.draw_text(surface)
