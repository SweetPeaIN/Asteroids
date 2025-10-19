from circleshape import CircleShape
import pygame
import constants

class Shot(CircleShape):
    
    def __init__(self, x, y, radius= constants.SHOT_RADIUS):
        super().__init__(x, y, radius)

    # overriding draw and update
    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
            
    def update(self, dt):
         self.position += self.velocity * dt