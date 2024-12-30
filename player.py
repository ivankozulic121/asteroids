import pygame
from shot import Shot
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    
    def __init__( self, x, y,radius):


        super().__init__( x, y, radius )
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        print('Update called.')
        keys = pygame.key.get_pressed()
        print("Window focus:", pygame.key.get_focused())
        print(f"a: {keys[pygame.K_a]}, d: {keys[pygame.K_d]}")

        if keys[pygame.K_a]:
            self.rotate(-dt)
            print("LEFT!")
        
        if keys[pygame.K_d]:
            self.rotate(dt)
            print("RIGHT!")
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
        
        if self.timer > 0:
            self.timer -= dt

    def move( self, dt ):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        
