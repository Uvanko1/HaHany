import pygame

from game_data import dialogs

ramka_sprite = pygame.sprite.Group()


class Dialog(pygame.sprite.Sprite):
    image = pygame.image.load('../graphics/Диалоги/ramka_1.png')

    def __init__(self):
        super().__init__(ramka_sprite)
        self.image = Dialog.image
        self.rect = self.image.get_rect(top=680)
        self.text_flag = False

    def draw_text(self, screen, dialog_num, dialog_part=0):
        try:
            text_dialog = dialogs[dialog_num]
            if dialog_part <= len(text_dialog) - 1:
                text_dialog_part = text_dialog[dialog_part]
                print(text_dialog)
            else:
                text_dialog_part = 'esc - закрыть'
        except KeyError:
            text_dialog_part = 'Не со мной говори, тут вопросы не я решаю'
        font = pygame.font.SysFont('Verdana', 50)
        text_x = 100
        text_y = 780
        lines = text_dialog_part.splitlines()
        for i, l in enumerate(lines):
            screen.blit(font.render(l, True, (255, 255, 255)), (text_x, text_y + 50 * i))
