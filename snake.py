import pygame
import random

pygame.init()

# =========== Game variables ============
screen_width = 600
screen_height = 600
delay_time = 300    # milliseconds
cell_size = 20

# color
bg_color = (255,200,150)
magenta = (255,0,255)
green = (0,255,0)
black = (0,0,0)
red = (255,0, 0)

# snake
snake = [
    [screen_width/2, screen_height/2],   # head
    [screen_width/2, screen_height/2 + cell_size],
    [screen_width/2, screen_height/2 + 2*cell_size],
    [screen_width/2, screen_height/2 + 3*cell_size],   # tail
]

# food
is_new_food = True
food_pos = [0, 0]

# game ends
is_game_end = False

# moving direction
xdir = 0   # 1 (right), -1 (left)
ydir = -1   # 1 (down), -1 (up)

# =========== Game begins ============
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake game')

# =========== Game loop ============
run = True
while run:
    # clear the screen
    screen.fill(bg_color)

    # crate the food
    if is_new_food:
        # prevent to create the new food
        is_new_food = False
        # random the food's position
        x = random.randint(0, screen_width/cell_size - 1) * cell_size
        y = random.randint(0, screen_height/cell_size - 1) * cell_size
        food_pos = [x, y]
        # food_pos[0] = x
        # food_pos[1] = y

    # draw the food
    pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], cell_size, cell_size))

    # check user interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_LEFT and xdir != -1:
                xdir = -1
                ydir = 0
            elif event.key == pygame.K_RIGHT and xdir != -1:
                xdir = 1
                ydir = 0
            elif event.key == pygame.K_UP and ydir != 1:
                ydir = -1
                xdir = 0
            elif event.key == pygame.K_DOWN and ydir != -1:
                ydir = 1
                xdir = 0

    if is_game_end:
        continue
            
    # draw snake
    # head
    # pygame.draw.rect(screen, black, (snake[0][0], snake[0][1], cell_size, cell_size))
    # pygame.draw.rect(screen, magenta, (snake[0][0]+1, snake[0][1]+1, cell_size-2, cell_size-2))
    # # body
    # pygame.draw.rect(screen, black, (snake[1][0], snake[1][1], cell_size, cell_size))
    # pygame.draw.rect(screen, green, (snake[1][0]+1, snake[1][1]+1, cell_size-2, cell_size-2))
    # pygame.draw.rect(screen, green, (snake[2][0], snake[2][1], cell_size, cell_size))
    # pygame.draw.rect(screen, green, (snake[3][0], snake[3][1], cell_size, cell_size))

    for idx, pos in enumerate(snake):
        # border     
        pygame.draw.rect(screen, black, (pos[0], pos[1], cell_size, cell_size))
        # head?
        if idx == 0:
            pygame.draw.rect(screen, magenta, (pos[0]+1, pos[1]+1, cell_size-2, cell_size-2))
        else:
            pygame.draw.rect(screen, green, (pos[0]+1, pos[1]+1, cell_size-2, cell_size-2))

    # move the snake
    # [a b c d] -> [x a b c] -> [y x a b] -> [z y x a]
    # 1. remove the tail  [a b c d] -> [a b c]
    # snake.pop()
    # 2. insert the new head [a b c] -> [x a b c]
    # snake.insert(0, [snake[0][0], snake[0][1] -  cell_size])
    # if xdir == -1:
    #      snake.pop()
    #      snake.insert(0, [snake[0][0] - cell_size, snake[0][1]])
    # elif xdir == 1:
    #      snake.pop()
    #      snake.insert(0, [snake[0][0] + cell_size, snake[0][1]])

    snake.pop()
    snake.insert(0, [snake[0][0] + xdir * cell_size, snake[0][1] + ydir * cell_size])

    # is the food eaten by the snake?
    if snake[0] == food_pos:
        # print ('hit')
        # incress game sdeed (decrease delay time), limit at 100
        if delay_time > 100:
            delay_time -= 20

        # random a new food position

        # x = random.randint(0, screen_width/cell_size - 1) * cell_size
        # y = random.randint(0, screen_height/cell_size - 1) * cell_size
        # food_pos = [x, y]
        # pygame.draw.rect(screen, red, (food_pos[0], food_pos[1], cell_size, cell_size))
        
        is_new_food = True

        # increase the snake's lenght by 1
        snake.insert(0, [snake[0][0] + xdir * cell_size, snake[0][1] + ydir * cell_size])
        
        #either add a new part at head or tail
        # duplicate the tail
        snake.append(snake[-1])

    # end game conditions
    # 1. the snake's head passes the wall
    if snake[0][0] < 0 or snake[0][0] >= screen_width or snake[0][1] < 0 or snake[0][1] >= screen_height:
        is_game_end = True

    # 2. the snake's head hits its body
    
    # for idx,snk in enumerate(snake):
    #     # if it is not a head
    #     if snk != 0:
    #         # if the head hit the body
    #         if snake[0] == snk:
    #             is_game_end = True

    if snake[0] in snake[1:]:
        is_game_end = True



    # update the screen
    pygame.display.update()
    # delay the game, noted that this delay time should be small enough to detect the user's input
    pygame.time.delay(delay_time)

# =========== Game ends ============
pygame.quit()