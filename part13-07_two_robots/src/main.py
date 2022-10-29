# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
x1 = 0
y1 = 0
x2 = 0
y2 = 100
direction1 = 1
direction2 = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += direction1
    x2 += direction2

    if x1 == 0 or x1 + width == 640:
        direction1 = -direction1
      
    if x2 == 0 or x2 + width == 640:
        direction2 = -direction2
       
    clock.tick(144)