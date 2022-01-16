# [DONE] random the pipes' height
# TODO: bird hits the ground
# TODO: bird hits the pipes
# TODO: replay button
# TODO: scoring

import pygame
from pygame.locals import *
import pyganim
import random

pygame.init()
clock = pygame.time.Clock()
fps = 30     #frames per second

# --- game assets ---
bg_img = pygame.image.load('img/bg.png')
# bg_width = bg_img.get_rect().width
bg_width = bg_img.get_width()
# bg_height = bg_img.get_rect().height
bg_height = bg_img.get_height()

ground_img = pygame.image.load('img/ground.png')
ground_width = ground_img.get_rect().width
ground_height = ground_img.get_rect().height
pipe_img = pygame.image.load('img/pipe.png')
pipe_img_flip = pygame.transform.flip(pipe_img, False, True)
pipe_width = pipe_img.get_rect().width
pipe_height = pipe_img.get_rect().height

# --- game setting ---
screen_width = bg_width
screen_height = bg_height + ground_height
# scrolling ground image to the left
ground_x = 0
ground_scroll_speed = 5
# bird location (top-left)
bird_x = 150
bird_y = screen_height/2
# pipe location
pipe_x = 400
pipe_y = 500
pipe_number = 5
pipe_interval = 200
pipe_gap = 300

gravity = 5
# flag to prevent double click
left_click = False

# --- bird animation ---
bird_set = []
for i in range(3):
    bird_set.append((f'img/bird{i+1}.png', 200))

bird_anim = pyganim.PygAnimation(
    bird_set
    # [
    #     ('img/bird1.png', 200),
    #     ('img/bird2.png', 200),
    #     ('img/bird3.png', 200),
    # ]
)
bird_anim.play()

# ---------------- Randoming pipe lenght ----------
pipe_randoms = []
for i in range(pipe_number):
    pipe_randoms.append(random.randint(-50,50))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# --- game starts here ---
run = True
while run:
    # set fps
    clock.tick(fps)
    # draw the background
    screen.blit(bg_img, (0,0))

    # draw pipes
    for i in range(pipe_number):
        px = pipe_x + i*pipe_interval
        screen.blit(pipe_img, (px, pipe_y + pipe_randoms[i]))
        screen.blit(pipe_img_flip, (px, -(pipe_y+pipe_randoms[i]) + pipe_gap))
        
    # scroll pipe to the left
    pipe_x -= ground_scroll_speed
    # if the first pipe is out of left margin
    if pipe_x <= -pipe_width:
        pipe_x = pipe_interval - pipe_width
        # remove the first pipe's random value
        # [1 2 3 4 5] -> [2 3 4 5]
        pipe_randoms.pop(0)
        # add new random value
        # [2 3 4 5] -> [2 3 4 5 rnd]
        pipe_randoms.append(random.randint(-50,50))

    # draw the ground
    screen.blit(ground_img, (ground_x, bg_height))
    ground_x -= ground_scroll_speed
    if ground_x < -(ground_width-bg_width):
        ground_x = 0

    # draw animated bird
    bird_anim.blit(screen, (bird_x, bird_y))

    # gravity
    bird_y += gravity

    # fly the bird
    # mouse click event
    if pygame.mouse.get_pressed()[0] == 1 and left_click == False:
        # left mouse clicked
        bird_y -= 50
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