import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.rect.y += cam_y


class HorseTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

    def update(self, cam_x, cam_y):
        # print(cam_x, cam_y)
        pass


class ForestTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface
