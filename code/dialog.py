import pygame
from game_data import dialogs, dialogs_pos

ramka_sprite = pygame.sprite.Group()


class Dialog(pygame.sprite.Sprite):
    image = pygame.image.load('../graphics/Диалоги/ramka.png')

    def __init__(self):
        super().__init__(ramka_sprite)
        self.image = Dialog.image
        self.rect = self.image.get_rect(top=250)
        self.text_flag = False

    def draw_text(self, screen, pos=None):
        text_dialog = dialogs[pos]
        font = pygame.font.Font(None, 25)
        text = font.render(text_dialog, True, (255, 255, 255))
        text_x = 30
        text_y = 273
        screen.blit(text, (text_x, text_y))
