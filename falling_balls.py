import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))
v = 100
clock = pygame.time.Clock()

# create dict for saving properties of balls
# (coords): (color)
balls = {}
bottom = {}

screen_2 = pygame.Surface(screen.get_size())
running = True
while running:
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

    screen_2.fill(pygame.Color('black'))
    for pos in balls:
        color = balls[pos]
        pygame.draw.circle(screen_2, pygame.Color(*color), pos, 10)
        x, y = pos
        y += int(v * clock.tick() / 100)
        del balls[pos]
        balls[(x, y)] = color
        if y >= HEIGHT - 10:
            bottom[(x, y)] = color


    for pos in bottom:
        pygame.draw.circle(screen_2, pygame.Color(*bottom[pos]), pos, 10)
        #

    screen.fill(pygame.Color('black'))
    screen.blit(screen_2, (0, 0))

    pygame.display.flip()
pygame.quit()
