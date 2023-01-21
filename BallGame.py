import pygame
import sys
from Initial import *
from Ball import *
from Board import *
from Key import *
from Display import *
class BallGame():
    def __init__(self):       
        self.disp = Display()
        while True:
            self.disp.serveBall()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_r:
                        disp = Display()
                self.disp.keyEvent(event)
            self.disp.setScreen(screen)
            pygame.display.flip()
            fclock.tick(FPS)