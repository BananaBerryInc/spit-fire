# Import those moduels!!!!
import os
import sys
import os.path as osp
import io
import subprocess
from subprocess import call
try:
    import pygame
except ImportError:
    print("You don't have Pygame installed; I'll install it for you")
    call(["python3", "-m", "pip","install","pygame","--user"])
try:
    from PIL import Image
except ImportError:
    print("You don't have PIL installed; I'll install it for you")
    call(["python3", "-m", "pip","install","Pillow","--user"])
from configparser import SafeConfigParser

#Settin' up the window!
pygame.init()
pygame.font.init()
font = pygame.font.Font("res/Saira-Regular.ttf", 25)
font50 = pygame.font.Font("res/Saira-Regular.ttf", 35)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 5")
pygame.display.flip()

#Intro Music
#pygame.mixer.music.load("res/Title scren.ogg")
#pygame.mixer.music.play(1,0)
#Variables
clock = pygame.time.Clock()
x = 30
y = 30
x2 = 60
y2 = 60
parser = SafeConfigParser()
parser.read("res/options.ini")
players = int(parser.get("options", "players"))
inhelp = False
shifting = "Automatic"
shifting2 = "Automatic"
shifttext = ""
shifttext2 = ""
currentcar2 = parser.get("options", "car2")
back = pygame.image.load("res/Title Screen Parking Lot.png")
carimagepath2 = parser.get("options", "carimage2")
carimage2 = pygame.image.load("res/ford_gt.png")
parser = SafeConfigParser()
parser.read("res/options.ini")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
level = parser.get("options", "level")
trackname = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
shifting = parser.get("options", "shifting")
shifting2 = parser.get("options", "shifting2")
points = parser.get("options", "points")
clockspeed = int(parser.get("options", "speed"))
level = int(level)
levelpoints = (int(level) + 100) * 202.2
levelpoints = round(levelpoints, 1)
levelpixels = float(points) / levelpoints * 300
carimage = pygame.image.load(parser.get("options", "carimage"))
carimage2 = pygame.image.load(parser.get("options", "carimage"))
carimagepath = parser.get("options", "carimage")
currentcar = parser.get("options", "car")
cartext = "Car: "
track = int(parser.get("options", "track"))
parser.read("res/tracks.ini")
trackname = trackname = parser.get("track" + str(track), "trackname")
change = 0
carimage3 = pygame.image.load(parser.get("options", "carimage2"))
carimage4 = carimage3
parser = SafeConfigParser()
if level == 1:
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
    global carimagepath
    global carimagepath2
    global currentcar
    global currentcar2
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global levelpoints
    global players
    global car2
    global shifting
    global shifting2
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "track", str(track))
    parser.set("options", "car", currentcar)
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "shifting", shifting)
    parser.set("options", "shifting2", shifting2)
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
            if inhelp:
                if change == 0:
                    inhelp = False
                    change = 30
            else:
                if change == 0:
                    #Quit With the escape key
                    pygame.QUIT
                    quit()
        if pressed[pygame.K_c]:
            if currentcar == "Dodge Challenger":
                if change == 0:
                    if level >= 4:
                        currentcar = "Koenigsegg One"
                        carimagepath = "res/Koenigsegg_One.png"
                        carimage2 = pygame.image.load("res/Koenigsegg_One.png")
                        carimage = pygame.image.load("res/Koenigsegg_One.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Ferrari F40":
                if change == 0:
                    if level >= 5:
                        currentcar = "Dodge Challenger"
                        carimagepath = "res/Dodge_Challenger.png"
                        carimage2 = pygame.image.load("res/Dodge_Challenger.png")
                        carimage = pygame.image.load("res/Dodge_Challenger.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Ford GT":
                if change == 0:
                    if level >= 2:
                        currentcar = "Ferrari F40"
                        carimagepath = "res/Ferrari_F40.png"
                        carimage2 = pygame.image.load("res/Ferrari_F40.png")
                        carimage = pygame.image.load("res/Ferrari_F40.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Koenigsegg One":
                if change == 0:
                    if level >= 6:
                        currentcar = "Bugatti Vision GT Gran Turismo"
                        carimagepath = "res/Bugatti Vision GT Gran Turismo.png"
                        carimage2 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                        carimage = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Bugatti Vision GT Gran Turismo":
                if change == 0:
                    if level >= 7:
                        currentcar = "Camaro ZL1 1LE"
                        carimagepath = "res/Camaro ZL1 1LE.png"
                        carimage2 = pygame.image.load("res/Camaro ZL1 1LE.png")
                        carimage = pygame.image.load("res/Camaro ZL1 1LE.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Camaro ZL1 1LE":
                if change == 0:
                    if level >= 8:
                        currentcar = "Mclaren P1"
                        carimagepath = "res/Mclaren P1.png"
                        carimage2 = pygame.image.load("res/Mclaren P1.png")
                        carimage = pygame.image.load("res/Mclaren P1.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Mclaren P1":
                if change == 0:
                    if level >= 9:
                        currentcar = "Nissan 240SX"
                        carimagepath = "res/Nissan 240SX.png"
                        carimage2 = pygame.image.load("res/Nissan 240SX.png")
                        carimage = pygame.image.load("res/Nissan 240SX.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nissan 240SX":
                if change == 0:
                    if level >= 10:
                        currentcar = "Nissan GTR R35"
                        carimagepath = "res/Nissan GTR R35.png"
                        carimage2 = pygame.image.load("res/Nissan GTR R35.png")
                        carimage = pygame.image.load("res/Nissan GTR R35.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nissan GTR R35":
                if change == 0:
                    if level >= 11:
                        currentcar = "Porsche 918"
                        carimagepath = "res/Porsche 918.png"
                        carimage2 = pygame.image.load("res/Porsche 918.png")
                        carimage = pygame.image.load("res/Porsche 918.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Porsche 918":
                if change == 0:
                    if level >= 12:
                        currentcar = "Nitro Cart"
                        carimagepath = "res/Nitro Cart.png"
                        carimage2 = pygame.image.load("res/Nitro Cart.png")
                        carimage = pygame.image.load("res/Nitro Cart.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Nitro Cart":
                if change == 0:
                    if level >= 13:
                        currentcar = "Limited Gold Koenigsegg One"
                        carimagepath = "res/Limited Gold Koenigsegg One.png"
                        carimage2 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                        carimage = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Limited Gold Koenigsegg One":
                if change == 0:
                    if level >= 16:
                        currentcar = "Toyota Supra"
                        carimagepath = "res/Toyota Supra.png"
                        carimage2 = pygame.image.load("res/Toyota Supra.png")
                        carimage = pygame.image.load("res/Toyota Supra.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Toyota Supra":
                if change == 0:
                    if level >= 17:
                        currentcar = "WMotors Fenyr SuperSport"
                        carimagepath = "res/WMotors Fenyr SuperSport.png"
                        carimage2 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                        carimage = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "WMotors Fenyr SuperSport":
                if change == 0:
                    if level >= 19:
                        currentcar = "1998 Ferrari F355 Spider"
                        carimagepath = "res/1998 Ferrari F355 Spider.png"
                        carimage2 = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                        carimage = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "1998 Ferrari F355 Spider":
                if change == 0:
                    if level >= 20:
                        currentcar = "Dodge Viper ACR"
                        carimagepath = "res/Dodge Viper ACR.png"
                        carimage2 = pygame.image.load("res/Dodge Viper ACR.png")
                        carimage = pygame.image.load("res/Dodge Viper ACR.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Dodge Viper ACR":
                if change == 0:
                    if level >= 21:
                        currentcar = "2016 Lamborghini Huracan LP610-4"
                        carimagepath = "res/2016 Lamborghini Huracan LP610-4.png"
                        carimage2 = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                        carimage = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        carimage = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "2016 Lamborghini Huracan LP610-4":
                if change == 0:
                    if level >= 22:
                        currentcar = "Porsche Mission E Concept"
                        carimagepath = "res/porsche mission e concept.png"
                        carimage = pygame.image.load("res/porsche mission e concept.png")
                        carimage2 = pygame.image.load("res/porsche mission e concept.png")
                        change = 10
                    else:
                        currentcar = "Ford GT"
                        carimagepath = "res/ford_gt.png"
                        carimage = pygame.image.load("res/ford_gt.png")
                        carimage2 = pygame.image.load("res/ford_gt.png")
                        change = 10
            if currentcar == "Porsche Mission E Concept":
                if change == 0:
                     currentcar = "Ford GT"
                     carimagepath = "res/ford_gt.png"
                     carimage = pygame.image.load("res/ford_gt.png")
                     carimage2 = pygame.image.load("res/ford_gt.png")
                     change = 10
        if players == 2:
            if pressed[pygame.K_v]:
                if currentcar2 == "Dodge Challenger":
                    if change == 0:
                        if level >= 4:
                            currentcar2 = "Koenigsegg One"
                            carimagepath2 = "res/Koenigsegg_One.png"
                            carimage3 = pygame.image.load("res/Koenigsegg_One.png")
                            carimage4 = pygame.image.load("res/Koenigsegg_One.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Ferrari F40":
                    if change == 0:
                        if level >= 5:
                            currentcar2 = "Dodge Challenger"
                            carimagepath2 = "res/Dodge_Challenger.png"
                            carimage3 = pygame.image.load("res/Dodge_Challenger.png")
                            carimage4 = pygame.image.load("res/Dodge_Challenger.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Ford GT":
                    if change == 0:
                        if level >= 2:
                            currentcar2 = "Ferrari F40"
                            carimagepath2 = "res/Ferrari_F40.png"
                            carimage3 = pygame.image.load("res/Ferrari_F40.png")
                            carimage4 = pygame.image.load("res/Ferrari_F40.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Koenigsegg One":
                    if change == 0:
                        if level >= 6:
                            currentcar2 = "Bugatti Vision GT Gran Turismo"
                            carimagepath2 = "res/Bugatti Vision GT Gran Turismo.png"
                            carimage3 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                            carimage4 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Bugatti Vision GT Gran Turismo":
                    if change == 0:
                        if level >= 7:
                            currentcar2 = "Camaro ZL1 1LE"
                            carimagepath2 = "res/Camaro ZL1 1LE.png"
                            carimage3 = pygame.image.load("res/Camaro ZL1 1LE.png")
                            carimage4 = pygame.image.load("res/Camaro ZL1 1LE.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Camaro ZL1 1LE":
                    if change == 0:
                        if level >= 8:
                            currentcar2 = "Mclaren P1"
                            carimagepath2 = "res/Mclaren P1.png"
                            carimage3 = pygame.image.load("res/Mclaren P1.png")
                            carimage4 = pygame.image.load("res/Mclaren P1.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Mclaren P1":
                    if change == 0:
                        if level >= 9:
                            currentcar2 = "Nissan 240SX"
                            carimagepath2 = "res/Nissan 240SX.png"
                            carimage3 = pygame.image.load("res/Nissan 240SX.png")
                            carimage4 = pygame.image.load("res/Nissan 240SX.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nissan 240SX":
                    if change == 0:
                        if level >= 10:
                            currentcar2 = "Nissan GTR R35"
                            carimagepath2 = "res/Nissan GTR R35.png"
                            carimage3 = pygame.image.load("res/Nissan GTR R35.png")
                            carimage4 = pygame.image.load("res/Nissan GTR R35.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nissan GTR R35":
                    if change == 0:
                        if level >= 11:
                            currentcar2 = "Porsche 918"
                            carimagepath2 = "res/Porsche 918.png"
                            carimage3 = pygame.image.load("res/Porsche 918.png")
                            carimage4 = pygame.image.load("res/Porsche 918.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Porsche 918":
                    if change == 0:
                        if level >= 12:
                            currentcar2 = "Nitro Cart"
                            carimagepath2 = "res/Nitro Cart.png"
                            carimage3 = pygame.image.load("res/Nitro Cart.png")
                            carimage4 = pygame.image.load("res/Nitro Cart.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Nitro Cart":
                    if change == 0:
                        if level >= 13:
                            currentcar2 = "Limited Gold Koenigsegg One"
                            carimagepath2 = "res/Limited Gold Koenigsegg One.png"
                            carimage3 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                            carimage4 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Limited Gold Koenigsegg One":
                    if change == 0:
                        if level >= 16:
                            currentcar2 = "Toyota Supra"
                            carimagepath2 = "res/Toyota Supra.png"
                            carimage3 = pygame.image.load("res/Toyota Supra.png")
                            carimage4 = pygame.image.load("res/Toyota Supra.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Toyota Supra":
                    if change == 0:
                        if level >= 17:
                            currentcar2 = "WMotors Fenyr SuperSport"
                            carimagepath2 = "res/WMotors Fenyr SuperSport.png"
                            carimage3 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                            carimage4 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "WMotors Fenyr SuperSport":
                    if change == 0:
                        if level >= 19:
                            currentcar2 = "1998 Ferrari F355 Spider"
                            carimagepath2 = "res/1998 Ferrari F355 Spider.png"
                            carimage3 = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                            carimage4 = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "1998 Ferrari F355 Spider":
                    if change == 0:
                        if level >= 20:
                            currentcar2 = "Dodge Viper ACR"
                            carimagepath2 = "res/Dodge Viper ACR.png"
                            carimage3 = pygame.image.load("res/Dodge Viper ACR.png")
                            carimage4 = pygame.image.load("res/Dodge Viper ACR.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Dodge Viper ACR":
                    if change == 0:
                        if level >= 21:
                            currentcar2 = "2016 Lamborghini Huracan LP610-4"
                            carimagepath2 = "res/2016 Lamborghini Huracan LP610-4.png"
                            carimage3 = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                            carimage4 = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "2016 Lamborghini Huracan LP610-4":
                    if change == 0:
                        if level >= 22:
                            currentcar2 = "Porsche Mission E Concept"
                            carimagepath2 = "res/porsche mission e concept.png"
                            carimage3 = pygame.image.load("res/porsche mission e concept.png")
                            carimage4 = pygame.image.load("res/porsche mission e concept.png")
                            change = 10
                        else:
                            currentcar2 = "Ford GT"
                            carimagepath2 = "res/ford_gt.png"
                            carimage3 = pygame.image.load("res/ford_gt.png")
                            carimage4 = pygame.image.load("res/ford_gt.png")
                            change = 10
                if currentcar2 == "Porsche Mission E Concept":
                    if change == 0:
                         currentcar2 = "Ford GT"
                         carimagepath2 = "res/ford_gt.png"
                         carimage3 = pygame.image.load("res/ford_gt.png")
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
            if x <= 183:
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
                            change = 20
            if x >= 200:
                if x <= 362:
                    if players == 1:
                        if y >= 620:
                            if change == 0:
                                if shifting == "Automatic":
                                    shifting = "Manual"
                                    change = 10
                            if change == 0:
                                if shifting == "Manual":
                                    shifting = "Automatic"
                                    change = 10
                    if players == 2:
                        if y >= 620:
                            if y <= 679:
                                if change == 0:
                                    if shifting == "Automatic":
                                        shifting = "Manual"
                                        change = 10
                                if change == 0:
                                    if shifting == "Manual":
                                        shifting = "Automatic"
                                        change = 10
                        if y >= 680:
                            if change == 0:
                                if shifting2 == "Automatic":
                                    shifting2 = "Manual"
                                    change = 10
                            if change == 0:
                                if shifting2 == "Manual":
                                    shifting2 = "Automatic"
                                    change = 10
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
        helplabel2 = "Press C to change cars (for the first player)"
        helplabel3 = "Press T to change tracks"
        helplabel4 = "Press B to change the clockspeed/difficulty"
        helplabel5 = "During a race:"
        helplabel6 = "Left and Right steer"
        helplabel7 = "Up is the gas pedal/accelleration"
        helplabel8 = "Down is the brake"
        helplabel9 = "Space will use your nos"
        helplabel10 = "Press escape to get rid of this message"
        helplabel11 = "Press P to change amount of players (Up to 2)"
        helplabel12 = "The W,A,S,D,Q Keys control player 2 in the same way as player 1"
        helplabel13 = "About Leveling:"
        helplabel14 = "At each new level (up to level 22) you will unlock a new car or track"
        helplabel15 = "(They will be automatically added to the Menu screen.)"
        helplabel16 = "Press V to change the second player vehicle"
        helplabel17 = "Press Right Shift or E to shift gears"
        helplabel18 = "Shifting is always manual on the Drag Strip"
        fullscrlabel = "Fullscreen"
        fullscrlabel2 = "Toggle"
        shiftinglabel = "Shifting:"
        playerlabel = "Players : " + str(players)
        playerl = font.render(playerlabel, 10, white)
        pointsl = font.render(str(points) + " / " + str(levelpoints), 10, white)
        levell = font50.render("Level " + str(level), 10, white)
        levelposition = levelpoints
        fullscrl = font.render(fullscrlabel, 10, white)
        fullscrl2 = font.render(fullscrlabel2, 10, white)
        welcomel = font.render(welcometo, 10 ,white)
        shiftingtitle = font.render(shiftinglabel, 10 ,white)
        shiftingl = font.render(shifting, 10 ,white)
        shifting2l = font.render(shifting2, 10 ,white)
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
        helpl17 = font.render(helplabel17, 10 ,white)
        helpl18 = font.render(helplabel18, 10 ,white)
        help10 = font.render(help, 10 ,white)
        #Drawing/rendering
        screen.blit(back, (0,0))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 620, 100, 100))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 180, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(1180, 0, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(0, 640, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(200, 640, 160, 85))
        pygame.draw.rect(screen, gray, pygame.Rect(800, 300, 300, 40))
        pygame.draw.rect(screen, blue, pygame.Rect(800, 300, int(levelpixels), 40))
        screen.blit(levell, (800, 250))
        screen.blit(shiftingtitle, (201, 631))
        screen.blit(shiftingl, (201, 661))
        screen.blit(pointsl, (800, 350))
        screen.blit(helpl, (1180, 0))
        screen.blit(fullscrl, (0, 670))
        screen.blit(fullscrl2, (0, 640))
        screen.blit(tracklabel2, (150,200))
        screen.blit(clockspeedlabel2, (150, 250))
        screen.blit(label, (1185, 625))
        screen.blit(labelstart, (1, 1))
        screen.blit(carlabel2, (150, 150))
        screen.blit(help10, (470, 580))
        screen.blit(logo, (630, 0))
        screen.blit(welcomel, (500, 40))
        screen.blit(playerl, (150, 300))
        if players == 2:
            screen.blit(shifting2l, (201, 685))
        screen.blit(carimage2, (x,y))
        if players == 2:
            screen.blit(carimage4, (x2,y2))
        if inhelp:
            screen.fill(darkdarkred)
            screen.blit(helpl, (565, 10))
            screen.blit(helpl1, (50, 40))
            screen.blit(helpl2, (50, 70))
            screen.blit(helpl3, (50, 100))
            screen.blit(helpl4, (50, 130))
            screen.blit(helpl5, (580, 40))
            screen.blit(helpl6, (580, 70))
            screen.blit(helpl7, (580, 100))
            screen.blit(helpl8, (580, 130))
            screen.blit(helpl9, (580, 160))
            screen.blit(helpl10, (430, 450))
            screen.blit(helpl11, (50, 160))
            screen.blit(helpl12, (580, 190))
            screen.blit(helpl13, (400, 310))
            screen.blit(helpl14, (400, 350))
            screen.blit(helpl15, (400, 380))
            screen.blit(helpl16, (50, 190))
            screen.blit(helpl17, (580, 220))
            screen.blit(helpl18, (580, 250))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
