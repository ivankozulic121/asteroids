import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if event.type == pygame.KEYDOWN:
        print("PRESSED!")
        if keys[pygame.K_a]:
            print("A is pressed")
        if keys[pygame.K_d]:
            print("D is pressed")

    if event.type == pygame.KEYUP:
        if event.type == pygame.K_LEFT or event.type == pygame.K_RIGHT:
            print("stop")
        pygame.display.update()

pygame.quit()