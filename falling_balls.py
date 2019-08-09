import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))
clock = pygame.time.Clock()
v = 100
fps = 60

# create 2 lists for saving properties of balls
# coords, colors

balls_coords = []
balls_colors = []
bottom = []

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls_coords.append(event.pos)

            balls_colors.append(
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )

    for i in range(len(balls_coords)):
        pygame.draw.circle(screen, pygame.Color(
            *balls_colors[i]
        ), (balls_coords[i][0], int(balls_coords[i][1])), 10)
        y = balls_coords[i][1]
        y += v * clock.tick(fps) / 100
        if y >= HEIGHT - 10:
            y = HEIGHT - 10
        balls_coords[i] = (balls_coords[i][0], y)

    for i in range(len(balls_coords)):
        if balls_coords[i][1] >= HEIGHT - 10:
            bottom.append(i)

    for i in bottom:
        pygame.draw.circle(screen, pygame.Color(
            *balls_colors[i]
        ), (balls_coords[i][0], HEIGHT - 10), 10)

    pygame.display.flip()
pygame.quit()
