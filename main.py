import pygame
import time
import math
import random
import json 
from Classes_Functions import *
from Config import *
from Content import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60

gameOn = True
while gameOn:

  keys = pygame.key.get_pressed()
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      gameOn = False
      
    if event.type == pygame.MOUSEBUTTONDOWN:
      sliderObj.moveSlider(event)
      if stg.isActive:
        drawSettings()
      else:
        playDraw()
      
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
          print("Printing your mom")
          titlescreen.isActive = False
          stg.isActive = True
          
          
          
  titledraw()
  drawSettings()
  mapObj.drawMap()
  backDraw()
  if playerObj.canMove(keys, mapObj):
    playerObj.move(keys)
  saveDraw()
  scrollobj.bckscrl()

  if stg.isActive:
    drawSettings()
  
  
  pygame.display.update()
  clock.tick(FPS)

pygame.quit()