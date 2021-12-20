import pygame
import pytmx

from constans import *


class Chunk:
    def __init__(self, filename_map):
        self.map = pytmx.load_pygame(f'{MAPS_DIR}/{filename_map}')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth

    def render(self, screen, cam_x, cam_y):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                print(cam_x, cam_y)
                screen.blit(image, (x * self.tile_size - cam_x, y * self.tile_size - cam_y))

    def get_title_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    chunk = Chunk(MAP_FILE)
    clock = pygame.time.Clock()
    cam_x, cam_y = 0, 0
    frame = 0
    while 1:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                cam_x -= 10
            if key[pygame.K_d]:
                cam_x += 10
            if key[pygame.K_w]:
                cam_y -= 10
            if key[pygame.K_s]:
                cam_y += 10

        chunk.render(screen, cam_x, cam_y)
        pygame.display.update()
        clock.tick(480)
        frame += 1
        if frame % 10 == 0:
            pygame.display.set_caption('FPS' + str(round(clock.get_fps())))


if __name__ == "__main__":
    main()
