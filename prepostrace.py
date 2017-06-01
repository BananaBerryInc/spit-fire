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
font = pygame.font.SysFont("freesansbold.ttf", 50)
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
score = parser.get("options", "score")
place = parser.get("options", "place")
trackimage = pygame.image.load(trackpath)
track = int(trackstring)
trackkey = "track" + str(track)
car = parser.get("options", "car")
clockspeedstring = parser.get("options", "speed")
clockspeed = int(clockspeedstring)
trackimage = pygame.image.load(trackpath)
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

#Exit Control
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        #Setting up the labels
        resultsl = font.render("Results: ", 30, black)
        scorelabel = "Your Score: " + score
        scorel = font.render(scorelabel, 30, black)
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
        if place == "1":
            firstplacelabel = "1st (You) :  " + score
        if place == "2":
            secondplacelabel = "2nd (You) :  " + score
        if place == "3":
            thirdplacelabel = "3rd (You) :  " + score
        if place == "4":
            fourthplacelabel = "4th (You) :  " + score
        if place == "5":
            fifthplacelabel = "5th (You) :  " + score
        if place == "6":
            sixthplacelabel = "6th (You) :  " + score
        if place == "7":
            seventhplacelabel = "7th (You) :  " + score
        if place == "8":
            eightplacelabel = "8th (You) :  " + score
        if place == "9":
            ninthplacelabel = "9th (You) :  " + score
        if place == "10":
            tenthplacelabel = "10th (You) :  " + score
        firstplacel = font.render(firstplacelabel, 30, black)
        # Rendering and drawing
        screen.fill(lightblue)
        screen.blit(resultsl, (600, 10))
        #ANND, GO!
        pygame.display.flip()
        clock.tick(clockspeed)
