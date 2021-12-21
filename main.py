import pygame

import pytmx
from constans import *

pygame.init()

cam_x, cam_y = 0, 0

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, size)

clock = pygame.time.Clock()

chunk_size = 65
world_map = pytmx.load_pygame(f'{MAPS_DIR}/{MAP_FILE}')
tile_size = world_map.tilewidth
textures = None

world_size_chunk_x = 1024 // chunk_size
world_size_chunk_y = 1024 // chunk_size


def chunks_on_screen():
    x1 = cam_x // (chunk_size * tile_size)
    y1 = cam_y // (chunk_size * tile_size)

    x2 = (cam_x + res[0]) // (chunk_size * tile_size)
    y2 = (cam_y + res[1]) // (chunk_size * tile_size)

    x1 = min(max(x1, 0), world_size_chunk_x - 1)
    x2 = min(max(x2, 0), world_size_chunk_x - 1)

    y1 = min(max(y1, 0), world_size_chunk_y - 1)
    y2 = min(max(y2, 0), world_size_chunk_y - 1)

    result = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result.append(x + y * world_size_chunk_x)

    return result


class Chunk:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.map = world_map

    def render(self):
        for y in range(chunk_size + 22):
            for x in range(chunk_size):
                texture = self.map.get_tile_image(x, y, 0)
                screen.blit(texture, (self.x + x * tile_size - cam_x, self.y + y * tile_size - cam_y))


chunks = []
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x * chunk_size * tile_size, y * chunk_size * tile_size))

frame = 0
while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        cam_x -= 20
    if key[pygame.K_d]:
        cam_x += 20
    if key[pygame.K_w]:
        cam_y -= 20
    if key[pygame.K_s]:
        cam_y += 20

    for i in chunks_on_screen():
        chunks[i].render()

    window.blit(pygame.transform.scale(screen, size), (0, 0))
    pygame.display.update()
    clock.tick(480)

    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
        chunks_on_screen()
