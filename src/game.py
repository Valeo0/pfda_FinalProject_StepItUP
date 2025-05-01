import random
import pygame

screen_width = 800
screen_height = 600
arrow_size = 50
arrow_speed = 1/2
arrows = []




arrow_images = [
    pygame.image.load("up_arrow.png"),
    pygame.image.load("down_arrow.png"),
    pygame.image.load("left_arrow.png"),
    pygame.image.load("right_arrow.png")
]

class Arrow():
    
    def __init__(self,pos=(300,0), size = 25, life= 3000):
        self.image = random.choice(arrow_images)
        self.pos = pos
        self.size = size
        self.age = 0
        self.life = life
        self.dead = False

    def update(self,dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
    
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
        pygame.draw.line(screen,(255,46,31,255),(0,500),(screen_width,500))
        for arrow in arrows:
            arrow.draw(screen)
            arrow._update_pos()
            arrow.update(dt)
        pygame.display.update()
        for idx,arrow in enumerate(arrows):
            if arrow.pos[1] >= screen_height:
                del arrows[idx]
            if arrow.dead:
                del arrows[idx]
                arrows.append(Arrow())
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.update()

if __name__ == "__main__":
    main()


