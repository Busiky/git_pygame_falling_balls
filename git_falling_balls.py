import pygame

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('black'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

    pygame.display.flip()
pygame.quit()
