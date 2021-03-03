import pygame
import imgs
import plants

pygame.init()

screen = pygame.display.set_mode((1000, 611))

pygame.display.set_caption("Plants vs Zombies by b4rt0n")
imgs.icon()

imgs.background(screen)
pygame.display.update()
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                plants.Plant(screen, mx, my)
