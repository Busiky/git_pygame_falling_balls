import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))

# create dict for saving properties of balls
# (coords): (color)
balls = {}

running = True
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            balls[pos] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )

    for ball in balls:
        pygame.draw.circle(screen, pygame.Color(
            *balls[ball]
        ), ball, 10)
    pygame.display.flip()
pygame.quit()
