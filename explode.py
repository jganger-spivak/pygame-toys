import pygame
import random
import time

pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("particle test")

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2, 2))
        self.color = color
        self.image.fill(color)
        self.rect = pygame.Rect(x, y, 2, 2)
        self.yvector = -4
    
    def update(self):
        self.yvector += 0.1
        if self.color.g - 2 >= 0:
            self.color.g -= 2
        self.image.fill(self.color)
        self.rect = self.rect.move(random.randint(-5, 5), random.randint(0, 2)*self.yvector)
        #print(self.rect)

def time_ms():
    return round(time.time() * 1000)
start = time_ms()

particles = pygame.sprite.Group()
for i in range(0, 100):
    particles.add(Particle(200, 200, pygame.Color(255, 255, 0)))
particles.draw(screen)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for particle in particles:
                    particle.yvector = -4
                    particle.color.g = 255
                    particle.rect.update(200, 200, 2, 2)
                    
    screen.fill((0 ,0, 0))
    delta_time = time_ms() - start
    particles.update()
    particles.draw(screen)
    pygame.display.flip()
exit()