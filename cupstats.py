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
import random

#Settin' up the window!
pygame.init()
pygame.font.init()
font = pygame.font.Font("res/Saira-Regular.ttf", 40)
fontbig = pygame.font.Font("res/Saira-Regular.ttf", 55)
fontsmall = pygame.font.Font("res/Saira-Regular.ttf", 27)
screen = pygame.display.set_mode((1280, 720))
done = False
pygame.display.set_caption("Spitfire Alpha 5")
pygame.display.flip()

#Re-collecting those settings!
reallydonewiththis = False
parser = SafeConfigParser()
parser.read("res/options.ini")
carimagepath = parser.get("options", "carimage")
trackstring = parser.get("options", "track")
trackpath = parser.get("options", "trackpath")
track = int(parser.get("cupstats", "track"))
if track == 0:
    score = 0
    place = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 =0
    p5 = 0
    p6 = 0
    p7 = 0
    p8 = 0
    p9 = 0
    p10 = 0
    parser.set("cupstats", "points1"," 0")
    parser.set("cupstats", "points2", "0")
    parser.set("cupstats", "points3", "0")
    parser.set("cupstats", "points4", "0")
    parser.set("cupstats", "points5", "0")
    parser.set("cupstats", "points6", "0")
    parser.set("cupstats", "points7", "0")
    parser.set("cupstats", "points8", "0")
    parser.set("cupstats", "points9", "0")
    parser.set("cupstats", "points10", "0")
    parser.set("cupstats","playerpoints","0")
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    parser.read("res/names.ini")
    randomplacing = random.sample(range(1, 11), 10)
    name1 = parser.get("Main", str(randomplacing[0]))
    name2 = parser.get("Main", str(randomplacing[1]))
    name3 = parser.get("Main", str(randomplacing[2]))
    name4 = parser.get("Main", str(randomplacing[3]))
    name5 = parser.get("Main", str(randomplacing[4]))
    name6 = parser.get("Main", str(randomplacing[5]))
    name7 = parser.get("Main", str(randomplacing[6]))
    name8 = parser.get("Main", str(randomplacing[7]))
    name9 = parser.get("Main", str(randomplacing[8]))
    name10 = parser.get("Main", str(randomplacing[9]))
    parser.read("res/options.ini")
    parser.set("cupstats", "name1", name1)
    parser.set("cupstats", "name2", name2)
    parser.set("cupstats", "name3", name3)
    parser.set("cupstats", "name4", name4)
    parser.set("cupstats", "name5", name5)
    parser.set("cupstats", "name6", name6)
    parser.set("cupstats", "name7", name7)
    parser.set("cupstats", "name8", name8)
    parser.set("cupstats", "name9", name9)
    parser.set("cupstats", "name10", name10)
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
else:
    parser.read("res/options.ini")
    score = parser.get("cupstats", "playerpoints")
    place = parser.get("options", "place")
    fulscr = parser.get("options", "fulscr")
    p1 = parser.get("cupstats", "points1")
    p2 = parser.get("cupstats", "points2")
    p3 = parser.get("cupstats", "points3")
    p4 = parser.get("cupstats", "points4")
    p5 = parser.get("cupstats", "points5")
    p6 = parser.get("cupstats", "points6")
    p7 = parser.get("cupstats", "points7")
    p8 = parser.get("cupstats", "points8")
    p9 = parser.get("cupstats", "points9")
    p10 = parser.get("cupstats", "points10")
    name1 = parser.get("cupstats", "name1")
    name2 = parser.get("cupstats", "name2")
    name3 = parser.get("cupstats", "name3")
    name4 = parser.get("cupstats", "name4")
    name5 = parser.get("cupstats", "name5")
    name6 = parser.get("cupstats", "name6")
    name7 = parser.get("cupstats", "name7")
    name8 = parser.get("cupstats", "name8")
    name9 = parser.get("cupstats", "name9")
    name10 = parser.get("cupstats", "name10")
if fulscr == "True":
    screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
