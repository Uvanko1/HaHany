import pygame

pygame.mixer.init()
pygame.mixer.music.load('../sounds/horse.mp3')
soundtrack = pygame.mixer.Sound('../sounds/soundtrack.mp3')
cut_tree = pygame.mixer.Sound('../sounds/cut_tree.mp3')

pygame.mixer.music.play(-1)
pygame.mixer.music.pause()


def horse(play_music):
    if play_music:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()


def soundtrack_on():
    soundtrack.set_volume(0.1)
    soundtrack.play(-1)


def cut_tree_sound(flag):
    cut_tree.set_volume(0.8)
    if flag:
        cut_tree.play()
    else:
        cut_tree.stop()
