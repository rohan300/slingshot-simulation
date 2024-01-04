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
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("assets/jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class SpaceObject:
    def __init__(self, x, y, x_vel, y_vel, mass):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.mass = mass

    def move(self, planet = None):
        self.x+= self.x_vel
        self.y+= self.y_vel

    def draw(self):
        pygame.draw.circle(window, RED, (int(self.x), int(self.y)), 5)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        window.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))
        

def createShip(loc, mouse):
    x, y = loc
    m_x, m_y = mouse
    x_vel = (m_x - x) / VEL_SCALE
    y_vel = (m_y - y) / VEL_SCALE
    return SpaceObject(x, y, x_vel, y_vel, SHIP_MASS)

def main():
    running = True
    clock = pygame.time.Clock()
    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    temp_obj = None


    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj:
                    obj = createShip(temp_obj, pygame.mouse.get_pos())
                    objects.append(obj)
                    temp_obj = None
                else:
                    temp_obj = pygame.mouse.get_pos()

        window.blit(BG, (0, 0))

        if temp_obj:
            pygame.draw.line(window, WHITE, temp_obj, pygame.mouse.get_pos(), 2)
            pygame.draw.circle(window, RED, temp_obj, 5)

        for obj in objects[:]:
            obj.draw()
            obj.move()
            offscreen = obj.x > WIDTH or obj.x < 0 or obj.y > HEIGHT or obj.y < 0
            collide = math.sqrt((obj.x - planet.x) ** 2 + (obj.y - planet.y) ** 2) <= PLANET_SIZE
            if offscreen or collide:
                objects.remove(obj)

        planet.draw()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
