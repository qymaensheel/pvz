import pygame
import helpers


class Object(object):
    height = 80
    width = 60
    line = 0

    pass


class Plant(Object):
    def __init__(self, screen, mx, my):
        print(helpers.getGridCoords(mx,my))
        im = pygame.image.load('gfx/plants/sunflower.png')
        im = pygame.transform.scale(im,(self.width,self.height))
        screen.blit(im, (mx-30, my-60))
        pass
