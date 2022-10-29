# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
window.fill((0, 0, 0))

def draw_robot(times):    
    for i in range(times):
        window.blit(robot, (randint(0,640) , randint(0,480)))            
        

draw_robot(1000)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()