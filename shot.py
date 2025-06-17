import pygame
from circleshape import CircleShape

from constants import *


class Shot(CircleShape):

    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        