import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))
clock = pygame.time.Clock()
v = 100
fps = 60
# x, y = pos = (0, 0)
# color = (200, 0, 0)

# create 2 lists for saving properties of balls
# coords, colors
balls_coord_x = []
balls_coord_y = []
balls_colors = []

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
    #         color = balls_colors[0]
    # pygame.draw.circle(screen, pygame.Color(*color), (x, int(y)), 10)
    # y += v * clock.tick() / 1000

    for i in range(len(balls_coord_x)):
        pygame.draw.circle(screen, pygame.Color(
            *balls_colors[i]
        ), (balls_coord_x[i], int(balls_coord_y[i])), 10)
    for i in range(len(balls_coord_y)):
        balls_coord_y[i] += v * clock.tick(fps) / 1000

    pygame.display.flip()
pygame.quit()
