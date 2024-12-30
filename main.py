import pygame
import sys
from constants import * 
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = ( asteroids, updatable, drawable)
    Player.containers = ( updatable, drawable )
    Shot.containers = (shots, updatable, drawable )

    asteroidField = AsteroidField()
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS )
    
    

    clock = pygame.time.Clock()
    dt=0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60) / 1000  # Control FPS and get delta time

        # Update the player's state, adjust state based on input
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print('Game Over!')
                sys.exit()
            for shot in shots:
                if asteroid.check_collision(shot) == True:
                    asteroid.split()
                    shot.kill()

    
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the player (after updating)
        for item in drawable:
            item.draw(screen)

        
    
        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main()