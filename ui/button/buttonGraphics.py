import pygame
from mydraw import shapes
from mydraw import fill

class DefaultButtonGraphics:
    def __init__(self, params):
        ################ Data Members ################

        self.topleft = params.topleft
        self.dimensions = params.dimensions
        
        self.img_normal = None
        self.img_hover = None
        self.img_pressed = None

        #This is the image that will be drawn.
        #    Will be equal to img_normal by default,
        #    img_hover if the mouse is hovering over the button,
        #    or img_press if it is pressed.
        self.image = None

        self.rect = None

        self.color = params.color
        self.highlight_color = params.highlight_color

        ################ Data Members ################
        
        self.generateImages()

        self.image = self.img_normal

        self.rect = self.img_normal.get_rect()
        self.rect.topleft = self.topleft

    def setState(self, state):
        if state == 'normal':
            self.image = self.img_normal
        elif state == 'hover':
            self.image = self.img_hover
        elif state == 'pressed':
            self.image = self.img_pressed

    def generateImages(self):
        self.color = (self.color[0], self.color[1], self.color[2], 255)
        colors = [self.color] * 4

        if not self.highlight_color:
            self.highlight_color = (self.color[0] + 60, self.color[1] + 60,
                                    self.color[2] + 60, 255)
            self.highlight_color = fill.fixColor(self.highlight_color)
        else:
            self.highlight_color = (self.highlight_color[0], self.highlight_color[1],
                                    self.highlight_color[2], 255)

        line_dark = (self.color[0] - 60, self.color[1] - 60,
                     self.color[2] - 60, 255)
        line_dark = fill.fixColor(line_dark)
        line_light = (200, 200, 200, 255)

        color_dark = (self.color[0] - 40, self.color[1] - 40,
                      self.color[2] - 40, 255)

        color_light = (self.color[0] + 40, self.color[1] + 40,
                       self.color[2] + 40, 255)
        
        radius = int(self.dimensions[1] / 5)
        self.img_normal = shapes.drawRoundedRect(\
            self.dimensions[0] - 2 * radius,
            self.dimensions[1] - 2 * radius,
            radius, colors, 4)

        fill.fillVerticalGradient(self.img_normal, color_light, color_dark,
                                  4, self.dimensions[1] - 5)

        colors = [self.highlight_color] * 4

        self.img_hover = shapes.drawRoundedRect(\
            self.dimensions[0] - 2 * radius,
            self.dimensions[1] - 2 * radius,
            radius, colors, 4)

        fill.fillVerticalGradient(self.img_hover, color_light, color_dark,
                                  4, self.dimensions[1] - 5)

        self.img_pressed = shapes.drawRoundedRect(\
            self.dimensions[0] - 2 * radius,
            self.dimensions[1] - 2 * radius,
            radius, colors, 4)

        fill.fillVerticalGradient(self.img_pressed, color_dark, color_light,
                                  4, self.dimensions[1] - 5)

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.image, self.rect, area)






















