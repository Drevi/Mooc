# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

def draw_robot(times):
    x = 50
    y = 100
    for i in range(0, times):
        window.blit(robot, (x, y))
        x += width + 5
        #y += height + 10
draw_robot(10)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()