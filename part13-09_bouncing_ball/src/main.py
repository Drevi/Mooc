# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()

x = 50
y = 100
xdir = 1
ydir = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))    

    if x == 0 or x == 640 - ball.get_width():
        xdir = -xdir
    if y == 0 or y == 480 - ball.get_height():
        ydir = -ydir

    x += xdir
    y += ydir    
    
    pygame.display.flip()
        
    clock.tick(144)
