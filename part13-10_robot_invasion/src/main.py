# WRITE YOUR SOLUTION HERE:
from random import randint, choice
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robotimg = pygame.image.load("robot.png")
clock = pygame.time.Clock()

class Robot:
    def __init__(self):
        self.x = randint(0, 640 - robotimg.get_width())
        self.y = -robotimg.get_height()
        self.direction = choice([1, -1])
    def reset(self):
        self.x = randint(0, 640 - robotimg.get_width())
        self.y = -robotimg.get_height()
        self.direction = choice([1, -1])

robots = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()   

    window.fill((0, 0, 0))

    if randint(0,100) == 13 and len(robots) < 20:
        robots.append(Robot())

    for robot in robots:
        window.blit(robotimg, (robot.x, robot.y))   

        if robot.y < 480 - robotimg.get_height():
            robot.y += 1
        else:   
            robot.x += robot.direction
            if robot.x < 0 - robotimg.get_width() or robot.x > 640:
                robot.reset()
        
    pygame.display.flip()
        
    clock.tick(60)