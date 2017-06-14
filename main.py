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
font50 = pygame.font.SysFont("freesansbold.ttf", 50)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 2")
pygame.display.flip()

#Variables
clock = pygame.time.Clock()
x = 30
y = 30
x2 = 60
y2 = 60
players = 1
inhelp = False
currentcar2 = "ford_gt"
carimagepath2 = "res/ford_gt.png"
carimage2 = pygame.image.load("res/ford_gt.png")
parser = SafeConfigParser()
parser.read("res/options.ini")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
level = parser.get("options", "level")
points = parser.get("options", "points")
level = int(level)
levelpoints = (int(level) + 100) * 202.2
levelpoints = round(levelpoints, 1)
levelpixels = float(points) / levelpoints * 300
carimage = pygame.image.load("res/ford_gt.png")
carimage2 = pygame.image.load("res/ford_gt.png")
carimagepath = "res/ford_gt.png"
currentcar = "ford_gt"
cartext = "Car: "
track = 1
trackname = "First_track"
clockspeed = 100
change = 0
carimage3 = carimage
carimage4 = carimage
parser = SafeConfigParser()
parser.read("res/tracks.ini")
trackname = parser.get("track1", "trackname")
trackpath = parser.get("track1", "trackpath")
logo = pygame.image.load("res/Game Logo.png")


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


#Labels that don't change will go here
label = font.render("Exit", 1, white)
labelstart = font.render("Start the Race!", 10, white)

#Passoff to the main python script
def sendtomain():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global levelpoints
    global players
    global car2
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "track", str(track))
    parser.set("options", "car", currentcar)
    parser.set("options", "car2", currentcar2)
    parser.set("options", "trackpath", trackpath)
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "carimage2", carimagepath2)
    parser.set("options", "speed", str(clockspeed))
    parser.set("options", "racefinsihed", "No")
    parser.set("options", "fulscr", str(fulscr))
    parser.set("options", "levelpoints", str(levelpoints))
    parser.set("options", "players", str(players))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("race.py").read())


