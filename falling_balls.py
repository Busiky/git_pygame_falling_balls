import pygame
import random

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))
v = 100
clock = pygame.time.Clock()

# create dict for saving properties of balls
# (color): [coords]
balls = {}
bottom = {}

screen_2 = pygame.Surface(screen.get_size())
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen_2.blit(screen, (0, 0))
            pos = event.pos
            balls[
                (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )] = [pos[0], pos[1]]
    print(balls)
    screen_2.fill(pygame.Color('black'))
    for ball in balls:
        pygame.draw.circle(screen_2, pygame.Color(*ball), (
            balls[ball][0], balls[ball][1]
        ), 10)
        balls[ball][1] += int(v * clock.tick() / 100)
        if balls[ball][1] >= HEIGHT - 5:
            bottom[ball] = [balls[ball][0], HEIGHT - 5]
        screen.fill(pygame.Color('black'))
        screen.blit(screen_2, (0, 0))

    for ball in bottom:
        pygame.draw.circle(screen_2, pygame.Color(*ball), (
            bottom[ball][0], bottom[ball][1]
        ), 10)
        if balls[ball][1] >= HEIGHT - 5:
            del balls[ball]
        screen.blit(screen_2, (0, 0))
    pygame.display.flip()
pygame.quit()
