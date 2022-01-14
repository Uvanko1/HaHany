import pygame
from tiles import list_spawn_pos
icons_sprite = pygame.sprite.Group()


class Hints(pygame.sprite.Sprite):
    image = pygame.image.load('../graphics/icons/icon_e.png')

    def __init__(self, pos):
        super().__init__(icons_sprite)
        self.icons_sprite = icons_sprite
        self.image = Hints.image
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.x += list_spawn_pos[0]
        self.rect.y += list_spawn_pos[1]

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.rect.y += cam_y
