import pygame, math
from pygame.locals import *

def drawRoundedRect(width, height, radius, colors, border_width=1, surface=None):
    if surface:
        surf = surface
    else:
        surf = pygame.Surface((width + 2 * radius, height + 2 * radius),
                              flags = SRCALPHA)
    rect = surf.get_rect()
    
    #Draw corners:
    drawCircleSegment((radius - 1, radius - 1), radius, 90, 180, surf, colors[0])
    drawCircleSegment((rect.width - radius, radius - 1), radius, 0, 90, surf, colors[0])
    drawCircleSegment((radius - 1, rect.height - radius),
                      radius, 180, 270, surf, colors[0])
    drawCircleSegment((rect.width - radius, rect.height - radius),
                      radius, 270, 360, surf, colors[0])

    #Draw sides:
    drawLineSegment((radius - 1, 0), (radius + width - 1, 0), surf, colors[0])
    drawLineSegment((0, radius - 1), (0, radius + height - 1), surf, colors[0])
    drawLineSegment((rect.width - 1, radius - 1), (rect.width - 1, radius + height - 1),
                    surf, colors[0])
    drawLineSegment((radius - 1, rect.height - 1), (radius + width - 1, rect.height - 1),
                    surf, colors[0])

    #Thicken border:
    for i in range(1, border_width):
        for y in range(i, rect.height - i):
            x = 0
            
            #Find the shape's border
            while surf.get_at((x, y)) not in colors and x < rect.width:
                x += 1

            #Find the inside of the shape
            while surf.get_at((x, y)) in colors and x < rect.width:
                x += 1

            #Fill the top and bottom rows
            if y == i or y == rect.height - i - 1:
                while surf.get_at((x, y)) not in colors and x < rect.width:
                    surf.set_at((x, y), colors[i])
                    x += 1
            #Fill the first spot inside the border
            else:
                surf.set_at((x, y), colors[i])

                #Find the other side of the border
                while surf.get_at((x + 1, y)) not in colors and x + 1 < rect.width:
                    x += 1

                #Fill the first spot inside the far side of the border
                surf.set_at((x, y), colors[i])
    
    return surf

def drawCircleSegment(center, radius, startAngle, endAngle, surf, color, step=1):
    cx = center[0]
    cy = center[1]
    for i in range(startAngle, endAngle, step):
        surf.set_at((cx + int(math.cos(math.radians(i)) * radius),
                     cy - int(math.sin(math.radians(i)) * radius)), color)
        
def drawLineSegment(start, end, surf, color):
    if start[0] == end[0]:
        if end[1] < start[1]:
            tmp = end
            end = start
            start = tmp
        x = start[0]
        for y in range(start[1], end[1] + 1):
            surf.set_at((x, y), color)
    else:

        if end[0] < start[0]:
            tmp = end
            end = start
            start = tmp
        
        a = end[1] - start[1]
        b = start[0] - end[0]
        c = start[0] * end[1] - end[0] * start[1]

        for x in range(start[0], end[0] + 1):
            y = round((c - (a * x)) / b)
            surf.set_at((x, y), color)
