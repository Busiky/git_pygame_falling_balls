import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))

# create 2 lists for saving properties of balls
# coords, colors
balls_coords = []
balls_colors = []

running = True
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            balls_coords.append(pos)
            balls_colors.append(
                pygame.Color(
                    (
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255)
                    )
                )
            )

    pygame.display.flip()
pygame.quit()
