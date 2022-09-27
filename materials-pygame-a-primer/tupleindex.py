import pygame

pygame.init()

size = pygame.display.get_desktop_sizes()

SCREEN_WIDTH = size[0][0]
SCREEN_HEIGHT = size[0][1]

print(SCREEN_WIDTH)
print(SCREEN_HEIGHT)