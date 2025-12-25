from constants import PLAYER_RADIUS, LINE_WIDTH
from circleshape import Cshape

class Ship_Player(Cshape):
    def __init__(self, x, y,radius, rotation):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

        # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    
        
    
