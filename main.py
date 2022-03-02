import pygame
import os

# constants
WIDTH, HEIGHT = 900, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect((WIDTH / 2) - 5, 0, 10, HEIGHT)

# Raw Assets
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join('Assets', "spaceship_yellow.png"))
RED_SPACESHIP = pygame.image.load(
    os.path.join('Assets', "spaceship_red.png"))


# This is to scale and resize raw assets

def scale_resize(img, angle):
    return pygame.transform.rotate(pygame.transform.scale(img, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), angle)


# Modified Assets
Y_SPACESHIP = scale_resize(YELLOW_SPACESHIP, 90)
R_SPACESHIP = scale_resize(RED_SPACESHIP, 270)


# init setup
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Space Odeseyy')


# Resuable functions


# This is to draw objects on the display
def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(Y_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(R_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def yellow_movemonet(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # Y Left
        yellow.x -= VEL
    # Y Right
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Y Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 20:  # Y Down
        yellow.y += VEL


def red_movemonet(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # R Left
        red.x -= VEL
    # R Right
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - red.width:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # R Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 20:  # R Down
        red.y += VEL


# This is to start the exicution
def main():
    red = pygame.Rect(800, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 350, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        yellow_movemonet(keys_pressed, yellow)

        red_movemonet(keys_pressed, red)

        draw_window(red, yellow)

    pygame.QUIT()


# File name check
if __name__ == "__main__":
    main()
