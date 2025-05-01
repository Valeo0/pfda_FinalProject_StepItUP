import random
import pygame

screen_width = 800
screen_height = 600
arrow_size = 50
arrow_speed = 5
arrows = []


arrow_images = [
    pygame.image.load("up_arrow.png"),
    pygame.image.load("down_arrow.png"),
    pygame.image.load("left_arrow.png"),
    pygame.image.load("right_arrow.png")
]

class Arrow():
    
    def __init__(self,pos=(0,0), size = 50,):
        self.image = random.choice(arrow_images)
        self.pos = pos
        self.size = size
    
    def _update_pos(self):
        x,y = self.pos
        y += arrow_speed
        self.pos = (x,y)

    def draw(self,surface):
        surface.blit(self.image,self.pos)
            


class KeyTrail():
    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles = []

    def update(self, dt):
        random_size = random.randint(3,15)
        particle = Arrow(self.pos, size = 50, life = self.life)
        self.particles.insert(0,particle)
        self._update_particles(dt)
        self._update_pos()

    def _update_pos(self):
        x,y = self.pos
        y += self.size
        self.pos = (x,y)

    def draw(self,surface):
        for particle in self.particles:
            particle.draw(surface)
        
arrowclass = Arrow()
arrows.append(arrowclass)

def main():
    pygame.init()
    pygame.display.set_caption("Step It Up!")
    screen = pygame.display.set_mode((screen_width,screen_height))
    running = True
    while running:
        screen.fill((0,0,0))
        for arrow in arrows:
            arrow.draw(screen)
            arrow._update_pos()
        pygame.display.update()
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.update()

if __name__ == "__main__":
    main()


