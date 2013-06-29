import pygame
from pygame import freetype

def getSizeOfText(text, font_size, font_type, bold, italic, underline):
    font = pygame.font.Font(font_type, font_size)
    font.set_bold(bold)
    font.set_italic(italic)
    font.set_underline(underline)
    
    return font.size(text)

def getTextHeight(font_size, font_type, bold, italic, underline):
    font = pygame.font.Font(font_type, font_size)
    font.set_bold(bold)
    font.set_italic(italic)
    font.set_underline(underline)

    return font.get_height()

def isEdgePixel(image, x, y):

    kernelX = [[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]]

    kernelY = [[1, 2, 1],
               [0, 0, 0],
               [-1, -2, -1]]

    valX = 0
    valY = 0
    for row in range(y - 1, y + 2):
        for col in range(x - 1, x + 2):

            kernel_row = row - (y - 1)
            kernel_col = col - (x - 1)
            
            color = image.get_at((col, row))
            red = color[0]
            green = color[1]
            blue = color[2]
            valX += ((0.2126*red) + (0.7152*green) + (0.0722*blue))\
                    * kernelX[kernel_row][kernel_col]
            valY += ((0.2126*red) + (0.7152*green) + (0.0722*blue))\
                    * kernelY[kernel_row][kernel_col]

    return abs(valX) > 0 or abs(valY) > 0

def smoothEdges(image, alpha):
    width, height = image.get_rect().size
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if isEdgePixel(image, col, row):
                color = image.get_at((col, row))
                p = (color[0], color[1], color[2], alpha)
                image.set_at((col, row), p)

def cleanImage(image, distance):
    key = image.get_colorkey()
    if key:
        width, height = image.get_rect().size
        k = 0
        for i in range(height):
            for j in range(width):
                p = image.get_at((j, i))
                if (p[0] >= key[0] - distance and p[1] >= key[1] - distance and
                    p[2] >= key[2] - distance) and (p[0] <= key[0] + distance and
                    p[1] <= key[1] + distance and p[2] <= key[2] + distance):
                    image.set_at((j, i), key)
                    k += 1

def cleanImage2(image, color, distance=0):
    key = image.get_colorkey()
    if key:
        width, height = image.get_rect().size
        k = 0
        for i in range(height):
            for j in range(width):
                p = image.get_at((j, i))
                if (not (p[0] >= color[0] - distance and p[0] <= color[0] + distance) or
                    not (p[1] >= color[1] - distance and p[1] <= color[1] + distance) or
                    not (p[2] >= color[2] - distance and p[2] <= color[2] + distance)):
                    image.set_at((j, i), key)
                    k += 1

def cleanImage3(image):
    key = image.get_colorkey()
    if key:
        width, height = image.get_rect().size
        k = 0
        for i in range(height):
            for j in range(width):
                p = image.get_at((j, i))
                if True:
                    image.set_at((j, i), key)
                    k += 1















