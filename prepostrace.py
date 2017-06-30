# Import those moduels!!!!
import os
import sys
import pygame
import io
import subprocess
from configparser import SafeConfigParser
from random import randint
from PIL import Image
import operator

#Settin' up the window!
pygame.init()
pygame.font.init()
font = pygame.font.Font("res/Saira-Regular.ttf", 40)
fontbig = pygame.font.Font("res/Saira-Regular.ttf", 55)
fontsmall = pygame.font.Font("res/Saira-Regular.ttf", 27)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 4")
pygame.display.flip()

#Re-collecting those settings!
reallydonewiththis = False
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
trackstring = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
score = parser.get("options", "score")
place = parser.get("options", "place")
fulscr = parser.get("options", "fulscr")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
trackimage = pygame.image.load(trackpath)
level = int(parser.get("options", "level"))
points = float(parser.get("options", "points"))
levelpoints = (int(level) + 100) * 202.2
levelpixels = float(points) / levelpoints * 300
track = int(trackstring)
clock = pygame.time.Clock()
maxpoints = int(points) + int(score)
trackkey = "track" + str(track)
car = parser.get("options", "car")
clockspeedstring = parser.get("options", "speed")
players = int(parser.get("options", "players"))
score2 = int(parser.get("options", "score2"))
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
parser.read("res/tracks.ini")
maxlap = int(parser.get(trackkey, "laps"))
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")
parser.read("res/highscore.ini")
p1 = int(parser.get(trackkey, "p1"))
p2 = int(parser.get(trackkey, "p2"))
p3 = int(parser.get(trackkey, "p3"))
p4 = int(parser.get(trackkey, "p4"))
p5 = int(parser.get(trackkey, "p5"))
p6 = int(parser.get(trackkey, "p6"))
p7 = int(parser.get(trackkey, "p7"))
p8 = int(parser.get(trackkey, "p8"))
p9 = int(parser.get(trackkey, "p9"))
p10 = parser.get(trackkey, "p10")
p10 = int(p10)

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

trackimage = Image.open(trackpath)
tim = trackimage.load()
whiteout = (90,90,90)
pixcoloour = tim[1,1]
back = tuple(map(operator.add, pixcoloour, whiteout))
print(back)

def blanks():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global points
    global level
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "track", str(track))
    parser.set("options", "trackpath", trackpath)
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "speed", str(clockspeed))
    parser.set("options", "racefinsihed", "No")
    parser.set("options", "points", str(round(points, 0)))
    parser.set("options", "level", str(level))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    done = True
    pygame.QUIT
    quit()

def backtostart():
    global parser
    global carimage
    global currentcar
    global tracktotal
    global trackpath
    global track
    global trackname
    global clockspeed
    global points
    global level
    #send off the settings
    parser.read("res/options.ini")
    parser.set("options", "track", str(track))
    parser.set("options", "trackpath", trackpath)
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "speed", str(clockspeed))
    parser.set("options", "racefinsihed", "No")
    parser.set("options", "points", str(round(points, 0)))
    parser.set("options", "level", str(level))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("main.py").read())


