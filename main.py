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
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Pre-Alpha")
pygame.display.flip()




#Variables
clock = pygame.time.Clock()
x = 30
y = 30
carimage = pygame.image.load("res/ford_gt.png")
carimage2 = pygame.image.load("res/ford_gt.png")



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
        if pressed[pygame.K_UP]:
            y -= 3
            carimage = pygame.image.load("res/ford_gt.png")
            carimage2 = carimage
        if pressed[pygame.K_DOWN]:
            y += 3
            carimage = pygame.image.load("res/ford_gt.png")
            carimage2 =pygame.transform.rotate(carimage, 180)
        if pressed[pygame.K_LEFT]:
            x -= 3
            carimage = pygame.image.load("res/ford_gt.png")
            carimage2 =pygame.transform.rotate(carimage, 90)
        if pressed[pygame.K_RIGHT]:
            x += 3
            carimage = pygame.image.load("res/ford_gt.png")
            carimage2 =pygame.transform.rotate(carimage, 270)
        if pressed[pygame.K_SPACE]:
            if x >= 1175:
                if y >= 615:
                    done = True 
            if x <= 163:
                if y <= 87:
                    print("do you GEdit the Conky Joke?")
        if x >=1270:
            x = 1268
        if x <= -1:
            x = 2
        if y >= 710:
            y = 708
        if y <= -1:
            y = 2
        label = font.render("Exit", 1, white)
        labelstart = font.render("Start the Race!", 10, white)
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, darkdarkred, pygame.Rect(0, 0, 6000, 6000))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 620, 100, 100))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 160, 85))
        screen.blit(carimage2, (x,y))
        screen.blit(label, (1185, 625))
        screen.blit(labelstart, (10, 10))
        pygame.display.flip()
        clock.tick(100)

