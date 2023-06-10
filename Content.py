from Config import *
import pygame

titlescreentxt = titlefont.render("Welcome to the game!",200,BLACK)

#Play Button
playX = 825 
playY = 425
playW = 350
playH = 300
playbutton = pygame.image.load("Images/playbutton.png")
playbutton = pygame.transform.scale(playbutton,(playW,playH))

#Save Icon
saveicon = pygame.image.load("Images/floppy.png")
saveicon = pygame.transform.scale(saveicon,(100,100))
saveW = 100
saveH = 100
saveX = 700
saveY = 50

#BackArrow
backArrow = pygame.image.load("Images/BackArrow.png")
backArrow = pygame.transform.scale(backArrow,(200,150))

#Grass
grassSprite = pygame.image.load("Images/grasssprite.png")
grassSprite = pygame.transform.scale(grassSprite,(50,50))

#Sigma
sigma = pygame.image.load("Images/Sigma.png")

#Rock
rocksprite = pygame.image.load("Images/boulder.png")
rocksprite = pygame.transform.scale(rocksprite,(50,50))

#Tree
treeSprite = pygame.image.load("Images/tree1.png")
treeSprite = pygame.transform.scale(treeSprite,(50,50))

#Character Sprites:

forwardsidle = pygame.image.load("Images/EddieSprites/back-idle.png")
forwardsidle = pygame.transform.scale(forwardsidle,(50,50))

forwardstep1 = pygame.image.load("Images/EddieSprites/BW1.png")
forwardstep1 = pygame.transform.scale(forwardstep1,(50,50))

forwardstep2 = pygame.image.load("Images/EddieSprites/BW2.png")
forwardstep2 = pygame.transform.scale(forwardstep2,(50,50))

#nextUP = [1,2,3,1,1,1,1,1]
#nextDOWN = [4,5,6,7,4,]

backwardidle = pygame.image.load("Images/EddieSprites/F_Idle.png")
backwardidle = pygame.transform.scale(backwardidle,(50,50))
backwardstep1 = pygame.image.load("Images/EddieSprites/FW1.png")
backwardstep1 = pygame.transform.scale(backwardstep1,(50,50))
backwardstep2 = pygame.image.load("Images/EddieSprites/FW2.png")
backwardstep2 = pygame.transform.scale(backwardstep2,(50,50))

leftidle = pygame.image.load("Images/EddieSprites/L_idle.png")
leftidle = pygame.transform.scale(leftidle, (75,75))
leftstep1 = pygame.image.load("Images/EddieSprites/L_walk.png")
leftstep1 = pygame.transform.scale(leftstep1,(75,75))
leftstep2 = pygame.image.load("Images/EddieSprites/L_walk2.png")
leftstep2 = pygame.transform.scale(leftstep2,(75,75))

rightidle = pygame.image.load("Images/EddieSprites/R_idle.png")
rightidle = pygame.transform.scale(rightidle, (100,75))
rightstep1 = pygame.image.load("Images/EddieSprites/R_walk.png")
rightstep1 = pygame.transform.scale(rightstep1,(100,75))
rightstep2 = pygame.image.load("Images/EddieSprites/R_walk2.png")
rightstep2 = pygame.transform.scale(rightstep2,(100,75))

charSprites = [[forwardsidle,forwardstep1,forwardstep2], [backwardidle, backwardstep1, backwardstep2], [leftidle, leftstep1, leftstep2], [rightidle, rightstep1, rightstep2]]

#Text Box
textbox = pygame.image.load("Images/textbox.png")
textbox = pygame.transform.scale(textbox,(200,200))

#Title Screen Music
pygame.mixer.init()
titlemusic = pygame.mixer.Sound("Audio/Music/LoE_sample.mp3")

#Title Screen Background
img1 = pygame.image.load("Images/Backgrounds/firsthalfbg.png")
img1 = pygame.transform.scale(img1,(1920,1080))
img2 = pygame.image.load("Images/Backgrounds/2halfbg.png")
img2 = pygame.transform.scale(img2,(1920,1080))

def imgscroll():
  img1w = 1920
  img1h = 1080
  img2w = 1980
  img2h = 1080
  img1x = 0
  img1y = 0
  img2x = -1920
  img2y = 0
  scrlspd = 5
  img1x += scrlspd
  img2x += scrlspd
  if img1x > img1w:
    img1x = -img1w
    img2x = 0
  elif img2x > img2w:
    img2x = -img2w
    img1x = 0

#Game Logo
logo = pygame.image.load("Images/logo.png")
logo = pygame.transform.scale(logo,(400,400))