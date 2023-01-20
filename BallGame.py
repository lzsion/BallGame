import pygame
import sys
from Initial import *
from Ball import *
from Board import *
from Key import *
from Display import *
def main():
    disp = Display()
    while True:
        disp.serveBall()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_r:
                    disp = Display()
            disp.keyEvent(event)
        disp.setScreen(screen)
        pygame.display.flip()
        fclock.tick(FPS)
if __name__ == '__main__':
    main()