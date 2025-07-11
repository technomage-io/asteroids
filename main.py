# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)


def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")

    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
   
    player = Player(x,y)
    asteroid_field = AsteroidField() 
    clock = pygame.time.Clock() 
  
    

    while True: 
        dt = clock.tick(60) / 1000.0
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
           
        for sprite in updatable:
            sprite.update(dt)
            
            for shot in shots:
                for asteroid in asteroids:
                    if asteroid.collides(shot):
                        asteroid.kill()
                        shot.kill()
             
        
        for sprite in asteroids:
            if sprite.collides(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

















if __name__ == "__main__":
    main()