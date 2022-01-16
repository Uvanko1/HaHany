import pygame


class Sounds:
    def horse(self):
        pygame.mixer.init()
        pygame.mixer.music.load('../sounds/horse.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    def river(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
