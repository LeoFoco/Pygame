#All the imports
import pygame
from Drawing import *
#Displays the screen
WIDTH = 1500
HEIGHT = 750
win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
#The clock
clock = pygame.time.Clock()

#Sets the name of the window
pygame.display.set_caption("First Game")
load = pygame.image.load

#The music
#The -1 means it is on a loop if not the song would stop after the first time
#music = pygame.mixer.music.load('Music/music.mp3')
#pygame.mixer.music.play(-1)

#I think the animation it starts at (Don't quote me tho)
backgroundState = 0

#The score (Displayed top right)
score = 0

#Colors
White = (255,255,255)
Black = (0,0,0)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
