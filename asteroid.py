import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):


        super().__init__( x, y, radius)
        self.position = pygame.Vector2(x, y)


    def draw(self, screen):
        position_tuple = (int(self.position.x), int(self.position.y))
        pygame.draw.circle( screen, "white", position_tuple, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2