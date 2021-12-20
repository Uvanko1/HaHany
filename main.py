import pygame
import pytmx

from constans import *


class Chunk:
    def __init__(self, filename_map):
        self.map = pytmx.load_pygame(f'{MAPS_DIR}/{filename_map}')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))

    def get_title_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    chunk = Chunk(MAP_FILE)
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    while 1:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        chunk.render(screen)
        pygame.display.update()
        clock.tick(480)


if __name__ == "__main__":
    main()
