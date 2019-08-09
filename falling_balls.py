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
# coord, colors

balls_coord = []
balls_colors = []

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls_coord.append(event.pos)

            balls_colors.append(
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )

    for i in range(len(balls_coord)):
        pygame.draw.circle(screen, pygame.Color(
            *balls_colors[i]
        ), (balls_coord[i][0], int(balls_coord[i][1])), 10)
        y = balls_coord[i][1]
        y += v * clock.tick(fps) / 100
        if y >= HEIGHT - 10:
            y = HEIGHT - 10
        balls_coord[i] = (balls_coord[i][0], y)

    pygame.display.flip()
pygame.quit()
