import pygame
import sys
import time
from pygame.locals import QUIT
import random
pixels=[[130,60],[190,350],[480,400],[300,540],[210,800],[550,150],[900,150],[950,450],[1080,700],[600,650],[450,750],[850,750],[1260,750]]
r=[[-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,0,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1],
   [-1,0,0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,-1,-1],
   [-1,-1,0,-1,-1,-1,0,-1,-1,0,-1,-1,-1],
   [-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,0,100],
   [-1,-1,-1,-1,-1,0,-1,-1,-1,-1,0,0,-1],
   [-1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,0,-1],
   [-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,-1,100],
   [-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,0,100],
   ]

q=[[0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0],
   ]


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
imgrplc = pygame.image.load('birdrplc.jpg')
nest=pygame.image.load('nestt.jpg')
def draw():
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
    screen.blit(nest,(1350,750))
def train():
    state=random.randint(0,12)

    finish=False
    while(not finish):
        finish_state=False
        while(not finish_state):
            state_next=random.randint(0,12)

            if r[state][state_next]>=0:
                finish_state=True
                #screen.blit(img,(pixels[state_next][0],pixels[state_next][1]))
                #pygame.display.flip()
                #time.sleep(.20)
                #screen.blit(imgrplc,(pixels[state_next][0],pixels[state_next][1]))
        update(state,state_next)
        state=state_next
        if state==12:
            finish=True

def train_show():
    state=random.randint(0,12)

    finish=False
    while(not finish):
        finish_state=False
        while(not finish_state):
            state_next=random.randint(0,12)

            if r[state][state_next]>=0:
                finish_state=True
                screen.blit(img,(pixels[state_next][0],pixels[state_next][1]))
                pygame.display.flip()
                time.sleep(.20)
                screen.blit(imgrplc,(pixels[state_next][0],pixels[state_next][1]))
        update(state,state_next)
        state=state_next
        if state==12:
            finish=True


def trained_matrix():
    state=0

    finish=False
    while(not finish):
        finish_state=False
        while(not finish_state):
            state_next=random.randint(0,12)
            if q[state][state_next]>=maximum(q[state]):
                finish_state=True
                screen.blit(img,(pixels[state_next][0],pixels[state_next][1]))
                pygame.display.flip()
                time.sleep(2)
                screen.blit(imgrplc,(pixels[state_next][0],pixels[state_next][1]))

        state=state_next
        if state==12:
            finish=True
def update(state,state_next):
    gamma=0.5
    alpha=0.8
    q[state][state_next]+=(alpha*(r[state][state_next]+(gamma*(maximum(q[state_next])))-q[state][state_next]))


def maximum(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max

draw()
screen.blit(img,(50,150))


for i in range(1000):
    train()
for i in q:
    print i
for i in range(3):
    draw()
    train_show()
trained_matrix()
screen.blit(img,(pixels[state_next][0],pixels[state_next][1]))

def max_val(state):
    max_v=0
    for i in range(0,12):
        if r[state][i]>max_v:
            max_v=r[state][i]
    return max_v

while True:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
