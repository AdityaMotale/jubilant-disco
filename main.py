import pygame
import os

#constants
WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#Raw Assets
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join('Assets', "spaceship_yellow.png"))
RED_SPACESHIP = pygame.image.load(
    os.path.join('Assets', "spaceship_red.png"))


## This is to scale and resize raw assets

def scale_resize(img, angle):
    return pygame.transform.rotate(pygame.transform.scale(img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), angle)


#Modified Assets
Y_SPACESHIP = scale_resize(YELLOW_SPACESHIP, 270)
R_SPACESHIP = scale_resize(RED_SPACESHIP, 90)


#init setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Space Odeseyy')


#Resuable functions



## This is to draw objects on the display
def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(Y_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(R_SPACESHIP, (red.x, red.y))
    pygame.display.update()


## This is to start the exicution
def main():
    red = pygame.Rect(800, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        red.y += 1
        draw_window(red, yellow)
    pygame.QUIT()

## File name check
if __name__ == "__main__":
    main()