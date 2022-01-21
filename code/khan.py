import pygame
from support import import_folder
from settings import screen_width, screen_height

khan_sprite = pygame.sprite.Group()


class Khan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(khan_sprite)
        self.frames_right = import_folder('../graphics/khan/horse_right')
        self.frames_left = import_folder('../graphics/khan/horse_left')
        self.frames_top = import_folder('../graphics/khan/horse_top')
        self.frames_bottom = import_folder('../graphics/khan/horse_bottom')
        self.frames_index = 0
        self.image = self.frames_top[self.frames_index]
        self.rect = self.image.get_rect(topleft=((screen_width // 4) // 2 - 5, (screen_height // 4) // 2 - 5))
        mask_surf = pygame.Surface((16, 12))
        self.mask = pygame.mask.from_surface(mask_surf)

    def update(self, side, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y
        self.animation(side)

    def animation(self, side):
        self.frames_index += 0.15
        if self.frames_index >= 4:
            self.frames_index = 0
        if side == 'right':
            self.image = self.frames_right[int(self.frames_index)]
        if side == 'stop_right':
            self.image = self.frames_right[2]
        if side == 'left':
            self.image = self.frames_left[int(self.frames_index)]
        if side == 'stop_left':
            self.image = self.frames_left[2]
        if side == 'top':
            self.image = self.frames_top[int(self.frames_index)]
        if side == 'stop_top':
            self.image = self.frames_top[1]
        if side == 'bottom':
            self.image = self.frames_bottom[int(self.frames_index)]
        if side == 'stop_bottom':
            self.image = self.frames_bottom[0]
