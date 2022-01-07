import pygame
from settings import screen_width, screen_height
from saves import get_save_position

map_sprite = pygame.sprite.Group()
lst_spawn_pos = get_save_position()


class MapSprite(pygame.sprite.Sprite):
    image = pygame.image.load('../maps/map_data/mongolian.png')

    def __init__(self):
        super().__init__(map_sprite)
        self.image = MapSprite.image
        self.rect = self.image.get_rect()
        self.rect.x = -lst_spawn_pos[0]
        self.rect.y = -lst_spawn_pos[1]

    def update(self, cam_x, cam_y):
        if self.rect.x + cam_x <= 0 and -(self.rect.x + cam_x) <= self.rect.width - screen_width:
            self.rect.x += cam_x
        if self.rect.y + cam_y <= 0 and -(self.rect.y + cam_y) <= self.rect.height - screen_height:
            self.rect.y += cam_y

    def get_rect_pos(self):
        return self.rect.x, self.rect.y
