import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))

clock = pygame.time.Clock()
v = 100

coord = []
speed = []
color = []

screen_2 = pygame.Surface(screen.get_size())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            coord.append([pos[0], pos[1]])
            color.append('#{:06x}'.format(random.randrange(0, 0xffffff)))
            speed.append(v)
    screen_2.fill(pygame.Color('black'))
    for i in range(len(coord)):
        pygame.draw.circle(screen_2, pygame.Color(color[i]), (coord[i][0], int(coord[i][1])), 10)
        coord[i][1] += speed[i] * clock.tick() / 1000
        if coord[i][1] >= HEIGHT - 10:
            speed[i] = 0

    screen.blit(screen_2, (0, 0))
    pygame.display.flip()

pygame.quit()
