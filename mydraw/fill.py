import pygame, math
from pygame.locals import *

def fillVerticalGradient(surf, start_color, end_color, start_row, end_row, bg_color=None):
    num_rows = end_row - start_row

    start_color = fixColor(start_color)
    end_color = fixColor(end_color)

    color = list(start_color)

    '''print(start_row)
    print(end_row)
    print(num_rows)
    print(start_color)
    print(end_color)'''

    if not bg_color:
        bg_color = surf.get_at((0, 0))

    change_red = int((end_color[0] - start_color[0]) / num_rows)
    change_green = int((end_color[1] - start_color[1]) / num_rows)
    change_blue = int((end_color[2] - start_color[2]) / num_rows)
    change_alpha = int((end_color[3] - start_color[3]) / num_rows)

    remainder_red = (end_color[0] - start_color[0]) - change_red * num_rows
    remainder_green = (end_color[1] - start_color[1]) - change_green * num_rows
    remainder_blue = (end_color[2] - start_color[2]) - change_blue * num_rows
    remainder_alpha = (end_color[3] - start_color[3]) - change_alpha * num_rows

    rect = surf.get_rect()

    '''print("Remainders: ", (remainder_red, remainder_green,
                           remainder_blue, remainder_alpha))'''

    for y in range(start_row, end_row + 1):
        '''print(y, ": ",color)'''
        x = 0

        #Find the shape's border
        while surf.get_at((x, y)) == bg_color and x < rect.width:
            x += 1

        #Find the inside of the shape
        while surf.get_at((x, y)) != bg_color and x < rect.width:
            x += 1

        #Fill the row
        while surf.get_at((x, y)) == bg_color and x < rect.width:
            surf.set_at((x, y), tuple(color))
            x += 1

        color[0] += change_red
        color[1] += change_green
        color[2] += change_blue
        color[3] += change_alpha

        if y - start_row < abs(remainder_red):
            if (end_color[0] - start_color[0]) > 0:
                color[0] += 1
            else:
                color[0] -= 1
        if y - start_row < abs(remainder_green):
            if (end_color[1] - start_color[1]) > 0:
                color[1] += 1
            else:
                color[1] -= 1
        if y - start_row < abs(remainder_blue):
            if (end_color[2] - start_color[2]) > 0:
                color[2] += 1
            else:
                color[2] -= 1
        if y - start_row < abs(remainder_alpha):
            if (end_color[3] - start_color[3]) > 0:
                color[3] += 1
            else:
                color[3] -= 1

def fixColor(color):
    color = list(color)

    for i in range(len(color)):
        if color[i] < 0:
            color[i] = 0
        elif color[i] > 255:
            color[i] = 255

    return tuple(color)






















