from Content import *
from Config import *
import pygame
import json
import math

def playDraw():
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouseX, mouseY = pygame.mouse.get_pos()
      playX = 825
      playY = 425
      playW = 350
      playH = 300
      #Play button Collsion
      if mouseX > playX and mouseX < playX + playW and mouseY > playY and mouseY < playY + playH:
        print("The Play Button is Pressed!")
        titlescreen.isActive = False
        mapObj.isActive = True



def backDraw():
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouseX, mouseY = pygame.mouse.get_pos()
      arrowX = 200
      arrowY = 300
      arrowW = 200
      arrowH = 150

      if mouseX > arrowX and mouseX < arrowX + arrowW and mouseY > arrowY and mouseY < arrowY + arrowH:
        print("the Back arrow has been clicked")
        stg.isActive = False
        titlescreen.isActive = True
      
      
      


def saveDraw():
  for event in pygame.event.get():
    mouseX, mouseY = pygame.mouse.get_pos()
    saveW = 100
    saveH = 100
    saveX = 700
    saveY = 50
    if (mouseX > saveX and mouseX < saveX + saveW and mouseY > saveY
        and mouseY < saveY + saveH) and stg.isActive == True:
      print("Saved the Game!")
      saveGame()





class Player():

  def __init__(self, startX, startY):
    self.x = startX
    self.y = startY
    self.xspeed = 0
    self.yspeed = 0
    self.walkAnimTimerMax = 5
    self.walkAnimTimer = self.walkAnimTimerMax
    self.spriteDir = 0 #UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3
    self.currentPic = 0

  def plyrdraw(self):
  
    DISPLAYSURF.blit(charSprites[self.spriteDir][self.currentPic],(playerObj.x,playerObj.y))

    if self.walkAnimTimer <= 0:
      self.walkAnimTimer = self.walkAnimTimerMax
      if self.currentPic >= 2:
        self.currentPic = 0
      else:
        self.currentPic += 1
    #if self.spriteDir == 0:
      #self.currentPic = 0

    #elif self.spritedir == "DOWN":
      #self.currentpic = 3


  def move(self, keys):
    if keys[pygame.K_UP]: #UP MOVEMENT
      self.walkAnimTimer -= 1
      self.spriteDir = 0
      self.y -= 5

    elif keys[pygame.K_DOWN]: #DOWN MOVEMENT
      self.walkAnimTimer -= 1
      self.spriteDir = 1
      self.y += 5

    elif keys[pygame.K_LEFT]: #LEFT MOVEMENT
      self.walkAnimTimer -= 1
      self.spriteDir = 2
      self.x -= 5

    elif keys[pygame.K_RIGHT]: #RIGHT MOVEMENT
      self.walkAnimTimer -= 1
      self.spriteDir = 3
      self.x += 5

    else:
      self.walkAnimTimer = self.walkAnimTimerMax


  def canMove(self, keys, map):
    if keys[pygame.K_UP] and mapObj.map[self.y-1][self.x] != "R": #UP MOVEMENT
      return True

    elif keys[pygame.K_DOWN] and mapObj.map[self.y+1][self.x] != "R": #DOWN MOVEMENT
      return True

    elif keys[pygame.K_LEFT] and mapObj.map[self.y][self.x-1] != "R": #LEFT MOVEMENT
      return True

    elif keys[pygame.K_RIGHT] and mapObj.map[self.y][self.x+1] != "R": #RIGHT MOVEMENT
      return True

    else:
      return False

    

playerObj = Player(0,0)


class Title():

  def __init__(self):
    self.isActive = True


class settingsmenu():

  def __init__(self):
    self.isActive = False


stg = settingsmenu()


class Map():

  def __init__(self):
    self.map = mapMatrix
    self.isActive = False

  def drawMap(self):
    if self.isActive == True and stg.isActive == False:
      DISPLAYSURF.fill(BEIGE)
      for y in range(len(self.map)):
        for x in range(len(self.map[y])):
          #DISPLAYSURF.blit(rocksprite,(playerObj.x*50,(playerObj.y*50) - 10)) #Player model temp blit as rock
          playerObj.plyrdraw()
          if self.map[y][x] == "G":
            DISPLAYSURF.blit(grassSprite, (x * 50, y * 50))
          elif self.map[y][x] == "R":
            DISPLAYSURF.blit(rocksprite,(x*50,y*50))

          elif self.map[y][x] == "T":
            DISPLAYSURF.blit(treeSprite,(x*50,y*50))

          #elif self.map[(math.ceil(playerObj.y))][(math.ceil(playerObj.x))] == "G":

         # print(playerObj.x,playerObj.y)
          #print(self.map[(math.ceil(playerObj.y))][(math.ceil(playerObj.x))])
            


