# [DONE] random the pipes' height
# [DONE] bird hits the ground
# [DONE] bird hits the pipes
# TODO: replay button
# TODO: scoring

import pygame
from pygame import mouse
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

restart_img = pygame.image.load('img/restart.png')

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
game_over = False

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
bird_height = bird_anim.getRect().height
bird_width = bird_anim.getRect().width

# ---------------- Randoming pipe lenght ----------
pipe_randoms = []
for i in range(pipe_number):
    pipe_randoms.append(random.randint(-50,50))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

# ----- restart function --------
def restart():
    global pipe_x, bird_x, bird_y, gravity, left_click, game_over, pipe_randoms
    bird_x = 150
    bird_y = screen_height/2
    pipe_x = 400
    gravity = 5
    left_click = False
    game_over = False
    for i in range(pipe_number):
        pipe_randoms[i] = random.randint(-50,50)

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
        py = pipe_y + pipe_randoms[i]
        py_flip = -(pipe_y+pipe_randoms[i]) + pipe_gap
        screen.blit(pipe_img, (px, py))
        screen.blit(pipe_img_flip, (px, py_flip))
        # if the bird hits the pipe (first or second)
        if i == 0 or i == 1:
            if (bird_x + bird_width) >= px and (bird_x + bird_width) <= (px + pipe_width) and ((bird_y +bird_height) >= py or bird_y <= (py_flip + pipe_height)):
                game_over = True
        
    # scroll pipe to the left
    if not game_over:
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
    if not game_over:
        ground_x -= ground_scroll_speed
    if ground_x < -(ground_width-bg_width):
        ground_x = 0

    # draw animated bird
    bird_anim.blit(screen, (bird_x, bird_y))

    # is game over?
    if game_over:
        bird_anim.pause()
        screen.blit(restart_img, (screen_width/2, screen_height/2))
        if pygame.mouse.get_pressed()[0] == 1:
            # print('restart')
            # rectangle of restart image
            restart_rect = restart_img.get_rect()
            # set the top-lef position of restart image
            restart_rect.topleft = (screen_width/2, screen_height/2)
            # get mouse click position
            mouse_pos = pygame.mouse.get_pos()
            # print(mouse_pos)
            # print(restart_rect)
            # if we click on a restart image rectangle
            if restart_rect.collidepoint(mouse_pos) and left_click == False:
                left_click = True
                # restart game
                restart()
                # print('restart')
    
    # bird hits floor
    if gravity != 0:
        if (bird_y + bird_height)  >= bg_height:
            game_over = True
            gravity = 0
        else:
            bird_y += gravity
      
    # fly the bird
    # mouse click event
    if not game_over:
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