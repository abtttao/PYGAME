import pygame
from pygame.locals import *
import pyganim

pygame.init()
clock = pygame.time.Clock()
fps = 30

# --- game setting ---
screen_width = 864
screen_height = 768 + 168
ground_x = 0
ground_scroll_speed = 5
bird_x = 150
bird_y = screen_height/2
pipe_x = 400
pipe_y = 500
pips_interval = 200
pipe_number = 5
gravity = 5
left_click = False

# --- game assets ---
bg_img = pygame.image.load('img/bg.png')
bg_width = bg_img.get_rect().width
bg_height = bg_img.get_rect().height
bg_ground = pygame.image.load('img/ground.png')
ground_width = bg_ground.get_rect().width
ground_height = bg_ground.get_rect().height
pipe_img = pygame.image.load('img/pipe.png')
pipe_img_flip = pygame.transform.flip(pipe_img, False, True)
pipe_width = pipe_img.get_rect().width
pipe_height = pipe_img.get_rect().height

# --- brid animation ---
bird_anim = pyganim.PygAnimation(
    [
        ('img/bird1.png',200),
        ('img/bird2.png',200),
        ('img/bird3.png',200)
    ]
)
bird_anim.play()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Brid')

# --- game starts here ---
run = True
while run:
    # set fps
    clock.tick(fps)
    # draw the background
    screen.blit(bg_img,(0,0))

    # draw a pipe
    screen.blit(pipe_img, (pipe_x, pipe_y))
    # screen.blit(pipe_img_flip, (pipe_x, -pipe_y + 300))
    # screen.blit(pipe_img, (pipe_x + pips_interval, pipe_y))
    # screen.blit(pipe_img_flip, (pipe_x + pips_interval, -pipe_y + 300))
    # screen.blit(pipe_img, (pipe_x + 2*pips_interval, pipe_y))
    # screen.blit(pipe_img_flip, (pipe_x + 2*pips_interval, -pipe_y + 300))
    # screen.blit(pipe_img, (pipe_x + 3*pips_interval, pipe_y))
    # screen.blit(pipe_img_flip, (pipe_x + 3*pips_interval, -pipe_y + 300))

    for i in range(pipe_number):
        px = pipe_x + i*pips_interval
        screen.blit(pipe_img, (px, pipe_y))
        screen.blit(pipe_img_flip, (px, -pipe_y + 300))

    # scroll pipe to the left
    pipe_x -= ground_scroll_speed
    # if the frist pipe is out of left
    if pipe_x <= -pipe_width :
        pipe_x = pips_interval - pipe_width


    # draw the ground
    screen.blit(bg_ground, (ground_x,bg_height))
    ground_x -=  ground_scroll_speed
    if ground_x < -(ground_width-bg_width) :
        ground_x = 0

    # draw animated brid
    bird_anim.blit(screen, (bird_x, bird_y))

    # gravity
    bird_y += gravity

    # fly the bird
    # mouse click event
    if pygame.mouse.get_pressed()[0] == 1 and left_click == False:
        # left mouse click
        bird_y -= 50
        # print('x')
        left_click = True
    elif pygame.mouse.get_pressed()[0] == 0 and left_click == True:
        left_click = False

    # user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            # press ESC to end game
            if event.key == pygame.K_ESCAPE:
                run = False

    # update the display
    pygame.display.update()



# --- game ends ---
pygame.quit()