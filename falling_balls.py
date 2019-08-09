import pygame

pygame.init()

size = WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('#000000'))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
