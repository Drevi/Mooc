# WRITE YOUR SOLUTION HERE:
from random import randint
import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids")

robotimg = pygame.image.load("robot.png")
rockimg = pygame.image.load("rock.png")
clock = pygame.time.Clock()

to_right = False
to_left = False

class Robot:
    def __init__(self):
        self.x = width/2-robotimg.get_width()/2
        self.y = height-robotimg.get_height()/2
    
class Rock:
    def __init__(self):
        self.x = randint(0, 640 - rockimg.get_width())
        self.y = -rockimg.get_height()        
    
robot = Robot()
rocks = [Rock()]
lastrock = 0
points = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True            
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False            
 
        if event.type == pygame.QUIT:
            exit()   

    if to_right:
        robot.x += 2
    if to_left:
        robot.x -= 2    
 
    robot.x = max(robot.x,0)
    robot.x = min(robot.x,width-robotimg.get_width())
    robot.y = max(robot.y,0)
    robot.y = min(robot.y,height-robotimg.get_height())

    screen.fill((0, 0, 0))

    if len(rocks) < 5:
        rock = Rock()
        rock.y = rocks[-1].y -200
        rocks.append(rock)

    for rock in rocks:
        screen.blit(rockimg, (rock.x, rock.y))   
        
        if rock.y > 480 - robotimg.get_height() - rockimg.get_height():
            if rock.x > robot.x - rockimg.get_height() and rock.x < robot.x + robotimg.get_width():
                rocks.remove(rock)
                points += 1
        if rock.y < 480 - rockimg.get_height():
            rock.y += 1
        else:
            exit()    
    
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    screen.blit(text, (500, 10))
    screen.blit(robotimg, (robot.x, robot.y))    
        
    pygame.display.flip()        
    clock.tick(60)

