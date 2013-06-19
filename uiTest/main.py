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
from ui.textbox import *
from ui.textboxgraphics import *
from ui.uicomponent import *
from ui.components.menus import *
from ui.components.panels import *
from ui.components.buttons import *
from ui.components.labels import *
from ui.components.textboxes import *
from ui.screen import *
from uitestevents import *

def main():
    pygame.init()
    freetype.init()
    pygame.display.set_mode((1280, 720))
    ui.init()
    ui.event.start()

    pygame.key.set_repeat(500, 30)

    screen = pygame.display.get_surface()
    area = screen.get_rect()

    clock = pygame.time.Clock()

    ui_screen = Screen()
    
    menu = DefaultMenu(parent = ui_screen, dimensions = (area.width, 150),
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

    tbox = DefaultTextBox(topleft = (300, 20),
                          font_type='/usr/share/fonts/truetype/freefont/FreeSans.ttf',)
                          
    tbox.setVisible(True)
    panel.addComponents([btn, tbox])

    panel1 = DefaultPanel(parent = ui_screen, topleft = (area.width - 300, 0),
                          dimensions = (300, 100), outline_width = 1, border_width = 10)

    label = DefaultLabel((20, 20), "Clicks: 0")
    label.setVisible(True)
    panel1.addComponent(label)
    panel1.setVisible(True)

    c_counter = ClickCounter(label)
    btn.registerEvent(ui.internals.BUTTONPRESSEVENT, c_counter.onButtonPress)

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
                panel.setVisibleRecursive(not panel.getVisible())
            if event.type == KEYDOWN and event.key == K_p:
                for event in ui.internals.event_types:
                    print(ui.internals.event_types[event])
                print('\n\n\n')

        screen.blit(background, area)
        menu.draw()
        panel1.draw()

        pygame.display.flip()

class ClickCounter:
    def __init__(self, label):
        self.count = 0
        self.label = label

    def increment(self):
        self.count += 1

    def getClickCount(self):
        return self.count

    def onButtonPress(self, event):
        self.increment()
        self.label.setText('Clicks: ' + str(self.getClickCount()))





if __name__ == "__main__":
    main()
    ui.event.stop()
    pygame.quit()
