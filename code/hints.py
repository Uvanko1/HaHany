import pygame

icons_sprite = pygame.sprite.Group()


class Hints(pygame.sprite.Sprite):
    image = pygame.image.load('../graphics/icons/icon_e.png')

    def __init__(self):
        super().__init__(icons_sprite)
        self.icons_sprite = icons_sprite
        self.image = Hints.image
        self.rect = self.image.get_rect(top=180, left=300)
