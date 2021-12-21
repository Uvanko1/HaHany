import pygame

import pytmx
from constans import *

pygame.init()

cam_x, cam_y = 1, 1
cam_coords = [0, 0, 1920, 1080]

window = pygame.display.set_mode(WINDOW_SIZE)
screen = pygame.transform.scale(window, WINDOW_SIZE)

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
        self.cam_coords = cam_coords

    def render(self):
        try:
            for i in range(2):
                for x in range(self.cam_coords[2] // title_size):
                    for y in range(self.cam_coords[3] // title_size):
                        if 0 < x + cam_x <= self.map.width and 0 < y + cam_y < self.map.height:
                            texture = self.map.get_tile_image(x + cam_x, y + cam_y, i)
                            if texture is not None:
                                screen.blit(texture, (self.x + x * tile_size, self.y + y * tile_size))
                                self.cam_coords = 0 + cam_x, 0 + cam_y, 1920 + cam_x, 1080 + cam_y
        except ValueError:
            pass


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
    print(cam_x, cam_y)
    if key[pygame.K_a]:
        if 1 < cam_x:
            cam_x -= 1
    if key[pygame.K_d]:
        if cam_x < 232:
            cam_x += 1
    if key[pygame.K_w]:
        if 1 < cam_y:
            cam_y -= 1
    if key[pygame.K_s]:
        if cam_y < 258:
            cam_y += 1

    for i in chunks_on_screen():
        chunks[i].render()
    window.blit(pygame.transform.scale(screen, WINDOW_SIZE), (0, 0))
    pygame.display.update()
    clock.tick(480)

    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
        chunks_on_screen()
