from circleshape import CircleShape
import pygame
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
            
    def update(self, dt):
         self.position += self.velocity * dt

    # splits big asteroids and destroys small ones
    def split(self):
        # we want to kill any size asteroid first
        # then we create new ones
        # that's how splitting works
        self.kill() 
        
        # check to destroy (small asteroid)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        random_trajectory = random.uniform(20, 50) # random angle for new asteroids

        # vectors for newer asteroids
        vec1 = self.velocity.rotate(random_trajectory) 
        vec2 = self.velocity.rotate(-random_trajectory)
        
        new_radii = self.radius - constants.ASTEROID_MIN_RADIUS # newer asteroids radius

        # creating 2 new asteroids obj 
        ast1 = Asteroid(self.position.x, self.position.y, new_radii)
        ast2 = Asteroid(self.position.x, self.position.y, new_radii)

        # assigning velocities
        ast1.velocity = vec1 * 1.2
        ast2.velocity = vec2 * 1.2