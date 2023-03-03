# File created by: Tim Doan
'''
Goal: create a visually interactive Rock, Paper, Scissors game with goals, rules, freedom, and feedback.
'''
# imported libraries:
# used to delay the code
from time import sleep
# used to generate a random result in rps
from random import randint
# used to give us the ability to animate and make graphics. pygame is a comprehensive game library for use with python.
import pygame as pg
# used to allow us to access folders and directories
import os 
# this stores where I am currently working on the game folders.
gameFolder = os.path.dirname(__file__)
# game settings
width = 2880/4
height = 1920/4
fps = 30
# define colors. these are RGB values. these are tuples, which are immutable
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
# initializes and turns on the game
pg.init()
# allows for the use of sound 
pg.mixer.init()
# shows the rock, paper, and scissors picture
screen = pg.display.set_mode((width, height))
# shows the name of the game at the top of the program
pg.display.set_caption("Rock, Paper, Scissors")
# runs the in-game clock system 
clock = pg.time.Clock()
# stores the pixels for the rock image
rock_image = pg.image.load(os.path.join(gameFolder, "rock.jpg")).convert()
# storing (not the pixels) the dimensions of the image and allows us to change them 
rock_image_rect = rock_image.get_rect()
paper_image = pg.image.load(os.path.join(gameFolder, "paper.jpg")).convert()
paper_image_rect = paper_image.get_rect()
scissors_image = pg.image.load(os.path.join(gameFolder, "scissors.jpg")).convert()
scissors_image_rect = scissors_image.get_rect()

# shows the choices of what could be played
choices = ["rock", "paper", "scissors"]
winCounter = 0
# introduces the game
print("Let's play Rock, Paper, Scissors!")
print("What will you play?")

############# input ##############

# user chooses a choice
def choose():
    # sets the user choice to the value or rock, paper, or scissors
    global user
    if rock_image_rect.collidepoint(mouseCoords):
        print("You chose rock.")
        user = "rock"
    elif paper_image_rect.collidepoint(mouseCoords):
        print("You chose paper.")
        user = "paper"
    elif scissors_image_rect.collidepoint(mouseCoords):
        print("You chose scissors.")
        user = "scissors"
    else: 
        print("You chose nothing.")
        user = "nothing"
# computer chooses a random choice to match up against the user choice
def randomChoice():
    global myChoice
    global computerChoice
    computerChoice = choices[randint(0,2)]
    myChoice = print("I chose", computerChoice + "!")
# compares the user choice to the computer choice
def compare():
    # shows the win conditions along with conditions for the win streak counter 
    global outcome
    if user == computerChoice:
        print("It's a tie!")
        outcome = "tie"
    elif user == "rock" and computerChoice == "scissors":
        print("You win!")
        outcome = "win"
    elif user == "rock" and computerChoice == "paper":
        print("You lose!")
        outcome = "lose"
    elif user == "paper" and computerChoice == "rock":
        print("You win!")
        outcome = "win"
    elif user == "paper" and computerChoice == "scissors":
        print("You lose!")
        outcome = "lose"
    elif user == "scissors" and computerChoice == "paper":
        print("You win!")
        outcome = "win"
    elif user == "scissors" and computerChoice == "rock":
        print("You lose!")
        outcome = "lose"
    elif user == "nothing":
        outcome = "nothing"
        print("You can't play that! No one wins...")
    # conditions for the win streak counter 
    global winCounter
    if outcome == "win":
        winCounter = winCounter + 1
    elif outcome == "lose":
        winCounter = 0
    else:
        pass
    print("Win Streak:",winCounter)
running = True 
# keeps the program running
while running:
    # forces the frame rate to 30 FPS 
    clock.tick(fps)
    # event is anything I do any time with the computer
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        # runs and logs the event for when the mouse is pressed    
        if event.type == pg.MOUSEBUTTONUP:
            # gets and stores the mouse position
            mouseCoords = pg.mouse.get_pos()
            # calls upon the three functions in order: choose, randomChoice, compare
            choose()
            sleep(2)
            randomChoice()
            sleep(1)
            compare()
            sleep(1)

############ update ##############

    paper_image_rect.x = 300
    scissors_image_rect.x = 550

############ draw ###############

    screen.fill(white)
    # rock image is drawn on screen 
    screen.blit(rock_image, rock_image_rect)
    # paper image is drawn on screen 
    screen.blit(paper_image, paper_image_rect)
    # scissors image is drawn on screen 
    screen.blit(scissors_image, scissors_image_rect)
    pg.display.flip()
pg.quit()