#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Mainloop...?
        #Key detection!
        pressed = pygame.key.get_pressed()
        #Movement
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
        if pressed[pygame.K_w]:
            y2 -= 3
            carimage4 = carimage3
        if pressed[pygame.K_s]:
            y2 += 3
            carimage4 = pygame.transform.rotate(carimage3, 180)
        if pressed[pygame.K_a]:
            x2 -= 3
            carimage4 = pygame.transform.rotate(carimage3, 90)
            if pressed[pygame.K_w]:
                carimage4 = pygame.transform.rotate(carimage3, 45)
            if pressed[pygame.K_s]:
                carimage4 = pygame.transform.rotate(carimage3, 135)
        if pressed[pygame.K_d]:
            x2 += 3
            carimage4 = pygame.transform.rotate(carimage3, 270)
            if pressed[pygame.K_w]:
                carimage4 = pygame.transform.rotate(carimage3, 315)
            if pressed[pygame.K_s]:
                carimage4 = pygame.transform.rotate(carimage3, 225)
        #Change Cars
        if pressed[pygame.K_ESCAPE]:
            inhelp = False
        if pressed[pygame.K_c]:
            if currentcar == "Dodge_Challenger":
                if change == 0:
                    if level >= 4:
                        currentcar = "Koenigsegg_One"
                        carimagepath = "res/Koenigsegg_One.png"
                        carimage = pygame.image.load("res/Koenigsegg_One.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Ferrari_F40":
                if change == 0:
                    if level >= 5:
                        currentcar = "Dodge_Challenger"
                        carimagepath = "res/Dodge_Challenger.png"
                        carimage = pygame.image.load("res/Dodge_Challenger.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "ford_gt":
                if change == 0:
                    if level >= 2:
                        currentcar = "Ferrari_F40"
                        carimagepath = "res/Ferrari_F40.png"
                        carimage = pygame.image.load("res/Ferrari_F40.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Koenigsegg_One":
                if change == 0:
                    if level >= 6:
                        currentcar = "Bugatti Vision GT Gran Turismo"
                        carimagepath = "res/Bugatti Vision GT Gran Turismo.png"
                        carimage = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Bugatti Vision GT Gran Turismo":
                if change == 0:
                    if level >= 7:
                        currentcar = "Camaro ZL1 1LE"
                        carimagepath = "res/Camaro ZL1 1LE.png"
                        carimage = pygame.image.load("res/Camaro ZL1 1LE.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Camaro ZL1 1LE":
                if change == 0:
                    if level >= 8:
                        currentcar = "Mclaren P1"
                        carimagepath = "res/Mclaren P1.png"
                        carimage = pygame.image.load("res/Mclaren P1.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Mclaren P1":
                if change == 0:
                    if level >= 9:
                        currentcar = "Nissan 240SX"
                        carimagepath = "res/Nissan 240SX.png"
                        carimage = pygame.image.load("res/Nissan 240SX.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nissan 240SX":
                if change == 0:
                    if level >= 10:
                        currentcar = "Nissan GTR R35"
                        carimagepath = "res/Nissan GTR R35.png"
                        carimage = pygame.image.load("res/Nissan GTR R35.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nissan GTR R35":
                if change == 0:
                    if level >= 11:
                        currentcar = "Porsche 918"
                        carimagepath = "res/Porsche 918.png"
                        carimage = pygame.image.load("res/Porsche 918.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Porsche 918":
                if change == 0:
                    if level >= 12:
                        currentcar = "Nitro Cart"
                        carimagepath = "res/Nitro Cart.png"
                        carimage = pygame.image.load("res/Nitro Cart.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nitro Cart":
                if change == 0:
                    if level >= 13:
                        currentcar = "Limited Gold Koenigsegg One"
                        carimagepath = "res/Limited Gold Koenigsegg One.png"
                        carimage = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Limited Gold Koenigsegg One":
                if change == 0:
                    if level >= 16:
                        currentcar = "Toyota Supra"
                        carimagepath = "res/Toyota Supra.png"
                        carimage = pygame.image.load("res/Toyota Supra.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Toyota Supra":
                if change == 0:
                    if level >= 17:
                        currentcar = "WMotors Fenyr SuperSport"
                        carimagepath = "res/WMotors Fenyr SuperSport.png"
                        carimage = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                        change = 10
                    else:
                        currentcar = "ford_gt"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "WMotors Fenyr SuperSport":
                if change == 0:
                    currentcar = "ford_gt"
                    carimagepath = "res/ford_gt.png"
                    carimage = pygame.image.load("res/ford_gt.png")
                    change = 10
        if players == 2:
            if pressed[pygame.K_v]:
                if currentcar2 == "Dodge_Challenger":
                    if change == 0:
                        if level >= 4:
                            currentcar2 = "Koenigsegg_One"
                            carimagepath2 = "res/Koenigsegg_One.png"
                            carimage4 = pygame.image.load("res/Koenigsegg_One.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Ferrari_F40":
                    if change == 0:
                        if level >= 5:
                            currentcar2 = "Dodge_Challenger"
                            carimagepath2 = "res/Dodge_Challenger.png"
                            carimage4 = pygame.image.load("res/Dodge_Challenger.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "ford_gt":
                    if change == 0:
                        if level >= 2:
                            currentcar2 = "Ferrari_F40"
                            carimagepath2 = "res/Ferrari_F40.png"
                            carimage4 = pygame.image.load("res/Ferrari_F40.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Koenigsegg_One":
                    if change == 0:
                        if level >= 6:
                            currentcar2 = "Bugatti Vision GT Gran Turismo"
                            carimagepath2 = "res/Bugatti Vision GT Gran Turismo.png"
                            carimage4 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Bugatti Vision GT Gran Turismo":
                    if change == 0:
                        if level >= 7:
                            currentcar2 = "Camaro ZL1 1LE"
                            carimagepath2 = "res/Camaro ZL1 1LE.png"
                            carimage4 = pygame.image.load("res/Camaro ZL1 1LE.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Camaro ZL1 1LE":
                    if change == 0:
                        if level >= 8:
                            currentcar2 = "Mclaren P1"
                            carimagepath2 = "res/Mclaren P1.png"
                            carimage4 = pygame.image.load("res/Mclaren P1.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Mclaren P1":
                    if change == 0:
                        if level >= 9:
                            currentcar2 = "Nissan 240SX"
                            carimagepath2 = "res/Nissan 240SX.png"
                            carimage4 = pygame.image.load("res/Nissan 240SX.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nissan 240SX":
                    if change == 0:
                        if level >= 10:
                            currentcar2 = "Nissan GTR R35"
                            carimagepath2 = "res/Nissan GTR R35.png"
                            carimage4 = pygame.image.load("res/Nissan GTR R35.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nissan GTR R35":
                    if change == 0:
                        if level >= 11:
                            currentcar2 = "Porsche 918"
                            carimagepath2 = "res/Porsche 918.png"
                            carimage4 = pygame.image.load("res/Porsche 918.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Porsche 918":
                    if change == 0:
                        if level >= 12:
                            currentcar2 = "Nitro Cart"
                            carimagepath2 = "res/Nitro Cart.png"
                            carimage4 = pygame.image.load("res/Nitro Cart.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nitro Cart":
                    if change == 0:
                        if level >= 13:
                            currentcar2 = "Limited Gold Koenigsegg One"
                            carimagepath2 = "res/Limited Gold Koenigsegg One.png"
                            carimage4 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Limited Gold Koenigsegg One":
                    if change == 0:
                        if level >= 16:
                            currentcar2 = "Toyota Supra"
                            carimagepath2 = "res/Toyota Supra.png"
                            carimage4 = pygame.image.load("res/Toyota Supra.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Toyota Supra":
                    if change == 0:
                        if level >= 17:
                            currentcar2 = "WMotors Fenyr SuperSport"
                            carimagepath2 = "res/WMotors Fenyr SuperSport.png"
                            carimage4 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                            change = 10
                        else:
                            currentcar2 = "ford_gt"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "WMotors Fenyr SuperSport":
                    if change == 0:
                        currentcar2 = "ford_gt"
                        carimagepath2 = "res/ford_gt.png"
                        carimage4 = pygame.image.load("res/ford_gt.png")
                        change = 10
        #Change Players
        if pressed[pygame.K_p]:
            if players == 1:
                if change == 0:
                    players = 2
                    change = 10
            if players == 2:
                if change == 0:
                    players = 1
                    change = 10
        #Change Tracks
        if pressed[pygame.K_t]:
            parser.read("res/tracks.ini")
            if change == 0:
                change = 10
                track += 1
                tracktotalstr = parser.get("info", "tracktotal")
                tracktotal = int(tracktotalstr)
                if track >= tracktotal:
                    track = 1
                if track == 2:
                    trackname = parser.get("track2", "trackname")
                    trackpath = parser.get("track2", "trackpath")

                if track == 3:
                    if level >= 3:
                        trackname = parser.get("track3", "trackname")
                        trackpath = parser.get("track3", "trackpath")
                    else:
                        track = 1
                if track == 4:
                    if level >= 10:
                        trackname = parser.get("track4", "trackname")
                        trackpath = parser.get("track4", "trackpath")
                    else:
                        track = 1
                if track == 5:
                    if level >= 14:
                        trackname = parser.get("track5", "trackname")
                        trackpath = parser.get("track5", "trackpath")
                    else:
                        track = 1
                if track == 6:
                    if level >= 15:
                        trackname = parser.get("track6", "trackname")
                        trackpath = parser.get("track6", "trackpath")
                    else:
                        track = 1
                if track == 7:
                    if level >= 18:
                        trackname = parser.get("track7", "trackname")
                        trackpath = parser.get("track7", "trackpath")
                    else:
                        track = 1
                if track == 1:
                    trackname = parser.get("track1", "trackname")
                    trackpath = parser.get("track1", "trackpath")
        #Change Speed
        if pressed[pygame.K_b]:
            if change == 0:
                change = 10
                clockspeed = clockspeed + 50
        if clockspeed >= 301:
            clockspeed = 50
        #Selecting things
        if pressed[pygame.K_SPACE]:
            if x >= 1175:
                if y >= 615:
                    done = True
            if x <= 163:
                if y <= 87:
                    sendtomain()
            if x >= 1180:
                if y <= 100:
                    inhelp = True
            if x <= 160:
                if y >= 640:
                    if change == 0:
                        if not fulscr:
                            screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                            fulscr = True
                            change = 20
                    if change == 0:
                        if fulscr:
                            screen = pygame.display.set_mode((1280, 720))
                            fulscr = False
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
        if change >> 0:
            change -= 1
        carlabel = cartext + currentcar
        carlabel2 = font.render(carlabel, 10, white)
        tracklabel = "Track " + str(track) + ": " + trackname
        tracklabel2 = font.render(tracklabel, 10 ,white)
        clockspeedlabel = str(clockspeed) + " CC"
        clockspeedlabel2 = font.render(clockspeedlabel, 10 ,white)
        help = "Drive to a box, and press space to go!"
        welcometo = "Welcome to "
        helplabel = "Help"
        helplabel1 = "On the Menu screen:"
        helplabel2 = "Press C to change cars"
        helplabel3 = "Press T to change tracks"
        helplabel4 = "Press B to change the clockspeed"
        helplabel5 = "During a race:"
        helplabel6 = "Left and Right steer"
        helplabel7 = "Up is the gas pedal"
        helplabel8 = "Down is the brake"
        helplabel9 = "Space will use your nos"
        helplabel10 = "Press escape to get rid of this message"
        helplabel11 = "Press P to change amount of players (Up to 2)"
        helplabel12 = "W,A,S,D + Left Shift Keys control player 2 in the same way as player 1"
        helplabel13 = "About Leveling:"
        helplabel14 = "At each new level (up to level 17) you will unlock a new car or track"
        helplabel15 = "(They will be automatically added to the Menu screen.)"
        helplabel16 = "Press V to change the second player vehicle"
        fullscrlabel = "Fullscreen"
        playerlabel = "Players : " + str(players)
        playerl = font.render(playerlabel, 10, white)
        pointsl = font.render(str(points) + " / " + str(levelpoints), 10, white)
        levell = font50.render("Level " + str(level), 10, white)
        levelposition = levelpoints
        fullscrl = font.render(fullscrlabel, 10, white)
        welcomel = font.render(welcometo, 10 ,white)
        helpl = font.render(helplabel, 10 ,white)
        helpl1 = font.render(helplabel1, 10 ,white)
        helpl2 = font.render(helplabel2, 10 ,white)
        helpl3 = font.render(helplabel3, 10 ,white)
        helpl4 = font.render(helplabel4, 10 ,white)
        helpl5 = font.render(helplabel5, 10 ,white)
        helpl6 = font.render(helplabel6, 10 ,white)
        helpl7 = font.render(helplabel7, 10 ,white)
        helpl8 = font.render(helplabel8, 10 ,white)
        helpl9 = font.render(helplabel9, 10 ,white)
        helpl10 = font.render(helplabel10, 10 ,white)
        helpl11 = font.render(helplabel11, 10 ,white)
        helpl12 = font.render(helplabel12, 10 ,white)
        helpl13 = font.render(helplabel13, 10 ,white)
        helpl14 = font.render(helplabel14, 10 ,white)
        helpl15 = font.render(helplabel15, 10 ,white)
        helpl16 = font.render(helplabel16, 10 ,white)
        help10 = font.render(help, 10 ,white)
        #Drawing/rendering
        pygame.draw.rect(screen, darkdarkred, pygame.Rect(0, 0, 6000, 6000))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 620, 100, 100))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 0, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 640, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(700, 300, 300, 40))
        pygame.draw.rect(screen, blue, pygame.Rect(700, 300, int(levelpixels), 40))
        screen.blit(levell, (700, 250))
        screen.blit(pointsl, (700, 350))
        screen.blit(helpl, (1180, 0))
        screen.blit(fullscrl, (0, 650))
        screen.blit(tracklabel2, (100,200))
        screen.blit(clockspeedlabel2, (100, 250))
        screen.blit(label, (1185, 625))
        screen.blit(labelstart, (10, 10))
        screen.blit(carlabel2, (100, 150))
        screen.blit(help10, (495, 680))
        screen.blit(logo, (600, 10))
        screen.blit(welcomel, (495, 60))
        screen.blit(playerl, (100, 300))
        screen.blit(carimage2, (x,y))
        if players == 2:
            screen.blit(carimage4, (x2,y2))
        if inhelp:
            screen.fill(darkdarkred)
            screen.blit(helpl, (565, 10))
            screen.blit(helpl1, (100, 40))
            screen.blit(helpl2, (100, 70))
            screen.blit(helpl3, (100, 100))
            screen.blit(helpl4, (100, 130))
            screen.blit(helpl5, (600, 40))
            screen.blit(helpl6, (600, 70))
            screen.blit(helpl7, (600, 100))
            screen.blit(helpl8, (600, 130))
            screen.blit(helpl9, (600, 160))
            screen.blit(helpl10, (430, 400))
            screen.blit(helpl11, (100, 160))
            screen.blit(helpl12, (600, 190))
            screen.blit(helpl13, (400, 250))
            screen.blit(helpl14, (400, 280))
            screen.blit(helpl15, (400, 310))
            screen.blit(helpl16, (100, 190))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
