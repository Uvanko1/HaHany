import pygame
from settings import screen_width, screen_height

map_sprite = pygame.sprite.Group()


def import_cut_map_graphic(path):
    surface = pygame.image.load(path)
    chunk_x = int(surface.get_size()[0] // screen_width)
    chunk_y = int(surface.get_size()[1] // screen_height)
    cut_map_lst = []
    for row in range(chunk_y):
        for col in range(chunk_x):
            x = col * screen_width
            y = row * screen_height
            cut_map = pygame.Rect(x, y, screen_width, screen_height)
            cut_map_lst.append(cut_map)
    return cut_map_lst


print(import_cut_map_graphic('../maps/map_data/mongolian.png'))


class MapStatic(pygame.sprite.Sprite):
    image = pygame.image.load('../maps/map_data/mongolian.png')

    def __init__(self):
        super().__init__(map_sprite)
        self.image = pygame.image.load('../maps/map_data/mongolian.png')
        self.image = MapStatic.image
        self.rect = self.image.get_rect()

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.rect.y += cam_y

    # сделать функцию Перепечаеву Ивану
    def draw(self, screen):
        pass
