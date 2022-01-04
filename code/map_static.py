import pygame

map_sprite = pygame.sprite.Group()


class MapSprite(pygame.sprite.Sprite):
    image = pygame.image.load('../maps/map_data/mongolian.png')

    def __init__(self):
        super().__init__(map_sprite)
        self.image = MapSprite.image
        self.rect = self.image.get_rect()

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.rect.y += cam_y
