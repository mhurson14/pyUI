import pygame
from pygame import freetype
from pygame.locals import *
from ui import *
import time

class DefaultTextGraphics:
    def __init__(self, params):

        self.text = params.text

        self.font_size = params.font_size
        self.font_type = params.font_type
        self.font_color = params.font_color

        #booleans
        self.bold = params.bold
        self.italic = params.italic
        self.underline = params.underline

        self.font = None

        self.dimensions = params.dimensions
        self.topleft = params.topleft
        self.rect = pygame.Rect(self.topleft[0], self.topleft[1],
                                self.dimensions[0], self.dimensions[1])
        self.left_images = []
        self.selected_images = []
        self.right_images = []

        self.font = pygame.font.Font(self.font_type, self.font_size)

        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
        self.font.set_underline(self.underline)

        self.setSelected(0, 0)

    def setText(self, text):
        self.text = text
        self.setSelected(0, 0)

    def getRect(self):
        return self.rect

    def setRect(self, rect):
        self.rect = rect

    def setSelected(self, start, end):
        
        self.left_images = []
        self.selected_images = []
        self.right_images = []
        
        left = self.text[:start]
        selected = self.text[start:end]
        right = self.text[end:]
        
        if len(left) > 0:
            leftChars = int(15000 // self.font_size)
            numLeft = int(len(left) // leftChars) + 1
            for i in range(numLeft):
                image_left = self.font.render(left[i * leftChars:(i + 1) * leftChars],
                                              True, self.font_color)
                rect_left = image_left.get_rect()
                rect_left.top = self.topleft[1]
                if i == 0:
                    rect_left.left = self.topleft[0]
                else:
                    rect_left.left = self.left_images[i - 1][1].right
                self.left_images.append((image_left, rect_left))
                if rect_left.right > self.rect.right:
                    break
        if len(selected) > 0:
            selectedChars = int(15000 // self.font_size)
            numSelected = int(len(selected) // selectedChars) + 1
            for i in range(numSelected):
                image_selected = self.font.render(\
                                 selected[i * selectedChars:(i + 1) * selectedChars],
                                                  True, (255, 255, 255, 255),
                                                  (100, 200, 100, 255))
                rect_selected = image_selected.get_rect()
                rect_selected.top = self.topleft[1]
                if i == 0:
                    if len(self.left_images) > 0:
                        rect_selected.left = self.left_images[-1][1].right
                    else:
                        rect_selected.left = self.topleft[1]
                else:
                    rect_selected.left = self.selected_images[i - 1][1].right
                self.selected_images.append((image_selected, rect_selected))
                if rect_selected.right > self.rect.right:
                    break
        if len(right) > 0:
            rightChars = int(15000 // self.font_size)
            numRight = int(len(right) // rightChars) + 1
            for i in range(numRight):
                image_right = self.font.render(right[i * rightChars:(i + 1) * rightChars],
                                               True, self.font_color)
                rect_right = image_right.get_rect()
                rect_right.top = self.topleft[1]
                if i == 0:
                    if len(self.selected_images) > 0:
                        rect_right.left = self.selected_images[-1][1].right
                    elif len(self.left_images) > 0:
                        rect_right.left = self.left_images[-1][1].right
                    else:
                        rect_right.left = self.topleft[1]
                else:
                    rect_right.left = self.right_images[i - 1][1].right
                self.right_images.append((image_right, rect_right))
                if rect_right.right > self.rect.right:
                    break

    def getMetrics(self):
        return self.font.metrics(self.text)

    def draw(self, display_surface, area=None):
        for image in self.left_images:
            if self.rect.colliderect(image[1]):
                left = image[1].left - self.rect.left
                top = image[1].top
                display_surface.displayImage(image[0], (left, top))
        for image in self.selected_images:
            if self.rect.colliderect(image[1]):
                left = image[1].left - self.rect.left
                top = image[1].top
                display_surface.displayImage(image[0], (left, top))
        for image in self.right_images:
            if self.rect.colliderect(image[1]):
                left = image[1].left - self.rect.left
                top = image[1].top
                display_surface.displayImage(image[0], (left, top))

























