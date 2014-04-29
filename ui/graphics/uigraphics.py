class UIGraphics:
    def __init__(self, params):
        pass

    def draw(self, display_surface, area=None):
        display_surface.displayImage(self.image, self.rect, area)
