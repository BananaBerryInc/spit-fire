# Import those moduels!!!!
import os
import sys
import os.path as osp
import io
import subprocess
import urllib.request
from subprocess import call

printerror = False

#Detect Python version and give an error if too old
if sys.version_info[0] < 3:
    print("You need Python3 to run spit-fire!")
    quit()
    

#Install pip, pygame, and PIL if nessary
try:
    import pygame
except ImportError:
    print("You don't have Pygame installed; I'll install it for you")
    print("Downloading pip, incase you don't have it")
    url = "https://bootstrap.pypa.io/get-pip.py"
    urllib.request.urlretrieve(url, "get-pip.py")
    print("Now installing pip")
    call(["python3", "get-pip.py"])
    print("Now installing Pygame")
    call(["python3", "-m", "pip","install","pygame","--user"])
    try:
        import pygame
    except ImportError:
        printerror = True
try:
    from PIL import Image
except ImportError:
    print("You don't have PIL installed; I'll install it for you")
    call(["python3", "-m", "pip","install","Pillow","--user"])
from configparser import SafeConfigParser

if printerror:
        print("Pygame and/or PIL are now installed, but you will need to restart Spit-fire for them to work")
        quit()

#Settin' up the window!
pygame.init()
pygame.font.init()
fontsmall = pygame.font.Font("res/Saira-Regular.ttf", 15)
font = pygame.font.Font("res/Saira-Regular.ttf", 25)
font50 = pygame.font.Font("res/Saira-Regular.ttf", 35)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 5")
white = (255,255,255)
loading = font50.render("Now Loading...", 10, white)
screen.blit(loading, (640, 350))
pygame.display.flip()

#Intro Music
#pygame.mixer.music.load("res/Title scren.ogg")
#pygame.mixer.music.play(1,0)
#Variables
#Text Strings 



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


#Variables
frame = 2
help = "Drive to a box, and press space to go!"
welcometo = "Welcome to "
helplabel = "Help"
helplabel1 = "On the Menu screen:"
helplabel2 = "Press C to change cars (for the first player)"
helplabel3 = "Use the Track Picker to change tracks/cups"
helplabel4 = "Press B to change the clockspeed/difficulty"
helplabel5 = "During a race:"
helplabel6 = "Left and Right steer"
helplabel7 = "Up is the gas pedal/accelleration"
helplabel8 = "Down is the brake"
helplabel9 = "Space will use your nos"
helplabel10 = "Press escape to get rid of this message"
helplabel11 = "Press M to change the mode (Single Race, Cup, multiplayer)"
helplabel12 = "The W,A,S,D,Q Keys control player 2"
helplabel13 = "About Leveling:"
helplabel14 = "At each new level (up to level 23) you will unlock a new car or track"
helplabel15 = "(They will be automatically added to the Menu screen.)"
helplabel16 = "Press V to change the second player vehicle"
helplabel17 = "Press Right Shift or E to shift gears"
helplabel18 = "Shifting is always manual on the Drag Strip"
fullscrlabel = "Menu"
fullscrlabel2 = "Options"
optionslabel1 = "Fullscreen:"
reslabel = "Resloution: "
the1080plabel = "1920x1080 (Full HD) - BETA FEATURE!!!!"
the720plabel = "1280x720 (HD)"
shiftinglabel = "Shifting:"
changelabel = "Change"
about3 = fontsmall.render("GitHub version",10, white)
about = fontsmall.render("Spit-fire 0.0.5 (Alpha 5)", 10, white)
about2 = fontsmall.render("Spit-fire is lisenced under GPL v3.0", 10, white)
reset = font.render("Reset the save file", 10, white)
backl = font.render("Back", 10, white)
trpick = font.render("Track", 10, white)
trpick2 = font.render("Picker", 10, white)
help10 = font.render(help, 10 ,white)
optionsl1 = font.render(optionslabel1, 10, white)
resl = font.render(reslabel, 10, white)
the1080pl = font.render(the1080plabel, 10, white)
the720pl = font.render(the720plabel, 10, white)
changel = font.render(changelabel, 10, white)
helpl = font.render(helplabel, 10 ,white)
explainl = font.render("Use the terminal window to enter the new name...", 10, white)
confirml = font.render("Use the terminal window to confirm this...", 10, white)
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
fullscrl = font.render(fullscrlabel, 10, white)
fullscrl2 = font.render(fullscrlabel2, 10, white)
welcomel = font.render(welcometo, 10 ,white)
clock = pygame.time.Clock()
intrackpick = False
screenres = "720p"
x = 30
y = 30
x2 = 60
y2 = 60
cup = 1
cupname = "Beginner Cup"
parser = SafeConfigParser()
parser.read("res/options.ini")
players = int(parser.get("options", "players"))
inhelp = False
inoptions = False
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
newgame = parser.get("options","newgame")
level = int(level)
levelpoints = (int(level) + 40) * 487.89
levelpoints = round(levelpoints, 1)
levelpixels = float(points) / levelpoints * 300
carimage = pygame.image.load(parser.get("options", "carimage"))
carimage2 = pygame.image.load(parser.get("options", "carimage"))
carimagepath = parser.get("options", "carimage")
currentcar = parser.get("options", "car")
cartext = "Car: "
showstartcountdown = parser.get("options", "showstartcountdown")
track = int(parser.get("options", "track"))
playername = parser.get("options", "name")
parser.read("res/tracks.ini")
t1thumb = pygame.image.load( "res/PolarBear Roundoff_upscaled_thumb.png")
t2thumb = pygame.image.load("res/Fishy Slide_thumb.png")
t3thumb = pygame.image.load("res/Original_thumb.png")
t4thumb = pygame.image.load("res/Camelback Pass (3)_thumb.png")
t5thumb = pygame.image.load("res/The Dual Ring_thumb.png")
t6thumb = pygame.image.load("res/Not An Animal This Time (2)_thumb.png")
t7thumb = pygame.image.load("res/Drag Race_thumb.png")
t8thumb = pygame.image.load("res/The Egg_thumb.png")
cup1thumb = pygame.image.load("res/begcup_thumb.png")
cup2thumb = pygame.image.load("res/anicup_thumb.png")
cup3thumb = pygame.image.load("res/dragcup_thumb.png")
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


