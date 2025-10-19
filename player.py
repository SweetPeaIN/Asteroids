from circleshape import CircleShape
from shot import Shot
import constants
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # making circle a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # override draw method
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # rotate function
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    # move forward 
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation) # 0,0 --> 0,1 this is our forward unit vector
        self.position += forward * constants.PLAYER_SPEED * dt

    # update rotation value
    def update(self, dt):
        keys = pygame.key.get_pressed() # listening for keypress

        if keys[pygame.K_a]: # left rotation
            self.rotate(-dt) 
        if keys[pygame.K_d]: # right rotation
            self.rotate(dt)

        if keys[pygame.K_s]: # backwards
            self.move(-dt)
        if keys[pygame.K_w]: # forwards
            self.move(dt)

        if keys[pygame.K_SPACE]: # shooting
            self.shoot()
        
        self.timer -= dt # decrease timer by roughly 0.0166

    def shoot(self):
        
        # return if on a cooldown
        if self.timer > 0:
            return
        
        self.timer = constants.PLAYER_SHOOT_COOLDOWN # set 0.3 sec cooldown

        s = Shot(self.position.x, self.position.y, constants.SHOT_RADIUS) # create a shot
        # add velocity to shot by giving direction and speed
        s.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
