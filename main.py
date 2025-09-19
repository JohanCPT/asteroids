import pygame
from constants import *

def main():
    pygame.init()
    #print("Starting Asteroids!")
    #print(F"Screen width:{SCREEN_WIDTH:>5}")
    #print(F"Screen height:{SCREEN_HEIGHT:>4}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    gameclock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
               
        screen.fill(black)
        pygame.display.flip()
        dt = gameclock.tick(60)/1000

if __name__ == "__main__":
    main()