#If new game, set it up
if newgame == "True":
    print("Welcome to Spit-fire! Let's get you setup")
    name = input(str("Please enter your name >"))
    print("Okay, you're good to go!")
    print("You can enable fullscreen in settings if you want")
    newgame = False
    wait = 50
    for wait in range(0,100):
        wait -= 1


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
    global showstartcountdown
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "track", str(track))
    parser.set("options", "car", currentcar)
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "shifting", shifting)
    parser.set("options", "name", playername)
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
    parser.set("options", "showstartcountdown", str(showstartcountdown))
    parser.set("options", "newgame", "False")
    if players == 3:
        parser.set("cupstats", "cup", str(cup))
        parser.set("cupstats", "track", "0")
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    if players == 3:
        exec(open("cupstats.py").read())
    exec(open("race.py").read())

def carpicker():
    global currentcar
    global change
    global level
    global carimagepath
    global carimage
    global carimage2
    if currentcar == "Dodge Challenger":
                if change == 0:
                    if level >= 5:
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
            if level >= 4:
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

def carpicker2():
    global currentcar2
    global change
    global level
    global carimagepath2
    global carimage3
    global carimage4
    if currentcar2 == "Dodge Challenger":
                if change == 0:
                    if level >= 4:
                        currentcar2 = "Koenigsegg One"
                        carimage3path2 = "res/Koenigsegg_One.png"
                        carimage4 = pygame.image.load("res/Koenigsegg_One.png")
                        carimage3 = pygame.image.load("res/Koenigsegg_One.png")
                        change = 10
                    else:
                        currentcar2 = "Ford GT"
                        carimage3path2 = "res/ford_gt.png"
                        carimage4 = pygame.image.load("res/ford_gt.png")
                        carimage3 = pygame.image.load("res/ford_gt.png")
                        change = 10
    if currentcar2 == "Ferrari F40":
        if change == 0:
            if level >= 5:
                currentcar2 = "Dodge Challenger"
                carimage3path2 = "res/Dodge_Challenger.png"
                carimage4 = pygame.image.load("res/Dodge_Challenger.png")
                carimage3 = pygame.image.load("res/Dodge_Challenger.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Ford GT":
        if change == 0:
            if level >= 2:
                currentcar2 = "Ferrari F40"
                carimage3path2 = "res/Ferrari_F40.png"
                carimage4 = pygame.image.load("res/Ferrari_F40.png")
                carimage3 = pygame.image.load("res/Ferrari_F40.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Koenigsegg One":
        if change == 0:
            if level >= 6:
                currentcar2 = "Bugatti Vision GT Gran Turismo"
                carimage3path2 = "res/Bugatti Vision GT Gran Turismo.png"
                carimage4 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                carimage3 = pygame.image.load("res/Bugatti Vision GT Gran Turismo.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Bugatti Vision GT Gran Turismo":
        if change == 0:
            if level >= 7:
                currentcar2 = "Camaro ZL1 1LE"
                carimage3path2 = "res/Camaro ZL1 1LE.png"
                carimage4 = pygame.image.load("res/Camaro ZL1 1LE.png")
                carimage3 = pygame.image.load("res/Camaro ZL1 1LE.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Camaro ZL1 1LE":
        if change == 0:
            if level >= 8:
                currentcar2 = "Mclaren P1"
                carimage3path2 = "res/Mclaren P1.png"
                carimage4 = pygame.image.load("res/Mclaren P1.png")
                carimage3 = pygame.image.load("res/Mclaren P1.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Mclaren P1":
        if change == 0:
            if level >= 9:
                currentcar2 = "Nissan 240SX"
                carimage3path2 = "res/Nissan 240SX.png"
                carimage4 = pygame.image.load("res/Nissan 240SX.png")
                carimage3 = pygame.image.load("res/Nissan 240SX.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Nissan 240SX":
        if change == 0:
            if level >= 10:
                currentcar2 = "Nissan GTR R35"
                carimage3path2 = "res/Nissan GTR R35.png"
                carimage4 = pygame.image.load("res/Nissan GTR R35.png")
                carimage3 = pygame.image.load("res/Nissan GTR R35.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Nissan GTR R35":
        if change == 0:
            if level >= 11:
                currentcar2 = "Porsche 918"
                carimage3path2 = "res/Porsche 918.png"
                carimage4 = pygame.image.load("res/Porsche 918.png")
                carimage3 = pygame.image.load("res/Porsche 918.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Porsche 918":
        if change == 0:
            if level >= 12:
                currentcar2 = "Nitro Cart"
                carimage3path2 = "res/Nitro Cart.png"
                carimage4 = pygame.image.load("res/Nitro Cart.png")
                carimage3 = pygame.image.load("res/Nitro Cart.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Nitro Cart":
        if change == 0:
            if level >= 13:
                currentcar2 = "Limited Gold Koenigsegg One"
                carimage3path2 = "res/Limited Gold Koenigsegg One.png"
                carimage4 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                carimage3 = pygame.image.load("res/Limited Gold Koenigsegg One.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Limited Gold Koenigsegg One":
        if change == 0:
            if level >= 16:
                currentcar2 = "Toyota Supra"
                carimage3path2 = "res/Toyota Supra.png"
                carimage4 = pygame.image.load("res/Toyota Supra.png")
                carimage3 = pygame.image.load("res/Toyota Supra.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Toyota Supra":
        if change == 0:
            if level >= 17:
                currentcar2 = "WMotors Fenyr SuperSport"
                carimage3path2 = "res/WMotors Fenyr SuperSport.png"
                carimage4 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                carimage3 = pygame.image.load("res/WMotors Fenyr SuperSport.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "WMotors Fenyr SuperSport":
        if change == 0:
            if level >= 19:
                currentcar2 = "1998 Ferrari F355 Spider"
                carimage3path2 = "res/1998 Ferrari F355 Spider.png"
                carimage4 = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                carimage3 = pygame.image.load("res/1998 Ferrari F355 Spider.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "1998 Ferrari F355 Spider":
        if change == 0:
            if level >= 20:
                currentcar2 = "Dodge Viper ACR"
                carimage3path2 = "res/Dodge Viper ACR.png"
                carimage4 = pygame.image.load("res/Dodge Viper ACR.png")
                carimage3 = pygame.image.load("res/Dodge Viper ACR.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Dodge Viper ACR":
        if change == 0:
            if level >= 21:
                currentcar2 = "2016 Lamborghini Huracan LP610-4"
                carimage3path2 = "res/2016 Lamborghini Huracan LP610-4.png"
                carimage4 = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                carimage3 = pygame.image.load("res/2016 Lamborghini Huracan LP610-4.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage4 = pygame.image.load("res/ford_gt.png")
                carimage3 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "2016 Lamborghini Huracan LP610-4":
        if change == 0:
            if level >= 22:
                currentcar2 = "Porsche Mission E Concept"
                carimage3path2 = "res/porsche mission e concept.png"
                carimage3 = pygame.image.load("res/porsche mission e concept.png")
                carimage4 = pygame.image.load("res/porsche mission e concept.png")
                change = 10
            else:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage3 = pygame.image.load("res/ford_gt.png")
                carimage4 = pygame.image.load("res/ford_gt.png")
                change = 10
    if currentcar2 == "Porsche Mission E Concept":
        if change == 0:
                currentcar2 = "Ford GT"
                carimage3path2 = "res/ford_gt.png"
                carimage3 = pygame.image.load("res/ford_gt.png")
                carimage4 = pygame.image.load("res/ford_gt.png")
                change = 10

def trackpicker():
    global change
    global track
    global cup
    global cupname
    global trackname
    global trackpath
    global level
    parser.read("res/tracks.ini")
    if change == 0:
        change = 10
        if players == 3:
            cup += 1
            tracktotalstr = parser.get("info", "cuptotal")
            tracktotal = int(tracktotalstr)
            if cup >= tracktotal:
                cup = 1
            if cup == 2:
                if level >= 15:
                    track = 1
                    cupname = parser.get("cup2", "cupname")
                    trackname = parser.get("track1", "trackname")
                    trackpath = parser.get("track1", "trackpath")
                else:
                    cup = 1
            if cup == 3:
                if level >= 18:
                    track = 1
                    cupname = parser.get("cup3", "cupname")
                    trackname = parser.get("track7", "trackname")
                    trackpath = parser.get("track7", "trackpath")
                else:
                    cup = 1
            if cup == 1:
                if level >= 10:
                    track = 1
                    cupname = parser.get("cup1", "cupname")
                    trackname = parser.get("track1", "trackname")
                    trackpath = parser.get("track1", "trackpath")
                else:
                    cup = 1
        if players <= 2:
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
            if track == 8:
                if level >= 23:
                    trackname = parser.get("track8", "trackname")
                    trackpath = parser.get("track8", "trackpath")
                else:
                    track = 1
            if track == 1:
                trackname = parser.get("track1", "trackname")
                trackpath = parser.get("track1", "trackpath")

def spaceaction():
    global inoptions
    global inhelp
    global points
    global showstartcountdown
    global x
    global y
    global change
    global screenres
    global fulscr
    global screen
    global back
    global done
    global players
    global shifting
    global shifting2
    global playername
    global explainl
    global intrackpick
    global track
    global trackname
    global trackpath
    global cup
    global cupname
    global level
    global currentcar
    global currentcar2
    global carimage
    global carimage2
    global levelpoints
    global levelpixels
    global carimagepath
    global carimage3path2
    if intrackpick:
        if x <= 450:
            if x >= 280:
                if y <= 100:
                    if change == 0:
                        intrackpick = False
                        change = 30
        parser.read("res/tracks.ini")
        if players == 3:
            if y >= 100:
                if y <= 299:
                    if x <= 299:
                        track = 1
                        cup = 1
                        cupname = parser.get("cup1", "cupname")
                        trackname = parser.get("track1", "trackname")
                        trackpath = parser.get("track1", "trackpath")
                        intrackpick = False
                    if x >= 300:
                        if  x >= 600:
                            if x >= 900:
                                if level <= 0:
                                    track = 4
                                    cup = 4
                                    cupname = parser.get("cup4", "cupname")
                                    trackname = parser.get("track4", "trackname")
                                    trackpath = parser.get("track4", "trackpath")
                                    intrackpick = False
                            else:
                                if level >= 3:
                                    track = 3
                                    cup = 3
                                    cupname = parser.get("cup3", "cupname")
                                    trackname = parser.get("track7", "trackname")
                                    trackpath = parser.get("track7", "trackpath")
                                    intrackpick = False
                        else:
                            track = 2
                            cup = 2
                            cupname = parser.get("cup2", "cupname")
                            trackname = parser.get("track1", "trackname")
                            trackpath = parser.get("track1", "trackpath")
                            intrackpick = False
        if players <= 2:
            if y >= 100:
                if y <= 299:
                    if x <= 299:
                        track = 1
                        trackname = parser.get("track1", "trackname")
                        trackpath = parser.get("track1", "trackpath")
                        intrackpick = False
                    if x >= 300:
                        if  x >= 600:
                            if x >= 900:
                                if level >= 10:
                                    track = 4
                                    trackname = parser.get("track4", "trackname")
                                    trackpath = parser.get("track4", "trackpath")
                                    intrackpick = False
                            else:
                                if level >= 3:
                                    track = 3
                                    trackname = parser.get("track3", "trackname")
                                    trackpath = parser.get("track3", "trackpath")
                                    intrackpick = False
                        else:
                            track = 2
                            trackname = parser.get("track2", "trackname")
                            trackpath = parser.get("track2", "trackpath")
                            intrackpick = False
                else:
                    if x <= 299:
                        trackname = parser.get("track5", "trackname")
                        trackpath = parser.get("track5", "trackpath")
                        track = 5
                        intrackpick = False
                    if x >= 300:
                        if x >= 600:
                            if x >= 900:
                                if level >= 23:
                                    trackname = parser.get("track8", "trackname")
                                    trackpath = parser.get("track8", "trackpath")
                                    track = 8
                                    intrackpick = False
                            else:
                                if level >= 18:
                                    trackname = parser.get("track7", "trackname")
                                    trackpath = parser.get("track7", "trackpath")
                                    track = 7
                                    intrackpick = False
                        else:
                            if level >= 15:
                                track = 6
                                trackname = parser.get("track6", "trackname")
                                trackpath = parser.get("track6", "trackpath")
                                intrackpick = False

        
    if inoptions:
            if x <= 160:
                if y >= 640:
                    if change == 0:
                        if not inoptions:
                            inoptions = True
                            change = 20
                    if change == 0:
                        if inoptions:
                            inoptions = False
                            change = 20
            if x >= 1000:
                if x <= 1200:
                    if y >= 45:
                        if y <= 150:
                            screen = pygame.display.set_mode((1280, 720))
                            screen.blit(confirml, (0,0))
                            pygame.display.flip()
                            why = str(input("THIS WILL DELETE ALL UNLOCKED ITEMS, YOUR LEVEL, ETC.. Are you sure (y/n)  >"))
                            if why == "y":
                                why = str(input("THIS ACTION CANNOT BE UNDONE... Are you sure (y/n)  >"))
                                if why == "y":
                                    parser.read("res/options.ini")
                                    parser.set("options", "level" ,"1")
                                    parser.set("options", "points", "0")
                                    parser.set("options", "car", "Ford GT")
                                    parser.set("options", "track", "1")
                                    parser.set("options", "carimage", "res/ford_gt.png")
                                    parser.set("options","trackpath", "res/PolarBear Roundoff_upscaled.png")
                                    parser.set("options", "carimage2", "res/ford_gt.png")
                                    parser.set("options", "name", "Use the Options Menu to set your name")
                                    parser.set("options","newgame", "True")
                                    trackname = "PolarBear Roundoff"
                                    trackpath = "res/PolarBear Roundoff_upscaled.png"
                                    currentcar = "Ford GT"
                                    currentcar2 = "Ford GT"
                                    with open('res/options.ini', 'w') as configfile:
                                        parser.write(configfile)
                                    level = 1
                                    points = 0
                                    track = 1
                                    players = 1
                                    carimagepath = "res/ford_gt.png"
                                    carimage3path2 = "res/ford_gt.png"
                                    carimage = pygame.image.load("res/ford_gt.png")
                                    carimage2 = pygame.image.load("res/ford_gt.png")
                                    levelpoints = (int(level) + 40) * 487.89
                                    levelpoints = round(levelpoints, 1)
                                    levelpixels = float(points) / levelpoints * 300
                                    playername = "Use the Options Menu to set your name"
                            if fulscr:
                                screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)
            if x >= 495:
                if x <= 795:
                    if y >= 45:
                        if y <= 150:
                            screen = pygame.display.set_mode((1280, 720))
                            screen.blit(explainl, (0,0))
                            pygame.display.flip()
                            playername = str(input("Enter the new name here >"))
                            if fulscr:
                                screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)
            if x >= 95:
                if x <= 375:
                    if y >= 45:
                        if y <= 150:
                            if fulscr:
                                if change == 0:
                                    fulscr = False
                                    screen =  pygame.display.set_mode((1280, 720))
                                    change = 20
                            if not fulscr:
                                if change == 0:
                                    screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)
                                    fulscr = True
                                    change = 20
            if x >= 95:
                if x <= 375:
                    if y >= 195:
                        if y <= 250:
                            if showstartcountdown:
                                if change == 0:
                                    showstartcountdown = False
                                    change = 20
                            if not showstartcountdown:
                                if change == 0:
                                    showstartcountdown = True
                                    change = 20
    if not inoptions:
        if x <= 450:
            if x >= 280:
                if y <= 100:
                    if change == 0:
                        if intrackpick:
                            intrackpick = False
                            change = 30
                        if not intrackpick:
                            intrackpick = True
                            change = 30
        if x >= 1175:
            if y >= 615:
                done = True
        if x <= 183:
            if y <= 87:
                sendtomain()
        if x >= 1180:
            if y <= 100:
                if not intrackpick:
                    inhelp = True
        if x <= 160:
            if y >= 640:
                if not intrackpick:
                    if change == 0:
                        if not inoptions:
                            inoptions = True
                            change = 20
                    if change == 0:
                        if inoptions:
                            inoptions = False
                            change = 20
        if x >= 200:
            if x <= 362:
                if not intrackpick:
                    if players != 2:
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
        if players == 2:
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
            carpicker()
        if players == 2:
            if pressed[pygame.K_v]:
                carpicker2()
        #Change Players
        if pressed[pygame.K_m]:
            if players == 1:
                if change == 0:
                    players = 2
                    change = 15
            if players == 2:
                if change == 0:
                    if level >= 10:
                        players = 3
                        change = 15
                    else:
                        players = 1
                        change = 15
            if players == 3:
                if change == 0:
                    players = 1
                    change = 15
        #Change Tracks
        if pressed[pygame.K_t]:
            trackpicker()
        #Change Speed
        if pressed[pygame.K_b]:
            if change == 0:
                change = 10
                clockspeed = clockspeed + 50
        if clockspeed >= 301:
            clockspeed = 50
        #Selecting things
        if pressed[pygame.K_SPACE]:
            spaceaction()
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
        if players == 3:
            tracklabel = "Cup " + str(cup) + ": " + cupname
        tracklabel2 = font.render(tracklabel, 10 ,white)
        clockspeedlabel = str(clockspeed) + " CC"
        clockspeedlabel2 = font.render(clockspeedlabel, 10 ,white)
        if players <= 2:
            playerlabel = "Mode: " + "Single Race (" + str(players) + " Player)"
        if players == 3:
            playerlabel = "Mode: " + "Cup (1 Player)"
        playerl = font.render(playerlabel, 10, white)
        pointsl = font.render(str(points) + " / " + str(levelpoints), 10, white)
        levell = font50.render("Level " + str(level), 10, white)
        levelposition = levelpoints
        shiftingtitle = font.render(shiftinglabel, 10 ,white)
        shiftingl = font.render(shifting, 10 ,white)
        shifting2l = font.render(shifting2, 10 ,white)
        fulscrl = font.render(str(fulscr), 10, white)
        nametextl = font.render("Name: " + playername, 10, white)
        #Drawing/rendering
        screen.fill((0,0,0))
        if not inoptions:
            if not inhelp:
                if not intrackpick:
                    screen.blit(back, (0,0))
                    pygame.draw.rect(screen, gray, pygame.Rect(1180, 620, 100, 100))
                    pygame.draw.rect(screen, gray, pygame.Rect(1180, 0, 160, 85))
                    pygame.draw.rect(screen, gray, pygame.Rect(0, 640, 160, 85))
                    pygame.draw.rect(screen, gray, pygame.Rect(200, 640, 160, 85))
                    pygame.draw.rect(screen, gray, pygame.Rect(800, 300, 300, 40))
                    pygame.draw.rect(screen, gray, pygame.Rect(300, 0, 150, 85))
                    pygame.draw.rect(screen, blue, pygame.Rect(800, 300, int(levelpixels), 40))
                    screen.blit(trpick,(300,0))
                    screen.blit(trpick2, (300,30))
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
                    screen.blit(carlabel2, (150, 150))
                    screen.blit(help10, (470, 580))
                    screen.blit(logo, (630, 0))
                    screen.blit(welcomel, (500, 40))
                    screen.blit(playerl, (150, 300))
                    if players == 2:
                        screen.blit(shifting2l, (201, 685))
                pygame.draw.rect(screen, gray, pygame.Rect(0, 0, 180, 85))
                screen.blit(labelstart, (1, 1))
        if intrackpick:
            pygame.draw.rect(screen, gray, pygame.Rect(300, 0, 150, 85))
            screen.blit(backl,(300,0))
            if players <= 2:
                screen.blit(t1thumb, (0,100))
                screen.blit(t2thumb, (300,100))
                if level >= 3:
                    screen.blit(t3thumb, (600, 100))
                if level >= 10:
                    screen.blit(t4thumb, (900, 100))
                if level >= 14:
                    screen.blit(t5thumb, (0, 300))
                if level >= 15:
                    screen.blit(t6thumb, (300, 300))
                if level >= 18:
                    screen.blit(t7thumb, (600, 300))
                if level >= 23:
                    screen.blit(t8thumb, (900, 300))
            if players == 3:
                if level >= 10:
                    screen.blit(cup1thumb, (0,100))
                if level >= 15:
                    screen.blit(cup2thumb, (300,100))
                if level >= 18:
                    screen.blit(cup3thumb, (600,100))
        screen.blit(carimage2, (x,y))
        if players == 2:
            screen.blit(carimage4, (x2,y2))
        if inhelp:
            screen.blit(helpl, (565, 10))
            screen.blit(helpl1, (5, 40))
            screen.blit(helpl2, (5, 70))
            screen.blit(helpl3, (5, 100))
            screen.blit(helpl4, (5, 130))
            screen.blit(helpl5, (680, 40))
            screen.blit(helpl6, (680, 70))
            screen.blit(helpl7, (680, 100))
            screen.blit(helpl8, (680, 130))
            screen.blit(helpl9, (680, 160))
            screen.blit(helpl10, (430, 450))
            screen.blit(helpl11, (5, 160))
            screen.blit(helpl12, (680, 190))
            screen.blit(helpl13, (400, 310))
            screen.blit(helpl14, (400, 350))
            screen.blit(helpl15, (400, 380))
            screen.blit(helpl16, (5, 190))
            screen.blit(helpl17, (680, 220))
            screen.blit(helpl18, (680, 250))
            screen.blit(about, (1000, 630))
            screen.blit(about2, (1000, 690))
            screen.blit(about3, (1000, 660))
        if inoptions:
            startcountdownl = font.render("Race start countdown :" + str(showstartcountdown), 10, white)
            pygame.draw.rect(screen, gray, pygame.Rect(0, 640, 160, 85))
            pygame.draw.rect(screen, gray, pygame.Rect(100,50, 210, 55))
            pygame.draw.rect(screen, gray, pygame.Rect(500, 50, 210, 55))
            pygame.draw.rect(screen, gray, pygame.Rect(1000, 50, 220, 55))
            pygame.draw.rect(screen, gray, pygame.Rect(100, 200, 220, 55))
            screen.blit(changel ,(100,200))
            screen.blit(startcountdownl, (100,250))
            screen.blit(reset, (1000,50))
            screen.blit(about, (1000, 630))
            screen.blit(about2, (1000, 690))
            screen.blit(about3, (1000, 660))
            screen.blit(fullscrl, (0, 670))
            screen.blit(fullscrl2, (0, 640))
            screen.blit(changel , (100, 50))
            screen.blit(optionsl1, (100, 100))
            screen.blit(fulscrl, (250, 100))
            screen.blit(carimage2, (x,y))
            screen.blit(nametextl, (500,100))
            screen.blit(changel,(500,50))
        #ANND, GO
        pygame.display.flip()
        clock.tick(clockspeed)
