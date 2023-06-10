import json
import pygame
import time

#Screen Dimensions
WIDTH = 1920
HEIGHT = 1080

#Screen Variable
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

#Font
pygame.font.init()
titlefont = pygame.font.SysFont("Ariel Black",40)

# Colours 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED =(255,0,0)
GREEN =(0,255,0)
YELLOW = (255,255,0)
ORANGE = (255, 102, 0)
BLUE = (0,0,255)
BROWN = (26, 9, 0)
BEIGE = (139,101,8)

#Controls
#mouseX,mouseY = pygame.mouse.get_pos()
keys = pygame.key.get_pressed()


#JSON SAVING
gamesettings = {"Life":3,
                "Speed":1,
                "Arrows":2,
                "pldmg":1,
                "sfxvol": 1,
                "musicvolume":1
               }

def saveGame():
  with open("testfile.txt",'w') as savefile:
    json.dump(gamesettings,savefile)
    savefile.close()

#JSON LOADING


#Clock
clock = pygame.time.Clock()
FPS = 60