#Title Screen
pygame.display.set_icon(sigma)
pygame.display.set_caption("Legends of Eddie")
titlescreen = Title()


def titledraw():
  if titlescreen.isActive == True:
    #DISPLAYSURF.fill(BLUE)
    DISPLAYSURF.blit(img1, (scrollobj.img1x, scrollobj.img1y))
    DISPLAYSURF.blit(img2, (scrollobj.img2x, scrollobj.img2y))
    DISPLAYSURF.blit(logo, (775, 100))
    DISPLAYSURF.blit(playbutton, (825,400))
    titlemusic.set_volume(gamesettings["musicvolume"])
    pygame.mixer.Sound.play(titlemusic)
    #print("True!")


buttonh = 50
buttonw = 50
buttonrect = playbutton.get_rect()
buttonrect = pygame.Rect(300, 400, 300, 100)

bArrowRect = backArrow.get_rect()



mapFile = "Map.txt"
mapReading = open(mapFile, "r")
mapMatrix = []
line = " "
while line != "":
  line = mapReading.readline()
  line = line[0:-1]
  lineList = list(line)
  if lineList != []:  #FAIL SAFE
    mapMatrix.append(lineList)
mapObj = Map()


class dialouge():
  def __init__(self):
    self.speechsequence = False

  def speech(self,text):
    if self.speechsequence == True:
      DISPLAYSURF.blit(textbox,(200,200))



class imgscroll():
  def __init__(self):
    self.img1w = 1920
    self.img1h = 1080
    self.img2w = 1980
    self.img2h = 1080
    self.img1x = 0
    self.img1y = 0
    self.img2x = -1920
    self.img2y = 0
    self.scrlspd = 5

  def bckscrl(self):
    self.img1x += self.scrlspd
    self.img2x += self.scrlspd
    if self.img1x > self.img1w:
      self.img1x = -self.img1w
      self.img2x = 0
    elif self.img2x > self.img2w:
      self.img2x = -self.img2w
      self.img1x = 0

scrollobj = imgscroll()

class slider:
  def __init__(self, pos: tuple, size: tuple, iv: float, min: int, max: int):
    self.pos = pos
    self.size = size

    self.sliderLeft = self.pos[0] - (size[0]//2)
    self.sliderRight = self.pos[0] + (size[0]//2)
    self.sliderTop = self.pos[1] - (size[1]//2)

    self.min = min
    self.max = max

    self.iv = (self.sliderRight - self.sliderLeft) * iv

    self.container = pygame.Rect(self.sliderLeft, self.sliderTop, self.size[0], self.size[1])
    self.button = pygame.Rect (self.sliderLeft + iv - 5, self.sliderTop, 10, self.size[1])

    self.dragging = False


  def sliderDraw(self):
    pygame.draw.rect(DISPLAYSURF, GREEN, self.container)
    pygame.draw.rect(DISPLAYSURF, BLUE, self.button)

  def moveSlider(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == pygame.BUTTON_LEFT:
        if self.button.collidepoint(event.pos):
          self.dragging = True
          
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == pygame.BUTTON_LEFT:
        self.dragging = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
      if self.dragging:
        mousex = event. pos[0]
        newButton = mousex - self.container.left
        newButton = max(0,newButton)
        newButton = min(newButton, self.container.width - self.button.width)
        self.buttonX = self.container.left + newButton
        

sliderObj = slider( (825,425), (100, 30), (0.5), 0, 1)

def drawSettings():
  if stg.isActive == True:
    DISPLAYSURF.fill(RED)
    DISPLAYSURF.blit(saveicon, (700, 50))
    DISPLAYSURF.blit(backArrow, (200, 300))
    sliderObj.sliderDraw()
    pygame.display.update()

    
