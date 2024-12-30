import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        points = self.triangle()
        pygame.draw.polygon( screen, "white", points , 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other_circle):
        dist =  pygame.math.Vector2.distance_to(self.position,other_circle.position)

        if dist <= self.radius + other_circle.radius:
            return True
        else:
            return False
 
     #def distance_to(self, other_circle)
    