import pygame
import random
import board_data
import helpers

suns = pygame.sprite.Group()

balance = 100  # starting bank balance


def balanceBgDisplay(screen):
    balanceBg = pygame.Surface((200, 28))
    balanceBg.fill((255, 255, 255))
    screen.blit(balanceBg, (190, 575))


def balanceDisplay(screen, balanceValue):
    black = (0, 0, 0)
    font = pygame.font.SysFont("Times New Roman", 24)
    balanceLabel = font.render("Your balance:", True, black)
    balanceValue = font.render(str(balance), True, black)
    screen.blit(balanceLabel, (200, 575))
    screen.blit(balanceValue, (340, 575))


class Sun(pygame.sprite.Sprite):
    sunSize = 50
    spawnOffset = 20

    def __init__(self):
        print("Sun Sprite")
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('gfx/misc/sun.png')
        self.image = pygame.transform.scale(self.image, (self.sunSize, self.sunSize))
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(board_data.Xmin + self.spawnOffset, board_data.Xmax - self.spawnOffset),
            random.randint(board_data.Ymin + self.spawnOffset, board_data.Ymax - self.spawnOffset)
        )
        t0 = pygame.time.get_ticks() + 5000
        t1 = t0 + 10000  # 10 s
        helpers.generationTime = random.randint(t0, t1)


def spawn(screen):
    sunSize = 50
    print("sun")
    im = pygame.image.load('gfx/misc/sun.png')
    im = pygame.transform.scale(im, (sunSize, sunSize))
    suns.append(im)
    screen.blit(im, (
        random.randint(board_data.Xmin, board_data.Xmax - sunSize),
        random.randint(board_data.Ymin, board_data.Ymax - sunSize)
    ))
    t0 = pygame.time.get_ticks() + 5000
    t1 = t0 + 10000  # 10 s
    helpers.generationTime = random.randint(t0, t1)
