# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess

#Settin' up the window!
pygame.init()
font = pygame.font.SysFont("monospace", 15)
pygame.font.init()
font = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode((700, 450))
done = False
pygame.display.set_caption("Spitfire Pre-Alpha")
pygame.display.flip()



#Variables
clock = pygame.time.Clock()
x = 30
y = 30




#Colours
black = (0,0,0)
white = (255,255,255)
brown = (100,42,42)
gray = (128,128,128)
darkdarkred = (64,0,0)
rhubarb = (128,0,0)
red = (255,0,0)
redorange = (255,64,0)
orange = (255,128,0)
orangeyellow = (255,192,0)
yellow = (255,255,0)
limegreen = (192,255,0)
screengreen = (128,255,0)
lightgreen = (64,255,0)
green = (0,255,0)
mehgreen = (0,255,64)
greenblue = (0,255,128)
aqua = (0,255,192)
lightblue = (0,255,255)
turquoise = (0,192,255)
teal = (0,128,255)
lightdarkblue = (0,64,255)
blue = (0,0,255)
darkblue = (64,0,255)
purple = (128,0,255)
violet = (192,0,255)
magenta = (255,0,255)
darklightmagenta = (255,0,192)
pink = (255,0,128)
lightred = (255,0,64)


#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Mainloop...?
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if x >=690:
		x = 689
        if x <= 10:
		x = 11
        if y >= 440:
		y = 430
        if y <= 1:
		y = 2
        label = font.render("Exit", 1, white)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, blue, pygame.Rect(x, y, 60, 60))
        screen.blit(label, (665, 350))
        pygame.display.flip()
        clock.tick(100)

