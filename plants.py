import pygame
import helpers
import board_data


class Object(object):
    height = 80
    width = 60
    line = 0

    pass


class Plant(Object):
    cost = 0

    def __init__(self, screen, mx, my):
        print(helpers.getGridCoords(mx, my))
        cx, cy = helpers.getGridCoords(mx, my)
        if cx != 0 or cy != 0:
            im = pygame.image.load('gfx/plants/sunflower.png')
            im = pygame.transform.scale(im, (self.width, self.height))
            screen.blit(im, (
                board_data.Xmin + cx * board_data.fieldX - self.width - 5,
                board_data.Ymin + cy * board_data.fieldY - self.height - 10
            ))


class Sunflower(Plant):


    pass