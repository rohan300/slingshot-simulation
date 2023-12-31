import math
import pygame

# Initialize pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

# Create the screen
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Simulation")

PLANET_MASS = 100
G = 5
SHIP_MASS = 5
FPS = 60
PLANET_SIZE = 50
VEL_SCALE = 1000

BG = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def main():
    running = True
    clock = pygame.time.Clock()


    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        window.blit(BG, (0, 0))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
