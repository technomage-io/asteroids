# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    while True: 
        pygame.time.Clock().tick(60)
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()
        
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
               return     
        
























if __name__ == "__main__":
    main()