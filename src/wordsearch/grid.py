import pygame, sys
import random, string


def png(grid, size):
    pygame.init()
    WINDOW_SIZE = 800
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    SCREEN.fill((0,0,0,0))

    blockSize = WINDOW_SIZE/size
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            font = pygame.font.SysFont(None, int(blockSize))
            text = font.render(grid[y][x], True, (200,200,200))
            text_rect = text.get_rect(center=(blockSize/2+x*blockSize, blockSize/2+y*blockSize))
            SCREEN.blit(text, text_rect)

    # for x in range(0, WINDOW_SIZE, blockSize):
    #     for y in range(0, WINDOW_SIZE, blockSize):
    #         font = pygame.font.SysFont(None, 40)
    #         text = font.render(random.choice(string.ascii_letters).upper(), True, (200,200,200))
    #         text_rect = text.get_rect(center=(blockSize/2+x, blockSize/2+y))
    #         SCREEN.blit(text, text_rect)

    pygame.image.save(SCREEN, "grid.png")
    pygame.quit()
