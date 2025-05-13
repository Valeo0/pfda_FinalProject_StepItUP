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
arrow_directions = {
"up_arrow.png":pygame.K_UP,
 "down_arrow.png": pygame.K_DOWN,
"left_arrow.png": pygame.K_LEFT,
 "right_arrow.png": pygame.K_RIGHT
}
class Arrow():
    
    def __init__(self,pos=(300,0), size = 25, life= 3000):
        self.image = random.choice(arrow_images)
        self.pos = pos
        self.size = size
        self.age = 0
        self.life = life
        self.dead = False
        self.filename = random.choice(list(arrow_directions.keys()))
        self.image = pygame.image.load(self.filename)
        self.direction = arrow_directions[self.filename]

    def update(self,dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
    
    def _update_pos(self, dt):
        x,y = self.pos
        y += arrow_speed * dt
        self.pos = (x,y)

    def draw(self,surface):
        surface.blit(self.image,self.pos)
            
arrowclass = Arrow()
arrows.append(arrowclass)

def main():
    pygame.init()
    pygame.font.init()
    previous_time = pygame.time.get_ticks()
    pygame.display.set_caption("Step It Up!")
    score = 0
    strikes = 0
    screen = pygame.display.set_mode((screen_width,screen_height))
    score_font = pygame.font.Font(None, size = 50)
    text_surface = score_font.render("Player Score", True, (255,255,255))
    score_surface = score_font.render(str(score), True,(255,255,255))
    strike_surface = score_font.render("Strikes", True, (255,255,255))
    red_X_surface = score_font.render("X",True,(252,3,15))
    running = True
    while running:
        dt = pygame.time.get_ticks() - previous_time
        screen.fill((0,0,0))
        screen.blit(text_surface,(0,0))
        screen.blit(score_surface,(40,40))
        screen.blit(strike_surface,(400,0))
        for i in range(strikes):
                            red_X_surface = score_font.render("X",True,(252,3,15))
                            screen.blit(red_X_surface,(400 + i * 30, 50))
        pygame.draw.line(screen,(255,46,31,255),(0,500),(screen_width,500,),10)
        for arrow in arrows:
            arrow.draw(screen)
            arrow._update_pos(dt)
            arrow.update(dt)
        previous_time = pygame.time.get_ticks()
        pygame.display.update()
        for idx,arrow in enumerate(arrows):
            if arrow.pos[1] >= screen_height:
                del arrows[idx]
                arrows.append(Arrow())
            elif arrow.dead:
                del arrows[idx]
                arrows.append(Arrow())
        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #Check which key was pressed
                for arrow in arrows:

                    if event.key == arrow.direction and 330 <= arrow.pos[1] <= 430:
                        score += 1
                        score_surface = score_font.render(str(score), True, (255, 255, 255))
                    else:
                        strikes += 1
                        
                if strikes == 3:
                    while running:
                        game_over = pygame.image.load("game_over_screen.png")
                        screen.blit(game_over,(0,0))
                        screen.blit(score_surface,(400,360))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running = False
                        pygame.display.update()       

                
    pygame.display.update()

if __name__ == "__main__":
    main()


