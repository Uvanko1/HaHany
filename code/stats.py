import pygame

stats_sprite = pygame.sprite.Group()


class Stats:
    def __init__(self):
        self.horse = pygame.sprite.Sprite(stats_sprite)
        self.horse.image = pygame.image.load('../graphics/stats/horse_stats.png')
        self.horse.rect = self.horse.image.get_rect(left=30)
        self.mongol = pygame.sprite.Sprite(stats_sprite)
        self.mongol.image = pygame.image.load('../graphics/stats/mongol_stats.png')
        self.mongol.rect = self.horse.image.get_rect(left=90)
        self.wood = pygame.sprite.Sprite(stats_sprite)
        self.wood.image = pygame.image.load('../graphics/stats/wood_stats.png')
        self.wood.rect = self.wood.image.get_rect(left=150)

    def draw_stats_text(self, screen, text_x, text_y, text):
        font = pygame.font.SysFont('Arial', 20)
        text_end = font.render(text, True, (0, 0, 0))
        screen.blit(text_end, (text_x, text_y))
