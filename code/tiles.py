import random

import pygame

from support import import_folder
from saves import get_save_position
from map_static import MapSprite
from khan import Khan

map_static = MapSprite()

list_spawn_pos = get_save_position()
khan = Khan()

stop_flag = None


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x += list_spawn_pos[0]
        self.rect.y += list_spawn_pos[1]


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.rect.y += cam_y


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.speed = speed
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.stop_flag = None
        mask_surf = pygame.Surface((14, 26))
        self.mask = pygame.mask.from_surface(mask_surf)

    def animate(self):
        self.frames_index += self.speed
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self, cam_x, cam_y):
        self.animate()
        self.rect.x += cam_x
        self.rect.y += cam_y


    def get_mask(self):
        if pygame.sprite.collide_mask(self, khan):
            pass


class CharacterTile(Tile):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.speed = speed
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.stop_flag = None

    def animate(self):
        self.frames_index += self.speed
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self, cam_x, cam_y):
        self.animate()
        if pygame.sprite.collide_mask(self, khan):
            pass
        self.rect.x += cam_x
        self.rect.y += cam_y