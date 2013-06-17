import pygame
import shapes
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_mode((1280, 720))

    screen = pygame.display.get_surface()
    area = screen.get_rect()

    clock = pygame.time.Clock()

    colors = [(255, 200, 125, 100), (255, 200, 125, 150),
              (255, 200, 125, 200), (255, 200, 125, 255)]

    #shape = shapes.drawRoundedRect(200, 100, 30, (0, 200, 125, 255))
    shape = shapes.drawRoundedRect(125, 20, 10, colors, 4)
    srect = shape.get_rect()
    srect.topleft = (100, 100)

    screen.blit(shape, srect)
    pygame.display.flip()

    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or\
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
