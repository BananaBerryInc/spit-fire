# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess
from configparser import SafeConfigParser
from PIL import Image

#Settin' up the window!
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("freesansbold.ttf", 30)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 1")
pygame.display.flip()

#Re-collecting those settings!
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
carimagepath2 = parser.get("options", "carimage2")
trackstring = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
players = parser.get("options", "players")
trackimage = pygame.image.load(trackpath)
track = int(trackstring)
trackkey = "track" + str(track)
car = parser.get("options", "car")
car2 = parser.get("options", "car2")
clockspeedstring = parser.get("options", "speed")
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
tim = Image.open(trackpath)
trackpil = tim.load()

#Variables
carimage = pygame.image.load(carimagepath)
carimage3 = pygame.image.load(carimagepath2)
clock = pygame.time.Clock()
x = 30
y = 30
nos = 0
nosinuse = False
nosinuse2 = False
lap = "Lap: "
lapcount = 0
place = 11
atstart = True
atstart2 = True
newlap = False
newlap2 = False
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
finished = False


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

#Get all stats from the ini files
parser.read("res/carstats.ini")
carspeed = parser.get(car, "speed")
caraccel = parser.get(car, "accel")
carbrake = parser.get(car, "brake")
carhandling = parser.get(car, "handling")
carbrake = parser.get(car, "brake")
caraero = parser.get(car, "aero")
carnos = parser.get(car, "nos")
carspeed2 = parser.get(car2, "speed")
caraccel2 = parser.get(car2, "accel")
carbrake2 = parser.get(car2, "brake")
carhandling2 = parser.get(car2, "handling")
carbrake2 = parser.get(car2, "brake")
caraero2 = parser.get(car2, "aero")
carnos2 = parser.get(car2, "nos")
parser.read("res/tracks.ini")
maxlap = int(parser.get(trackkey, "laps"))
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")
parser.read("res/highscore.ini")
p1 = int(parser.get(trackkey, "1"))
p2 = int(parser.get(trackkey, "2"))
p3 = int(parser.get(trackkey, "3"))
p4 = int(parser.get(trackkey, "4"))
p5 = int(parser.get(trackkey, "5"))
p6 = int(parser.get(trackkey, "6"))
p7 = int(parser.get(trackkey, "7"))
p8 = int(parser.get(trackkey, "8"))
p9 = int(parser.get(trackkey, "9"))
p10 = parser.get(trackkey, "10")
p10 = int(p10)
pixcoloour = (0,0,0)

#More Variables!!!!
mostnos = int(carnos)
nosleft = int(carnos)
aero = int(caraero) / 10
cartopspeed = int(carspeed) / 18 * aero
topspeed = int(carspeed) / 18 * aero
braking = int(carbrake) / 500 * aero
accel = int(caraccel) / 2100 * aero
handling = int(carhandling) / 30 * aero
righthandling = 360 - handling
mostnos2 = int(carnos2)
nosleft2 = int(carnos2)
aero2 = int(caraero2) / 10
cartopspeed2 = int(carspeed2) / 18 * aero2
topspeed2 = int(carspeed2) / 18 * aero2
braking2 = int(carbrake2) / 500 * aero2
accel2 = int(caraccel2) / 2100 * aero2
handling2 = int(carhandling2) / 30 * aero2
righthandling2 = 360 - handling2
curspeed = 0
startlinex = int(startx)
startliney = int(starty)
checky = int(checkpointy)
checkx = int(checkpointx)
checkplus40x = checkx + 80
checkminus40x = checkx - 80
checkplus40y = checky + 80
checkminus40y = checky - 80
x = startliney
y = startlinex
x2 = startliney
y2 = startlinex
startneg80x = startlinex - 80
start80x = startlinex + 80
passstart = startliney + 10
rotater = 0
rotater2 = 0
carimage2 = pygame.transform.rotate(carimage, 0)
carimage4 = pygame.transform.rotate(carimage3, 0)
if trackkey == "track3" :
    carimage2 = pygame.transform.rotate(carimage, 90)
    rotater = 90
    passstart = startlinex - 10
