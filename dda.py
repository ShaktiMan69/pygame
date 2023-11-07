#!/usr/bin/python3
#me@jugalnaik.in

import sys
import pygame

def dda_algorithm(screen, x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        screen.set_at((int(x), int(y)), (min(x, 255), min(y, 255), min(x*y, 255)))
        x += x_increment
        y += y_increment
        pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((640, 480))
color = (255, 255, 255)
x1, y1 = 100, 100
x2, y2 = 500, 300
dda_algorithm(screen, x1, y1, x2, y2, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x2, y2 = pygame.mouse.get_pos()
            dda_algorithm(screen, x1, y1, x2, y2, color)
            x1, y1 = x2, y2
