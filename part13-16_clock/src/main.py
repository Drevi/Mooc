# WRITE YOUR SOLUTION HERE:
from datetime import datetime
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
center = (320, 240)


while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
    now = datetime.now()
    pygame.display.set_caption(now.strftime("%H:%M:%S"))
    hours = int(now.strftime("%I")) -15
    minutes = int(now.strftime("%M")) -15
    seconds = int(now.strftime("%S")) -15
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (255, 0, 0), center, 200, 5)
    pygame.draw.circle(window, (255, 0, 0), center, 10)
    hours_tip = (320+math.cos(hours*0.523)*100, 240+math.sin(hours*0.523)*100)
    minutes_tip = (320+math.cos(minutes*0.1046)*140, 240+math.sin(minutes*0.1046)*140)
    seconds_tip = (320+math.cos(seconds*0.1046)*180, 240+math.sin(seconds*0.1046)*180)
    pygame.draw.line(window, (0, 0, 255), center, hours_tip, 4)
    pygame.draw.line(window, (0, 0, 255), center, minutes_tip, 3)
    pygame.draw.line(window, (0, 0, 255), center, seconds_tip, 2)

    

    pygame.display.flip()    
    clock.tick(1)