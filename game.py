import pygame
import imgs
import plants
import suns
import helpers

FPS = 30

allSprites = pygame.sprite.Group()
balanceValue = ""


def gameInit():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000, 611))
    pygame.display.set_caption("Plants vs Zombies by b4rt0n")
    imgs.icon()
    imgs.background(screen)
    suns.balanceBgDisplay(screen)
    pygame.display.update()



    running = True
    while running:
        clock.tick(FPS)
        pygame.display.update()
        allSprites.update()
        allSprites.draw(screen)
        suns.balanceBgDisplay(screen)
        suns.balanceDisplay(screen, balanceValue)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if event.button == 3:
                    sunflower = plants.Sunflower(screen, mx, my)
                    plants.plants.add(sunflower)
                    allSprites.add(sunflower)
                if event.button == 1:  # collecting suns
                    clicked_sprites = [s for s in suns.suns if s.rect.collidepoint(mx, my)]
                    print(clicked_sprites)
                    if clicked_sprites:
                        clicked_sprites[0].kill()
                        suns.suns.clear(screen, pygame.image.load('gfx/background/frontyard.png'))
                        suns.suns.draw(screen)
                        suns.balance += 25
                        print("Balance: ", suns.balance)
                    pass

        if pygame.time.get_ticks() >= helpers.generationTime:
            sun = suns.Sun()
            suns.suns.add(sun)
            allSprites.add(sun)

        # drawing

        #imgs.background(screen)
