import pygame

from support import import_folder
from saves import get_save_position
from khan import Khan

lst = get_save_position()
khan = Khan()


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x += lst[0]
        self.rect.y += lst[1]


class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

    def update(self, cam_x, cam_y):
        if not pygame.sprite.collide_mask(self, khan):
            stop()
        self.rect.x += cam_x
        self.rect.y += cam_y


class AnimatedTile(Tile):
    def __init__(self, size, x, y, path, speed):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.speed = speed
        self.frames_index = 0
        self.image = self.frames[self.frames_index]

    def animate(self):
        self.frames_index += self.speed
        if pygame.sprite.collide_mask(self, khan):
            stop()
            self.rect = self.rect.move(0, 1)
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self, cam_x, cam_y):
        self.animate()
        self.rect.x += cam_x
        self.rect.y += cam_y


def stop():
    print('ok')
