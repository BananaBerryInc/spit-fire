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
score = 0
Up = "Up"
Down = "Down"
Left = "Left"
Right = "Right"
LeftUp = "LeftUp"
LeftDown = "LeftDown"
RightUp = "RightUp"
RightDown = "RightDown"
lastdirection = Down


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
braking = int(carbrake) / 500 * aero
accel = int(caraccel) / 300 * aero
handling = int(carhandling) / 30 * aero
righthandling = 360 - handling
curspeed = 0
startlinex = int(startx)
startliney = int(starty)
checky = int(checkpointy)
checkx = int(checkpointx)
checkplus40x = checkx + 40
checkminus40x = checkx - 40
checkplus40y = checkx + 40
checkminus40y = checkx - 40
x = startliney
y = startlinex
startneg80x = startlinex - 80
start80x = startlinex + 80
passstart = startliney + 10
carimage2 = pygame.transform.rotate(carimage, 180)
rotater = 0

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
                            score += 2000
                            lapcount += 1
                            newlap = True
        if newlap == True:
            laptime += 1
            if laptime >= 150:
                newlap = False
                laptime = 0
        if pressed[pygame.K_UP]:
            curspeed = curspeed + accel
            lastdirection = Up
            if curspeed >= topspeed:
                curspeed = topspeed
            #UP
            if rotater >= 340:
                ynow = y
                y = ynow - curspeed
            #Up
            if rotater <= 30:
                ynow = y
                y = ynow - curspeed
            #LeftUp
            if rotater >= 30:
                if rotater <= 70:
                    xnow = x
                    x = xnow - curspeed
                    ynow = y
                    y = ynow - curspeed
            #Left
            if rotater >= 70:
                if rotater <= 110:
                    xnow = x
                    x = xnow - curspeed
            #LeftDown
            if rotater >= 110:
                if rotater <= 140:
                    xnow = x
                    x = xnow - curspeed
                    ynow = y
                    y = ynow + curspeed
            #Down
            if rotater >= 140:
                if rotater <= 210:
                    ynow = y
                    y = ynow + curspeed
            #RightDown
            if rotater >= 210:
                if rotater <= 250:
                    xnow = x
                    x = xnow + curspeed
            #Right
            if rotater >= 250:
                if rotater <= 300:
                    ynow = y
                    y = ynow + curspeed
                    xnow = x
                    x = xnow + curspeed
            #RightUp
            if rotater >= 300:
                if rotater <= 340:
                    ynow = y
                    y = ynow - curspeed
                    xnow = x
                    x = xnow + curspeed
        if pressed[pygame.K_DOWN]:
            curspeed = curspeed + accel
            lastdirection = Down
            if curspeed >= topspeed:
                curspeed = topspeed
            carimage2 = pygame.transform.rotate(carimage, 180)
        if pressed[pygame.K_LEFT]:
            lastdirection = Left
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            rotater += handling
            if rotater >= 360:
                rotater = 0
            if rotater <= 0:
                rotater = 0
            carimage2 = pygame.transform.rotate(carimage, rotater)
            if pressed[pygame.K_UP]:
                lastdirection = LeftUp
            if pressed[pygame.K_DOWN]:
                lastdirection = LeftDown
        if pressed[pygame.K_RIGHT]:
            lastdirection = Right
            curspeed = curspeed + accel
            if curspeed >= topspeed:
                curspeed = topspeed
            rotater -= handling
            if rotater >= 360:
                rotater = 0
            if rotater <= 0:
                rotater = 360
            carimage2 = pygame.transform.rotate(carimage, rotater)
            if pressed[pygame.K_UP]:
                lastdirection = RightUp
            if pressed[pygame.K_DOWN]:
                lastdirection = RightDown
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
        if pressed[pygame.K_b]:
            curspeed = curspeed - braking
            if curspeed >= 0.19:
                curspeed = curspeed - 0.1
            else:
                curspeed = 0
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
                            else:
                                curspeed = 0
                            if lastdirection == LeftUp:
                                ynow = y
                                y = ynow - curspeed
                                xnow = x
                                x = xnow - curspeed
                            if lastdirection == RightDown:
                                ynow = y
                                y = ynow + curspeed
                                xnow = x
                                x = xnow + curspeed
                            if lastdirection == LeftDown:
                                xnow = x
                                x = xnow - curspeed
                                ynow = y
                                y = ynow + curspeed
                            if lastdirection == RightUp:
                                xnow = x
                                x = xnow + curspeed
                                ynow = y
                                y = ynow - curspeed
                            if lastdirection == Up:
                                ynow = y
                                y = ynow - curspeed
                            if lastdirection == Down:
                                ynow = y
                                y = ynow + curspeed
                            if lastdirection == Left:
                                xnow = x
                                x = xnow - curspeed
                            if lastdirection ==  Right:
                                xnow = x
                                x = xnow + curspeed
        #movement
        #Collision/OOB detection
        if x >=1270:
            x = 1268
        if x <= -1:
            x = 2
        if y >= 710:
            y = 708
        if y <= -1:
            y = 2
        score -= 1
        #Setting Up the label
        laplabel = lap + str(lapcount)
        lapl = font.render(laplabel, 10 ,black)
        nosleftround = round(nosleft, 1)
        noslabel = "Nos Left: " + str(nosleftround)
        nosl = font.render(noslabel, 30, black)
        scorelabel = "Score: " + str(round(score, 1))
        scorel = font.render(scorelabel, 30 , black)
        currentlabel = "Speed: " + str(round(curspeed, 2))
        curspeedl = font.render(currentlabel, 30, black)
        #Drawing and rendering
        screen.blit(trackimage, (0,0))
        screen.blit(scorel, (10, 100))
        screen.blit(nosl, (10, 10))
        screen.blit(lapl, (10, 40))
        screen.blit(curspeedl, (10, 70))
        screen.blit(carimage2, (x,y))
        print(rotater)
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
