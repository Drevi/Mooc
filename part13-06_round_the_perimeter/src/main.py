# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
x = 0
y = 0
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))


    while x < 640 - width:
        window.blit(robot, (x, y))
        pygame.display.flip()
        x += 1
        clock.tick(144)

    while y < 480 - height:
        window.blit(robot, (x, y))
        pygame.display.flip()
        y += 1
        clock.tick(144)

    while x > 0:
        window.blit(robot, (x, y))
        pygame.display.flip()
        x -= 1
        clock.tick(144)

    while y > 0:
        window.blit(robot, (x, y))
        pygame.display.flip()
        y -= 1
        clock.tick(144)
    
    


    