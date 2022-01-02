import pygame
from PIL import Image
from settings import screen_width, screen_height

Image.MAX_IMAGE_PIXELS = None


class MapStatic:
    def __init__(self):
        super().__init__()
        self.crop_map = None
        self.chunk_y = None
        self.chunk_x = None
        # self.im = Image.open('../maps/map_data/mongolian.png')
        # self.map_surf = pygame.image.load('../maps/map_data/mongolian.png')
        self.crop_im = None
        self.rect = pygame.Rect(0, 0, 1920, 1080)
        # self.num_chunk_x = int(self.re.get_size()[0] // screen_width)
        # self.num_chunk_y = int(self.map_surf.get_size()[1] // screen_height)

    def update(self, cam_x, cam_y):
        self.rect.x += cam_x
        self.chunk_x = self.rect.x // screen_width
        self.rect.y += cam_y
        self.chunk_y = self.rect.y // screen_height

    # сделать функцию Перепечаеву Ивану
    def render(self, screen):
        # for row in range(self.num_chunk_y):
        #     for col in range(self.num_chunk_x):
        #         if row == -self.chunk_y and col == -self.chunk_x:
        #             x = col * screen_width
        #             y = row * screen_height
        #             self.crop_im = self.im.crop((x, y, x + screen_width, y + screen_height))
        #             self.crop_im.save('crop.png', quality=95)
        self.crop_map = pygame.image.load('crop.png')
        screen.blit(self.crop_map, (0, 0), (self.rect.x, self.rect.y, screen_width, screen_height))

