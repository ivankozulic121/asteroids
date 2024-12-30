import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):

        super().__init__(x, y,  SHOT_RADIUS)


    def draw(self, screen):
        position_tuple = (int(self.position.x), int(self.position.y))
        pygame.draw.circle( screen, "white", position_tuple, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        