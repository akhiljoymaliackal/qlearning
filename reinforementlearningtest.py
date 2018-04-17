import pygame
import sys
import time
from pygame.locals import QUIT


pygame.init()

screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption("reinforcement learning")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (227, 27, 27)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RCB = (27, 27, 27)
img = pygame.image.load('bird.jpg')
nest=pygame.image.load('nest.jpg')
screen.fill(WHITE)


pygame.draw.line(screen, RED, [150, 50], [1250,50], 5)
pygame.draw.line(screen, RED, [150, 170], [150,1000], 5)
pygame.draw.line(screen, RED, [150, 1000], [1250,1000], 5)


pygame.draw.line(screen, RED, [450, 50], [450,400], 5)
pygame.draw.line(screen, RED, [450, 350], [300,350], 5)

pygame.draw.line(screen, RED, [270, 750], [450,750], 5)
pygame.draw.line(screen, RED, [450, 750], [450,550], 5)
pygame.draw.line(screen, RED, [150, 550], [300,550], 5)
pygame.draw.line(screen, RED, [450, 1000], [450,900], 5)

pygame.draw.line(screen, RED, [850, 200], [850,700], 5)
pygame.draw.line(screen, RED, [850, 320], [650,320], 5)
pygame.draw.line(screen, RED, [450, 720], [650,720], 5)
pygame.draw.line(screen, RED, [850, 1000], [850,850], 5)

pygame.draw.line(screen, RED, [1250, 50], [1250,840], 5)
pygame.draw.line(screen, RED, [1250, 395], [1000,395], 5)
pygame.draw.line(screen, RED, [850, 700], [1100,700], 5)
pygame.draw.line(screen, RED, [1250, 395], [1000,395], 5)





screen.blit(img,(1260,750))
screen.fill(WHITE)

screen.blit(nest,(1260,850))
while True:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
