# Basic Movement and Key Presses
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# start pygame module
pygame.init()

# make a window
win = pygame.display.set_mode((500,500))
pygame.time.delay(100)
pygame.display.set_caption("Ricky Rectangle")

#Spawn character
# where spawn
x = 50
y = 50
# size of character
width = 40
height = 60
# speed of character
vel = 5


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    # # this cleans up after the Character
    # win.fill((0, 0, 0))

    # Draw our character
    pygame.draw.rect(win, (255, 255, 0), (x, y , width, height) )
    # win = where do you want to draw this rect()
    # (255, 0, 0) = RBG color 
    # (x, y , width, height) = rectangle attributes
    pygame.display.update()

# brew



pygame.quit()