import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))
clock = pygame.time.Clock()
v = 100
x, y = pos = (0, 0)
color = (200, 0, 0)

# create 2 lists for saving properties of balls
# coords, colors
balls_coords = []
balls_colors = []

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pos = event.pos
            balls_coords.append(pos)

            balls_colors.append(
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )
            color = balls_colors[0]
    pygame.draw.circle(screen, pygame.Color(*color), (x, int(y)), 10)
    y += v * clock.tick() / 1000


    # for i in range(len(balls_coords)):
    #     pygame.draw.circle(screen, pygame.Color(
    #         *balls_colors[i]
    #     ), balls_coords[i], 10)
    # for i in range(len(balls_coords)):
    #     x, y = balls_coords[i][0], int(
    #         balls_coords[i][1] + v * clock.tick() / 1000)
    #     balls_coords[i] = (x, y)

    pygame.display.flip()
pygame.quit()
