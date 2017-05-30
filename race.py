# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess
from configparser import SafeConfigParser

#Settin' up the window!
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("freesansbold.ttf", 30)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Pre-Alpha")
pygame.display.flip()

#Re-collecting those settings!
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
trackstring = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
trackimage = pygame.image.load(trackpath)
track = int(trackstring)
trackkey = "track" + str(track)
car = parser.get("options", "car")
clockspeedstring = parser.get("options", "speed")
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)

#Variables
carimage = pygame.image.load(carimagepath)
clock = pygame.time.Clock()
x = 30
y = 30
nos = 0
nosinuse = False
lap = "Lap: "
lapcount = 0
place = "Place: "
atstart = True
newlap = False
laptime = 0


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

#Get car stats from the ini file
parser.read("res/carstats.ini")
carspeed = parser.get(car, "speed")
caraccel = parser.get(car, "accel")
carbrake = parser.get(car, "brake")
carhandling = parser.get(car, "handling")
carbrake = parser.get(car, "brake")
caraero = parser.get(car, "aero")
carnos = parser.get(car, "nos")
parser.read("res/tracks.ini")
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")

#More Variables!!!!
mostnos = int(carnos)
nosleft = int(carnos)
aero = int(caraero) / 10
cartopspeed = int(carspeed) / 20 * aero
topspeed = int(carspeed) / 20 * aero
accel = int(caraccel) / 300 * aero
handling = int(carhandling) / 30 * aero
curspeed = 0
startlinex = int(startx)
startliney = int(starty)
checky = int(checkpointy)
checkx = int(checkpointx)
x = startlinex
y = startliney
startneg80x = startlinex - 80
start80x = startlinex + 80
passstart = startliney + 10
carimage2 = pygame.transform.rotate(carimage, 180)


#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Key Detection
        pressed = pygame.key.get_pressed()
        if atstart == True:
            if y >= passstart:
                atstart = False
        if atstart == False:
            if newlap == False:
                if y >= startneg80x:
                    if y <= start80x:
                        if x <= startliney:
                            lapcount += 1
                            newlap = True
        if newlap == True:
            laptime += 1
            if laptime >= 90:
                newlap = False
                laptime = 0
        if pressed[pygame.K_UP]:
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            ynow = y
            y = ynow - curspeed
            carimage2 = carimage
        if pressed[pygame.K_DOWN]:
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            ynow = y
            y = ynow + curspeed
            carimage2 = pygame.transform.rotate(carimage, 180)
        if pressed[pygame.K_LEFT]:
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            xnow = x
            x = xnow - curspeed
            carimage2 = pygame.transform.rotate(carimage, 90)
            if pressed[pygame.K_UP]:
                carimage2 = pygame.transform.rotate(carimage, 45)
            if pressed[pygame.K_DOWN]:
                carimage2 = pygame.transform.rotate(carimage, 135)
        if pressed[pygame.K_RIGHT]:
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            xnow = x
            x = xnow + curspeed
            carimage2 = pygame.transform.rotate(carimage, 270)
            if pressed[pygame.K_UP]:
                carimage2 = pygame.transform.rotate(carimage, 315)
            if pressed[pygame.K_DOWN]:
                carimage2 = pygame.transform.rotate(carimage, 225)
        #Getting that nos working!!!
        if pressed[pygame.K_SPACE]:
            if nosleft >= 1:
                nosleft -= 1
                topspeed += 0.2
                nosinuse = True
            else:
               nosinuse = False
               if topspeed >= cartopspeed:
                   topspeed -= 0.1
               if not nosinuse:
                   if nosleft <= mostnos:
                       nosleft += 0.1
        if not pressed[pygame.K_SPACE]:
            nosinuse = False
            if topspeed >= cartopspeed:
                topspeed -= 0.1
            if not nosinuse:
                if nosleft <= mostnos:
                    nosleft += 0.1
        if not pressed[pygame.K_RIGHT]:
            if not pressed[pygame.K_LEFT]:
                if not pressed[pygame.K_DOWN]:
                    if not pressed[pygame.K_UP]:
                        if not pressed[pygame.K_SPACE]:
                            if curspeed >= 0.19:
                                curspeed = curspeed - 0.1
        #Collision/OOB detection
        if x >=1270:
            x = 1268
        if x <= -1:
            x = 2
        if y >= 710:
            y = 708
        if y <= -1:
            y = 2
        #Setting Up the label
        laplabel = lap + str(lapcount)
        lapl = font.render(laplabel, 10 ,black)
        nosleftround = round(nosleft, 1)
        noslabel = "Nos Left: " + str(nosleftround)
        nosl = font.render(noslabel, 30, black)
        currentlabel = "Speed: " + str(round(curspeed, 2))
        curspeedl = font.render(currentlabel, 30, black)
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(nosl, (10, 10))
        screen.blit(lapl, (10, 40))
        screen.blit(curspeedl, (10, 70))
        screen.blit(carimage2, (x,y))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
