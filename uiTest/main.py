import pygame, loadimage
from pygame import freetype
from pygame.locals import *
import ui
from ui.menu import *
from ui.nullgraphics import *
from ui.parameters import *
from ui.displaysurface import *
from ui.panelgraphics import *
from ui.panel import *
from ui.button import *
from ui.uicomponent import *
from ui.components.menus import *
from ui.components.panels import *
from ui.components.buttons import *
from uitestevents import *

def main():
    pygame.init()
    freetype.init()
    pygame.display.set_mode((1280, 720))
    ui.init()

    screen = pygame.display.get_surface()
    area = screen.get_rect()

    clock = pygame.time.Clock()
    
    menu = DefaultMenu(dimensions = (area.width, 150),
                       topleft = (0, area.bottom - 150))
    menu.setVisible(True)
    
    panel = DefaultPanel(topleft = (0, 0),
                         dimensions = menu.getAbsoluteRect().size,
                         outline_width = 1,
                         border_width = 10)
    panel.setVisible(True)

    menu.addComponents([panel])

    btn = DefaultButton(topleft = (20, 20), dimensions = (100, 40),
                        color = (100, 128, 160), text_in='Press',
                        font_type='/usr/share/fonts/truetype/freefont/FreeSans.ttf')
    btn.setVisible(True)
    panel.addComponents([btn])

    ui.event.addListener(ui.internals.BUTTONPRESSEVENT, btn, btnPressed)

    background = pygame.Surface((area.width, area.height))
    background.fill((0, 150, 150))
    screen.blit(background, area)
    
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            ui.event.process(event)
            if event.type == QUIT or\
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == KEYDOWN and event.key == K_v:
                screen.blit(background, area)
                panel.setVisible(not panel.getVisible())

        screen.blit(background, area)
        menu.draw()

        pygame.display.flip()
        




if __name__ == "__main__":
    main()
    pygame.quit()
