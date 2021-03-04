import pygame
import helpers
import board_data


# class Object(object):
#     height = 80
#     width = 60
#     line = 0
#
#     pass
#
#
# class Plant(Object):
#
#     def __init__(self, screen, mx, my, im):
#         print(helpers.getGridCoords(mx, my))
#         cx, cy = helpers.getGridCoords(mx, my)
#         if cx != 0 or cy != 0:
#             im = pygame.transform.scale(im, (self.width, self.height))
#             screen.blit(im, (
#                 board_data.Xmin + cx * board_data.fieldX - self.width - 5,
#                 board_data.Ymin + cy * board_data.fieldY - self.height - 10
#             ))

plants = pygame.sprite.Group()


class Object(pygame.sprite.Sprite):
    height = 80
    width = 60
    line = 0


class Plant(Object):
    def __init__(self, screen, mx, my, im):
        print("Plant Sprite")
        pygame.sprite.Sprite.__init__(self)
        print(helpers.getGridCoords(mx, my))
        cx, cy = helpers.getGridCoords(mx, my)
        if cx != 0 or cy != 0:
            self.image = pygame.transform.scale(im, (self.width, self.height))
            self. rect = self.image.get_rect()
            self.rect.topleft = (
                board_data.Xmin + cx * board_data.fieldX - self.width - 5,
                board_data.Ymin + cy * board_data.fieldY - self.height - 10
            )


class Sunflower(Plant):
    cost = 50

    def __init__(self, screen, mx, my):
        im = pygame.image.load('gfx/plants/sunflower.png')
        super(Sunflower, self).__init__(screen, mx, my, im)
