import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH
from ship import Ship_Player

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.draw.polygon(screen,"white",Ship_Player.triangle(),LINE_WIDTH)

    def update(self, dt):
        # must override
        pass