pos = 0
togo = 0
maxlaps = maxlap + 1
score = 0
pos2 = 0
togo2 = 0
maxlaps2 = maxlap + 1
score2 = 0
trackkey2 = trackkey
curspeed2 = 0
#Passoff to the postrace Python script
def sendtopost():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global score
    global place
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "racefinsihed", "Yes")
    parser.set("options", "score", str(score))
    parser.set("options", "place", str(place))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("prepostrace.py").read())

#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Key Detection
        if players == "2":
            pressed = pygame.key.get_pressed()
            pixcoloour = trackpil[x2,y2]
            print(rotater2)
            if not nosinuse2:
                if pixcoloour == (0, 0, 0, 255):
                    topspeed2 = int(carspeed2) / 18 * aero2
                else:
                    topspeed2 = int(carspeed2) / 25 * aero2
                if pixcoloour == (2, 2, 2, 255):
                    topspeed2 = int(carspeed2) / 18 * aero2
            if atstart2:
                if y2 >= passstart:
                    atstart2 = False
                if trackkey2 == "track3":
                    if x2 <= passstart:
                        atstart2 = False
            if not atstart2:
                if not newlap:
                    if y2 >= startneg80x:
                        if y2 <= start80x:
                            if x2 <= startliney:
                                score2 += 2000
                                lapcount += 1
                                newlap = True
                                atstart2 = False
            if not atstart2:
                laptime += 1
                if y2 >= checkminus40y:
                    if y2 <= checkplus40y:
                        if x2 <= checkplus40x:
                            if x2 >= checkminus40x:
                                atstart2 = False
                                newlap = False
                                laptime = 0
            if pressed[pygame.K_ESCAPE]:
                pygame.QUIT
                quit()
            if pressed[pygame.K_w]:
                curspeed2 = curspeed2 + accel
                lastdirection = Up
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                segment =  0
                segmentneg =  0
                segspeed2 = 0
                amount = 0
                rot2 = 0
                if rotater2 <= 90:
                    xnow = x2
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
                if rotater2 >= 90:
                    if rotater2 <= 180:
                        xnow = x2
                        rot2 = 180 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                if rotater2 >= 90.01:
                    if rotater2 <= 180:
                        ynow = y2
                        rot2 = rotater2 - 90
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        ynow = y2
                        rot2 = 270 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        xnow = x2
                        rot2 = rotater2 - 180
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        xnow = x2
                        rot2 = rotater2 - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        ynow = y2
                        rot2 = rotater2 - 270
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 <= 89.9:
                    ynow = y2
                    rot2 = -90 + rotater2
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if pressed[pygame.K_a]:
                lastdirection = Left
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                rotater2 += handling2
                if not pressed [pygame.K_w]:
                    if rotater2 <= 90:
                        xnow = x2
                        if rot2 <= 0:
                            amount = 0
                        if rot2 >= 0:
                            amount = rotater2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                    if rotater2 >= 90:
                        if rotater2 <= 180:
                            xnow = x2
                            rot2 = 180 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow - segspeed2
                    if rotater2 >= 90.01:
                        if rotater2 <= 180:
                            ynow = y2
                            rot2 = rotater2 - 90
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            ynow = y2
                            rot2 = 270 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            xnow = x2
                            rot2 = rotater2 - 180
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 359.9:
                            xnow = x2
                            rot2 = rotater2 - 270
                            rot3 = -90 + rot2
                            if rot3 >= 0:
                                amount = 1
                            if rot3 <= 0:
                                amount = rot3 / -90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            ynow = y2
                            rot2 = rotater2 - 270
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow - segspeed2
                    if rotater2 <= 89.9:
                        ynow = y2
                        rot2 = -90 + rotater2
                        if rot2 >= 0:
                            amount = 1
                        if rot2 <= 0:
                            amount = rot2 / -90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 >= 360:
                    rotater2 = 0
                if rotater2 <= 0:
                    rotater2 = 0
                carimage4 = pygame.transform.rotate(carimage3, rotater2)
                if pressed[pygame.K_w]:
                    lastdirection = LeftUp
                if pressed[pygame.K_s]:
                    lastdirection = LeftDown
            if pressed[pygame.K_d]:
                lastdirection = Right
                if not pressed [pygame.K_w]:
                    if rotater2 <= 90:
                        xnow = x2
                        if rot2 <= 0:
                            amount = 0
                        if rot2 >= 0:
                            amount = rotater2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                    if rotater2 >= 90:
                        if rotater2 <= 180:
                            xnow = x2
                            rot2 = 180 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow - segspeed2
                    if rotater2 >= 90.01:
                        if rotater2 <= 180:
                            ynow = y2
                            rot2 = rotater2 - 90
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            ynow = y2
                            rot2 = 270 - rotater2
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow + segspeed2
                    if rotater2 >= 180:
                        if rotater2 <= 270:
                            xnow = x2
                            rot2 = rotater2 - 180
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            xnow = x2
                            rot2 = rotater2 - 270
                            rot3 = -90 + rot2
                            if rot3 >= 0:
                                amount = 1
                            if rot3 <= 0:
                                amount = rot3 / -90
                            segspeed2 = amount * curspeed2
                            x2 = xnow + segspeed2
                    if rotater2 >= 270:
                        if rotater2 <= 360:
                            ynow = y2
                            rot2 = rotater2 - 270
                            amount = rot2 / 90
                            segspeed2 = amount * curspeed2
                            y2 = ynow - segspeed2
                    if rotater2 <= 89.9:
                        ynow = y2
                        rot2 = -90 + rotater2
                        if rot2 >= 0:
                            amount = 1
                        if rot2 <= 0:
                            amount = rot2 / -90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if curspeed2 >= topspeed2:
                    curspeed2 = topspeed2
                rotater2 -= handling2
                if rotater2 >= 360:
                    rotater2 = 0
                if rotater2 <= 0:
                    rotater2 = 360
                carimage4 = pygame.transform.rotate(carimage3, rotater2)
                if pressed[pygame.K_w]:
                    lastdirection = RightUp
                if pressed[pygame.K_s]:
                    lastdirection = RightDown
            #Getting that nos working!!!
            if pressed[pygame.K_LSHIFT]:
                if nosleft >= 1:
                    nosleft -= 1
                    topspeed2 += 0.2
                    nosinuse2 = True
                else:
                   nosinuse2 = False
                   if topspeed2 >= cartopspeed2:
                       topspeed2 -= 0.1
                   if not nosinuse2:
                       if nosleft <= mostnos:
                           nosleft += 0.1
            if pressed[pygame.K_s]:
                curspeed2 = curspeed2 - braking
                if curspeed2 >= -1.6:
                    curspeed2 = curspeed2 - 0.1
                else:
                    curspeed2 = -1.5
                segment =  0
                segmentneg =  0
                segspeed2 = 0
                amount = 0
                rot2 = 0
                if rotater2 <= 90:
                    xnow = x2
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater2 / 90
                    segspeed2 = amount * curspeed2
                    x2 = xnow - segspeed2
                if rotater2 >= 90:
                    if rotater2 <= 180:
                        xnow = x2
                        rot2 = 180 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow - segspeed2
                if rotater2 >= 90.01:
                    if rotater2 <= 180:
                        ynow = y2
                        rot2 = rotater2 - 90
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        ynow = y2
                        rot2 = 270 - rotater2
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow + segspeed2
                if rotater2 >= 180:
                    if rotater2 <= 270:
                        xnow = x2
                        rot2 = rotater2 - 180
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        xnow = x2
                        rot2 = rotater2 - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed2 = amount * curspeed2
                        x2 = xnow + segspeed2
                if rotater2 >= 270:
                    if rotater2 <= 360:
                        ynow = y2
                        rot2 = rotater2 - 270
                        amount = rot2 / 90
                        segspeed2 = amount * curspeed2
                        y2 = ynow - segspeed2
                if rotater2 <= 89.9:
                    ynow = y2
                    rot2 = -90 + rotater2
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed2 = amount * curspeed2
                    y2 = ynow - segspeed2
            if not pressed[pygame.K_SPACE]:
                nosinuse2 = False
                if topspeed2 >= cartopspeed2:
                    topspeed2 -= 0.1
                if not nosinuse2:
                    if nosleft <= mostnos:
                        nosleft += 0.1
            if not pressed[pygame.K_d]:
                if not pressed[pygame.K_a]:
                    if not pressed[pygame.K_s]:
                        if not pressed[pygame.K_w]:
                            if not pressed[pygame.K_LSHIFT]:
                                if curspeed2 >= 0.19:
                                    curspeed2 = curspeed2 - 0.1
                                if curspeed2 <= -0.1:
                                    curspeed2 = curspeed2 + 0.1
                                if curspeed2 >= -0.1:
                                    if curspeed2 <= 0.19:
                                        curspeed2 = 0
                                segment =  0
                                segmentneg =  0
                                segspeed2 = 0
                                amount = 0
                                rot2 = 0
                                if rotater2 <= 90:
                                    xnow = x2
                                    if rot2 <= 0:
                                        amount = 0
                                    if rot2 >= 0:
                                        amount = rotater2 / 90
                                    segspeed2 = amount * curspeed2
                                    x2 = xnow - segspeed2
                                if rotater2 >= 90:
                                    if rotater2 <= 180:
                                        xnow = x2
                                        rot2 = 180 - rotater2
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow - segspeed2
                                if rotater2 >= 90.01:
                                    if rotater2 <= 180:
                                        ynow = y2
                                        rot2 = rotater2 - 90
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2

                                        y2 = ynow + segspeed2
                                if rotater2 >= 180:
                                    if rotater2 <= 270:
                                        ynow = y2
                                        rot2 = 270 - rotater2
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        y2 = ynow + segspeed2
                                if rotater2 >= 180:
                                    if rotater2 <= 270:
                                        xnow = x2
                                        rot2 = rotater2 - 180
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow + segspeed2
                                if rotater2 >= 270:
                                    if rotater2 <= 360:
                                        xnow = x2
                                        rot2 = rotater2 - 270
                                        rot3 = -90 + rot2
                                        if rot3 >= 0:
                                            amount = 1
                                        if rot3 <= 0:
                                            amount = rot3 / -90
                                        segspeed2 = amount * curspeed2
                                        x2 = xnow + segspeed2
                                if rotater2 >= 270:
                                    if rotater2 <= 360:
                                        ynow = y2
                                        rot2 = rotater2 - 270
                                        amount = rot2 / 90
                                        segspeed2 = amount * curspeed2
                                        y2 = ynow - segspeed2
                                if rotater2 <= 89.9:
                                    ynow = y2
                                    rot2 = -90 + rotater2
                                    if rot2 >= 0:
                                        amount = 1
                                    if rot2 <= 0:
                                        amount = rot2 / -90
                                    segspeed2 = amount * curspeed2
                                    y2 = ynow - segspeed2
            #movement
            #Collision/OOB detection
            if x2 >=1270:
                x2 = 1268
            if x2 <= -1:
                x2 = 2
            if y2 >= 710:
                y2 = 708
            if y2 <= -1:
                y2 = 2
            score2 -= 1
        pressed = pygame.key.get_pressed()
        pixcoloour = trackpil[x,y]
        print(rotater)
        if not nosinuse:
            if pixcoloour == (0, 0, 0, 255):
                topspeed = int(carspeed) / 18 * aero
            else:
                topspeed = int(carspeed) / 25 * aero
            if pixcoloour == (2, 2, 2, 255):
                topspeed = int(carspeed) / 18 * aero
        if atstart:
            if y >= passstart:
                atstart = False
            if trackkey == "track3":
                if x <= passstart:
                    atstart = False
        if not atstart:
            if not newlap:
                if y >= startneg80x:
                    if y <= start80x:
                        if x <= startliney:
                            score += 2000
                            lapcount += 1
                            newlap = True
                            atstart = False
        if not atstart:
            laptime += 1
            if y >= checkminus40y:
                if y <= checkplus40y:
                    if x <= checkplus40x:
                        if x >= checkminus40x:
                            atstart = False
                            newlap = False
                            laptime = 0
        if pressed[pygame.K_ESCAPE]:
            pygame.QUIT
            quit()
        if pressed[pygame.K_UP]:
            curspeed = curspeed + accel
            lastdirection = Up
            if curspeed >= topspeed:
                curspeed = topspeed
            segment =  0
            segmentneg =  0
            segspeed = 0
            amount = 0
            rot2 = 0
            if rotater <= 90:
                xnow = x
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater / 90
                segspeed = amount * curspeed
                x = xnow - segspeed
            if rotater >= 90:
                if rotater <= 180:
                    xnow = x
                    rot2 = 180 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
            if rotater >= 90.01:
                if rotater <= 180:
                    ynow = y
                    rot2 = rotater - 90
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    ynow = y
                    rot2 = 270 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    xnow = x
                    rot2 = rotater - 180
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    xnow = x
                    rot2 = rotater - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    ynow = y
                    rot2 = rotater - 270
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if rotater <= 89.9:
                ynow = y
                rot2 = -90 + rotater
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed = amount * curspeed
                y = ynow - segspeed
        if pressed[pygame.K_LEFT]:
            lastdirection = Left
            if curspeed >= topspeed:
                curspeed = topspeed
            rotater += handling
            if not pressed [pygame.K_UP]:
                if rotater <= 90:
                    xnow = x
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
                if rotater >= 90:
                    if rotater <= 180:
                        xnow = x
                        rot2 = 180 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow - segspeed
                if rotater >= 90.01:
                    if rotater <= 180:
                        ynow = y
                        rot2 = rotater - 90
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        ynow = y
                        rot2 = 270 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        xnow = x
                        rot2 = rotater - 180
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 359.9:
                        xnow = x
                        rot2 = rotater - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        ynow = y
                        rot2 = rotater - 270
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow - segspeed
                if rotater <= 89.9:
                    ynow = y
                    rot2 = -90 + rotater
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
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
            if not pressed [pygame.K_UP]:
                if rotater <= 90:
                    xnow = x
                    if rot2 <= 0:
                        amount = 0
                    if rot2 >= 0:
                        amount = rotater / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
                if rotater >= 90:
                    if rotater <= 180:
                        xnow = x
                        rot2 = 180 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow - segspeed
                if rotater >= 90.01:
                    if rotater <= 180:
                        ynow = y
                        rot2 = rotater - 90
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        ynow = y
                        rot2 = 270 - rotater
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow + segspeed
                if rotater >= 180:
                    if rotater <= 270:
                        xnow = x
                        rot2 = rotater - 180
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        xnow = x
                        rot2 = rotater - 270
                        rot3 = -90 + rot2
                        if rot3 >= 0:
                            amount = 1
                        if rot3 <= 0:
                            amount = rot3 / -90
                        segspeed = amount * curspeed
                        x = xnow + segspeed
                if rotater >= 270:
                    if rotater <= 360:
                        ynow = y
                        rot2 = rotater - 270
                        amount = rot2 / 90
                        segspeed = amount * curspeed
                        y = ynow - segspeed
                if rotater <= 89.9:
                    ynow = y
                    rot2 = -90 + rotater
                    if rot2 >= 0:
                        amount = 1
                    if rot2 <= 0:
                        amount = rot2 / -90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
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
        if pressed[pygame.K_DOWN]:
            curspeed = curspeed - braking
            if curspeed >= -1.6:
                curspeed = curspeed - 0.1
            else:
                curspeed = -1.5
            segment =  0
            segmentneg =  0
            segspeed = 0
            amount = 0
            rot2 = 0
            if rotater <= 90:
                xnow = x
                if rot2 <= 0:
                    amount = 0
                if rot2 >= 0:
                    amount = rotater / 90
                segspeed = amount * curspeed
                x = xnow - segspeed
            if rotater >= 90:
                if rotater <= 180:
                    xnow = x
                    rot2 = 180 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow - segspeed
            if rotater >= 90.01:
                if rotater <= 180:
                    ynow = y
                    rot2 = rotater - 90
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    ynow = y
                    rot2 = 270 - rotater
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow + segspeed
            if rotater >= 180:
                if rotater <= 270:
                    xnow = x
                    rot2 = rotater - 180
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    xnow = x
                    rot2 = rotater - 270
                    rot3 = -90 + rot2
                    if rot3 >= 0:
                        amount = 1
                    if rot3 <= 0:
                        amount = rot3 / -90
                    segspeed = amount * curspeed
                    x = xnow + segspeed
            if rotater >= 270:
                if rotater <= 360:
                    ynow = y
                    rot2 = rotater - 270
                    amount = rot2 / 90
                    segspeed = amount * curspeed
                    y = ynow - segspeed
            if rotater <= 89.9:
                ynow = y
                rot2 = -90 + rotater
                if rot2 >= 0:
                    amount = 1
                if rot2 <= 0:
                    amount = rot2 / -90
                segspeed = amount * curspeed
                y = ynow - segspeed
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
                            if curspeed <= -0.1:
                                curspeed = curspeed + 0.1
                            if curspeed >= -0.1:
                                if curspeed <= 0.19:
                                    curspeed = 0
                            segment =  0
                            segmentneg =  0
                            segspeed = 0
                            amount = 0
                            rot2 = 0
                            if rotater <= 90:
                                xnow = x
                                if rot2 <= 0:
                                    amount = 0
                                if rot2 >= 0:
                                    amount = rotater / 90
                                segspeed = amount * curspeed
                                x = xnow - segspeed
                            if rotater >= 90:
                                if rotater <= 180:
                                    xnow = x
                                    rot2 = 180 - rotater
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    x = xnow - segspeed
                            if rotater >= 90.01:
                                if rotater <= 180:
                                    ynow = y
                                    rot2 = rotater - 90
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed

                                    y = ynow + segspeed
                            if rotater >= 180:
                                if rotater <= 270:
                                    ynow = y
                                    rot2 = 270 - rotater
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    y = ynow + segspeed
                            if rotater >= 180:
                                if rotater <= 270:
                                    xnow = x
                                    rot2 = rotater - 180
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    x = xnow + segspeed
                            if rotater >= 270:
                                if rotater <= 360:
                                    xnow = x
                                    rot2 = rotater - 270
                                    rot3 = -90 + rot2
                                    if rot3 >= 0:
                                        amount = 1
                                    if rot3 <= 0:
                                        amount = rot3 / -90
                                    segspeed = amount * curspeed
                                    x = xnow + segspeed
                            if rotater >= 270:
                                if rotater <= 360:
                                    ynow = y
                                    rot2 = rotater - 270
                                    amount = rot2 / 90
                                    segspeed = amount * curspeed
                                    y = ynow - segspeed
                            if rotater <= 89.9:
                                ynow = y
                                rot2 = -90 + rotater
                                if rot2 >= 0:
                                    amount = 1
                                if rot2 <= 0:
                                    amount = rot2 / -90
                                segspeed = amount * curspeed
                                y = ynow - segspeed
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
        #Getting the placing
        if score <= p10:
            place = 11
            togo = p10 - score
        if score >= p10:
            place = 10
            togo = p10 - score
        if score >= p9:
            place = 9
            togo = p10 - score
        if score >= p8:
            place = 8
            togo = p10 - score
        if score >= p7:
            place = 7
            togo = p10 - score
        if score >= p6:
            place = 6
            togo = p10 - score
        if score >= p5:
            place = 5
            togo = p10 - score
        if score >= p4:
            place = 4
            togo = p10 - score
        if score >= p3:
            place = 3
            togo = p10 - score
        if score >= p2:
            place = 2
            togo = p10 - score
        if score >= p1:
            place = 1
            togo = p10 - score
        #Finishing!
        if lapcount >= maxlaps:
            #PAssoff scfript here
            finished = True
            sendtopost()
        #Setting Up the labels
        laplabel = lap + str(lapcount) + "/" + str(maxlap)
        lapl = font.render(laplabel, 10 ,black)
        nosleftround = round(nosleft, 1)
        noslabel = "Nos Left: " + str(nosleftround)
        nosl = font.render(noslabel, 30, black)
        scorelabel = "Score: " + str(round(score, 1))
        scorel = font.render(scorelabel, 30 , black)
        speedlabel = curspeed * 41
        currentlabel = "Speed: " + str(round(speedlabel, 2)) + " Km/h"
        curspeedl = font.render(currentlabel, 30, black)
        placelabel = "Place: " + str(place)
        placel = font.render(placelabel, 30, black)
        donelabel = "Finsihed!  ANd more because this is cool!"
        donel = font.render(donelabel, 30, black)
        #Drawing and rendering
        print(amount)
        screen.blit(trackimage, (0,0))
        screen.blit(placel, (10, 130))
        screen.blit(scorel, (10, 100))
        screen.blit(nosl, (10, 10))
        screen.blit(lapl, (10, 40))
        screen.blit(curspeedl, (10, 70))
        screen.blit(carimage2, (x,y))
        if players == "2":
            screen.blit(carimage4, (x2,y2))
        if finished:
            screen.blit(donel, (620, 340))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
