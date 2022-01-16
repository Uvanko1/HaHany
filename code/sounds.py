import pygame

pygame.mixer.init()
pygame.mixer.music.load('../sounds/horse.mp3')
alll = pygame.mixer.Sound('../sounds/SQWOZ_BAB_-_TATARSKIJJ_BOGATYR_(ru.muzikavsem.org).mp3')

pygame.mixer.music.play(-1)
pygame.mixer.music.pause()


def horse(play_music):
    if play_music:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()


def all():
    alll.set_volume(0.2)
    alll.play(-1)
