import pygame


def background(screen):
    bgImg = pygame.image.load('gfx/background/frontyard.png')
    screen.blit(bgImg, (0, 0))


def icon():
    ic = pygame.image.load('gfx/plants/sunflower.png')
    pygame.display.set_icon(ic)