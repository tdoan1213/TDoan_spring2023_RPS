# File created by: Tim Doan

# imported libraries:
# used to delay the code
from time import sleep
# used to generate a random result in rps
from random import randint
# used to give us the ability to animate and make graphics. pygame is a comprehensive game library fro use with python.
import pygame as pg
# used to allow us to access folders and directories
import os 
# this stores where I am currently working on the game folders.
gameFolder = os.path.dirname(__file__)
# game settings
width = 360
height = 480
fps = 30
# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.init()
# allows for the use of sound 
pg.mixer.init()

screen = pg.display.set_mode((width, height))
pg.display.set_caption("rock, paper, scissors")
clock = pg.time.Clock()
my_image = pg.image.load(os.path.join(gameFolder, "download.jpg")).convert()
my_image_rect = my_image.get_rect()

running = True 
# keeps the program running
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    # get user input

    # update

    # draw
    screen.fill(black)
    screen.blit(my_image, my_image_rect)

    pg.display.flip()