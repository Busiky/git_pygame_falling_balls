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
balls_coord_x = []
balls_coord_y = []
balls_colors = []
bottom = []

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pos = event.pos
            balls_coord_x.append(x)
            balls_coord_y.append(y)

            balls_colors.append(
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
            )

    for i in range(len(balls_coord_x)):
        pygame.draw.circle(screen, pygame.Color(
            *balls_colors[i]
        ), (balls_coord_x[i], int(balls_coord_y[i])), 10)
        balls_coord_y[i] += v * clock.tick(fps) / 100

    for i in range(len(balls_coord_y)):
        if balls_coord_y[i] >= HEIGHT - 10:
            bottom.append((
                balls_coord_x[i],
                balls_colors[i]
            ))

    for i in range(len(bottom)):
        pygame.draw.circle(screen, pygame.Color(
            *bottom[i][1]
        ), (bottom[i][0], HEIGHT - 10), 10)

    pygame.display.flip()
pygame.quit()
