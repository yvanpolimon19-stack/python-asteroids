from circleshape import  CircleShape
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):

        super().__init__(x, y ,radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
          