#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Leveling
        if points <= maxpoints - 2000:
            points += 10.1
        if points <= maxpoints - 500:
            points -= 5.1
        if points <= maxpoints:
            points += 10.1
        if points >= levelpoints:
            level += 1
            maxpoints = maxpoints - points
            points = 0
        levelpoints = (int(level) + 100) * 202.2
        levelpixels = int(points) / levelpoints * 300
        #Key detection!
        pressed = pygame.key.get_pressed()
        #Quit With the escape key
        if pressed[pygame.K_ESCAPE]:
            blanks()
            reallydonewiththis = True
        #backtostart
        if pressed[pygame.K_RETURN]:
            backtostart()
        #Setting up the labels
        resultsl = font.render("Results: ", 30, black)
        if players == 2:
            scorelabel2 = "Player 2's score: " + str(score2)
            scorel2 = font.render(scorelabel2, 30, black)
        scorelabel = "Your Score: " + score
        scorel = fontbig.render(scorelabel, 30, black)
        firstplacelabel = "1st : " + str(p1)
        secondplacelabel = "2nd : " + str(p2)
        thirdplacelabel = "3rd : " + str(p3)
        fourthplacelabel = "4th : " + str(p4)
        fifthplacelabel = "5th : " + str(p5)
        sixthplacelabel = "6th : " + str(p6)
        seventhplacelabel = "7th : " + str(p7)
        eightplacelabel = "8th : " + str(p8)
        ninthplacelabel = "9th : " + str(p9)
        tenthplacelabel = "10th : " + str(p10)
        if place == "11":
            hi = "hi"
        if place == "1":
            firstplacelabel = "1st (You) :  " + score
            secondplacelabel = "2nd : " + str(p1)
            thirdplacelabel = "3rd : " + str(p2)
            fourthplacelabel = "4th : " + str(p3)
            fifthplacelabel = "5th : " + str(p4)
            sixthplacelabel = "6th : " + str(p5)
            seventhplacelabel = "7th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "2":
            secondplacelabel = "2nd (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p2)
            fourthplacelabel = "4th : " + str(p3)
            fifthplacelabel = "5th : " + str(p4)
            sixthplacelabel = "6th : " + str(p5)
            seventhplacelabel = "7th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "3":
            thirdplacelabel = "3rd (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            secondplacelabel = "2nd : " + str(p2)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            sixthplacelabel = "6th : " + str(p6)
            seventhplacelabel = "7th : " + str(p7)
            eightplacelabel = "8th : " + str(p8)
            ninthplacelabel = "9th : " + str(p9)
            tenthplacelabel = "10th : " + str(p10)
        if place == "4":
            fourthplacelabel = "4th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            secondplacelabel = "2nd : " + str(p2)
            fifthplacelabel = "5th : " + str(p4)
            sixthplacelabel = "6th : " + str(p5)
            seventhplacelabel = "7th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "5":
            fifthplacelabel = "5th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            secondplacelabel = "2nd : " + str(p2)
            sixthplacelabel = "6th : " + str(p5)
            seventhplacelabel = "7th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "6":
            sixthplacelabel = "6th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            secondplacelabel = "2nd : " + str(p2)
            seventhplacelabel = "7th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "7":
            seventhplacelabel = "7th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            secondplacelabel = "2nd : " + str(p2)
            sixthplacelabel = "6th : " + str(p6)
            eightplacelabel = "8th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "8":
            eightplacelabel = "8th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            secondplacelabel = "2nd : " + str(p2)
            sixthplacelabel = "6th : " + str(p6)
            seventhplacelabel = "7th : " + str(p7)
            ninthplacelabel = "9th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "9":
            ninthplacelabel = "9th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            secondplacelabel = "2nd : " + str(p2)
            sixthplacelabel = "6th : " + str(p6)
            seventhplacelabel = "7th : " + str(p7)
            ninthplacelabel = "8th : " + str(p8)
            tenthplacelabel = "10th : " + str(p9)
        if place == "10":
            tenthplacelabel = "10th (You) :  " + score
            firstplacelabel = "1st : " + str(p1)
            thirdplacelabel = "3rd : " + str(p3)
            fourthplacelabel = "4th : " + str(p4)
            fifthplacelabel = "5th : " + str(p5)
            secondplacelabel = "2nd : " + str(p2)
            sixthplacelabel = "6th : " + str(p6)
            seventhplacelabel = "7th : " + str(p7)
            eightplacelabel = "8th : " + str(p8)
            nineplacelabel = "9th : " + str(p9)
        firstplacel = font.render(firstplacelabel, 30, black)
        secondplacel = font.render(secondplacelabel, 30, black)
        thirdplacel = font.render(thirdplacelabel, 30, black)
        fourthplacel = font.render(fourthplacelabel, 30, black)
        fifthplacel = font.render(fifthplacelabel, 30, black)
        sixthplacel = font.render(sixthplacelabel, 30, black)
        seventhplacel = font.render(seventhplacelabel, 30, black)
        eightplacel = font.render(eightplacelabel, 30, black)
        ninthplacel = font.render(ninthplacelabel, 30, black)
        tenthplacel = font.render(tenthplacelabel, 30, black)
        startl = fontsmall.render("Press enter to start a new race", 30, black)
        donel = fontsmall.render("Press escape to exit Spitfire", 30, black)
        if players == 2:
            highl = fontsmall.render("Please note: highscore table is for player 1 ONLY!", 30, black)
        pointsl = font.render(str(round(points, 1)) + " / " + str(round(levelpoints, 1)), 10, black)
        levell = font.render("Level " + str(round(level, 1)), 10, black)
        # Rendering and drawing
        screen.fill(pixcoloour)
        s = pygame.Surface((1300,1300))
        if trackkey != "track1":
            if trackkey != "track4":
                s.set_alpha(75)
            else:
                s.set_alpha(0)
        else:
            s.set_alpha(75)
        if trackkey == "track5":
            s.set_alpha(100)
        s.fill((255,255,255))
        screen.blit(s, (0,0))
        pygame.draw.rect(screen, gray, pygame.Rect(700, 300, 300, 40))
        pygame.draw.rect(screen, blue, pygame.Rect(700, 300, int(levelpixels), 40))
        screen.blit(levell, (700, 250))
        screen.blit(pointsl, (700, 350))
        screen.blit(resultsl, (585, 10))
        screen.blit(firstplacel, (100, 80))
        screen.blit(secondplacel, (100, 130))
        screen.blit(thirdplacel, (100, 180))
        screen.blit(fourthplacel, (100, 230))
        screen.blit(fifthplacel, (100, 280))
        screen.blit(sixthplacel, (100, 330))
        screen.blit(seventhplacel, (100, 380))
        screen.blit(eightplacel, (100, 430))
        screen.blit(ninthplacel, (100, 480))
        screen.blit(tenthplacel, (100, 530))
        if players == 2:
            screen.blit(scorel2, (430, 660))
            screen.blit(highl, (680, 460))
        screen.blit(scorel, (430, 600))
        screen.blit(donel, (700, 400))
        screen.blit(startl, (700, 430))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