trackimage = pygame.image.load(trackpath)
level = int(parser.get("options", "level"))
points = float(parser.get("options", "points"))
levelpoints = (int(level) + 100) * 202.2
levelpixels = float(points) / levelpoints * 300
track2 = int(trackstring)
clock = pygame.time.Clock()
maxpoints = int(points) + int(score)
trackkey = "track" + str(track2)
car = parser.get("options", "car")
clockspeedstring = parser.get("options", "speed")
playername = parser.get("options", "name")
cupnum = parser.get("cupstats", "cup")
players = int(parser.get("options", "players"))
score2 = 0
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
parser.read("res/tracks.ini")
maxlap = int(parser.get(trackkey, "laps"))
startx = parser.get(trackkey, "startlinex")
starty = parser.get(trackkey, "startliney")
checkpointy = parser.get(trackkey, "checkpointy")
checkpointx = parser.get(trackkey, "checkpointx")



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

def exitthegame():
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
    global cupnum
    global level
    global track2
    #send off the settings
    track += 1
    parser.read("res/tracks.ini")
    tracktogoto2 = parser.get("cup" + str(cupnum), "track" + str(track))
    tracktogoto = "track" + tracktogoto2
    trackpath = parser.get(tracktogoto,"trackpath")
    trackname = parser.get(tracktogoto, "trackname")
    parser.read("res/options.ini")
    parser.set("cupstats","track", str(track))
    parser.set("options", "track", str(tracktogoto2))
    parser.set("options", "trackpath", str(trackpath))
    parser.set("options", "carimage", carimagepath)
    parser.set("options", "speed", str(clockspeed))
    parser.set("options", "racefinsihed", "No")
    parser.set("options", "points", str(round(points, 0)))
    parser.set("options", "level", str(level))
    with open('res/options.ini', 'w') as configfile:
        parser.write(configfile)
    exec(open("race.py").read())


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
            exitthegame()
            reallydonewiththis = True
        #backtostart
        if pressed[pygame.K_RETURN]:
            backtostart()
        #Setting up the labels
        resultsl = font.render("Cup Standings: ", 30, black)
        if players == 2:
            scorelabel2 = "Player 2's score: " + str(score2)
            scorel2 = font.render(scorelabel2, 30, black)
        scorelabel = "Your Current Score: " + str(score)
        scorel = fontbig.render(scorelabel, 30, black)
        firstplacelabel = "1st (" + name1 + ") : " + str(p1)
        secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
        thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
        fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
        fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
        sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
        seventhplacelabel = "7th (" + name7 + ") : " + str(p7)
        eightplacelabel = "8th (" + name8 + ") : " + str(p8)
        ninthplacelabel = "9th (" + name9 + ") : " + str(p9)
        tenthplacelabel = "10th (" + name10 + ") : " + str(p10)
        if place == "11":
            hi = "hi"
        if place == "1":
            firstplacelabel = "1st ("+ playername + ") :  " + score
            secondplacelabel = "2nd (" + name2 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p2)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p3)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p4)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p5)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "2":
            secondplacelabel = "2nd ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p2)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p3)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p4)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p5)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "3":
            thirdplacelabel = "3rd ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p7)
            eightplacelabel = "8th (" + name8 + ") : " + str(p8)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p9)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p10)
        if place == "4":
            fourthplacelabel = "4th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p4)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p5)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "5":
            fifthplacelabel = "5th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p5)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "6":
            sixthplacelabel = "6th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "7":
            seventhplacelabel = "7th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
            eightplacelabel = "8th (" + name8 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "8":
            eightplacelabel = "8th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p7)
            ninthplacelabel = "9th (" + name9 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "9":
            ninthplacelabel = "9th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p7)
            ninthplacelabel = "8th (" + name8 + ") : " + str(p8)
            tenthplacelabel = "10th (" + name10 + ") : " + str(p9)
        if place == "10":
            tenthplacelabel = "10th ("+ playername + ") :  " + score
            firstplacelabel = "1st (" + name1 + ") : " + str(p1)
            thirdplacelabel = "3rd (" + name3 + ") : " + str(p3)
            fourthplacelabel = "4th (" + name4 + ") : " + str(p4)
            fifthplacelabel = "5th (" + name5 + ") : " + str(p5)
            secondplacelabel = "2nd (" + name2 + ") : " + str(p2)
            sixthplacelabel = "6th (" + name6 + ") : " + str(p6)
            seventhplacelabel = "7th (" + name7 + ") : " + str(p7)
            eightplacelabel = "8th (" + name8 + ") : " + str(p8)
            nineplacelabel = "9th (" + name9 + ") : " + str(p9)
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
        startl = fontsmall.render("Press enter to go to the new race", 30, black)
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
