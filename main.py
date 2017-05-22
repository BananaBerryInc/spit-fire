# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess
from ConfigParser import SafeConfigParser

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
currentcar = "ford_gt"
cartext = "Car: "
track = 1
trackname = "First_track"
clockspeed = 100
parser = SafeConfigParser()


#Colours (Thanks to atmatm6 for the code in this section!)
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

label = font.render("Exit", 1, white)
labelstart = font.render("Start the Race!", 10, white)

#Passoff to the main python script
def sendtomain():
    global parser
    global carimage
    global currentcar
    global track
    global trackname
    global clockspeed
    parser.read("res/options.ini")
    parser.set("Options", "track", track)
    parser.set("Options", "car", currentcar)
    parser.set("Options", "carimage", carimage)
    parser.set("Options", "speed", clockspeed)
    execfile("res/race.py")


#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Mainloop...?
        #Key detection!
        if pressed[pygame.K_UP]:
            y -= 3
            carimage2 = carimage
        if pressed[pygame.K_DOWN]:
            y += 3
            carimage2 = pygame.transform.rotate(carimage, 180)
        if pressed[pygame.K_LEFT]:
            x -= 3
            carimage2 = pygame.transform.rotate(carimage, 90)
            if pressed[pygame.K_UP]:
                carimage2 = pygame.transform.rotate(carimage, 45)
            if pressed[pygame.K_DOWN]:
                carimage2 = pygame.transform.rotate(carimage, 135)
        if pressed[pygame.K_RIGHT]:
            x += 3
            carimage2 = pygame.transform.rotate(carimage, 270)
            if pressed[pygame.K_UP]:
                carimage2 = pygame.transform.rotate(carimage, 315)
            if pressed[pygame.K_DOWN]:
                carimage2 = pygame.transform.rotate(carimage, 225)
        if pressed[pygame.K_C]:
            if currentcar == "Ferrari_F40":
                currentcar = "ford_gt"
                carimage = pygame.image.load("res/ford_gt.png")
                change = 1
            if currentcar == "ford_gt":
                if change == 0:
                    currentcar = "Ferrari_F40"
                    carimage = pygame.image.load("res/Ferrari_F40.png")
                    change = 1
        if pressed[pygame.K_T]:
            track += 1
            if track >= 2:
                track = 1
                trackname = "Test_track"
            if track == 1:
                trackname = "First_track"
        if pressed[pygame.K_S]:
            clockspeed = clockspeed + 50
            if clockspeed >> 200:
                clockspeed = 50
        if pressed[pygame.K_SPACE]:
            if x >= 1175:
                if y >= 615:
                    done = True
            if x <= 163:
                if y <= 87:
                    print("do you GEdit the Conky Joke?")
        #Collision/OOB detection
        if x >=1270:
            x = 1268
        if x <= -1:
            x = 2
        if y >= 710:
            y = 708
        if y <= -1:
            y = 2
        #Other Variables
        change = 0
        carlabel = cartext + currentcar
        carlabel2 = font.render(carlabel, 10, white)
        tracklabel = "Track " + str(track) + ": " + trackname
        tracklabel2 = font.render(tracklabel, 10 ,white)
        clockspeedlabel = clockspeed + " CC"
        clockspeedlabel2 = font.render(clockspeedlabel, 10 ,white)
        #Drawing/rendering
        pygame.draw.rect(screen, darkdarkred, pygame.Rect(0, 0, 6000, 6000))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 620, 100, 100))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 160, 85))
        screen.blit(tracklabel2, (200,200))
        screen.blit(clockspeedlabel2, (300, 300))
        screen.blit(carimage2, (x,y))
        screen.blit(label, (1185, 625))
        screen.blit(labelstart, (10, 10))
        screen.blit(carlabel2, (100, 100))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
