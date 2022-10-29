# WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
robotimg = pygame.image.load("robot.png")
clock = pygame.time.Clock()


class Robot:
    def __init__(self, angle):
        self.angle = angle

    def x(self):
        return 320+math.cos(self.angle)*100-50/2

    def y(self):
        return 240+math.sin(self.angle)*100-86/2

robots = []
for i in range(10):
    robots.append(Robot(0.628*i))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for robot in robots:
            window.blit(robotimg, (robot.x(), robot.y()))
            robot.angle += 0.01    
        
    pygame.display.flip()
        
    clock.tick(144)




