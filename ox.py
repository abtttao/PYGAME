import pygame
from pygame.constants import K_ESCAPE
from pygame.locals import Rect

# --------- Game Variable ------------
sereen_width = 300
sereen_hight = 300
bg_color = (255,255,200)
grid_color = (50,50,50)
x_color = (255,0,0)
o_color = (0,255,0)
font_color = (0,0,255)
font_bg_color = (255,255,0)
replay_color = (255,255,255)
button_color = (5,120,200)

marker = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
# notation: 0 = blank, 1 = x, -1 = O
# player 
player = 1
is_win = False # flag to check winer
# replay rectangle
replay_rect = Rect(sereen_width/2 -60,sereen_hight/2 + 35, 130, 40)
 

# --------- Game Setting  ------------
pygame.init()
# font must be create after pygame.init()
font = pygame.font.SysFont(None, 40)
screen = pygame.display.set_mode((sereen_width,sereen_hight))
pygame.display.set_caption('Tic Tac Toe')
screen.fill((bg_color))


# --------- Function  ----------------
# +++++++++ draw grid ++++++++++++++++
def draw_grid():
    # hotizemtal lines
    pygame.draw.line(screen,grid_color, (0,sereen_hight/3),(sereen_width,sereen_hight/3))
    pygame.draw.line(screen,grid_color, (0,2*sereen_hight/3),(sereen_width,2*sereen_hight/3))
    # vertical lines
    pygame.draw.line(screen,grid_color, (sereen_width/3,0),(sereen_width/3,sereen_hight))
    pygame.draw.line(screen,grid_color, (2*sereen_width/3,0),(2*sereen_width/3,sereen_hight))
    pygame.display.update()

# +++++++++ draw maeker ++++++++++++++
def draw_marker(row,col):
    # # block 0;0
    # pygame.draw.line(screen, x_color,  (20, 20), (80, 80), 5)
    # pygame.draw.line(screen, x_color,  (20, 80,), (80, 20), 5)
    # # block 0;1
    # pygame.draw.line(screen, x_color,  (120, 20), (180, 80), 5)
    # pygame.draw.line(screen, x_color,  (120, 80,), (180, 20), 5)
    # # block 0;2
    # pygame.draw.line(screen, x_color,  (220, 20), (280, 80), 5)
    # pygame.draw.line(screen, x_color,  (220, 80,), (280, 20), 5)

    # block r c
    if player == 1:
        pygame.draw.line(screen, x_color,  (20 + col*100, 20 + row*100), (80 + col*100, 80 + row*100), 5)
        pygame.draw.line(screen, x_color,  (20 + col*100, 80 + row*100), (80 + col*100, 20 + row*100), 5)
    else:
        pygame.draw.circle(screen, o_color, (50 + col*100, 50 + row*100), 40, 5)

    pygame.display.update()


# +++++++++ draw maeker +++++++++++++++
def check_winner():
    global is_win
    # check marker array
    # **** 1. diagonal *****
    # [0,0], [1,1] [2,2]
    # [0,2], [1,1] [2,0]
    if marker[1][1] != 0:
        if marker[0][0] == marker[1][1] and marker[1][1] == marker[2][2]:
            is_win = True
        elif marker[0][2] == marker[1][1] and marker[1][1] == marker[2][0]:
            is_win = True

    # **** 2. horizental *****
    # [0,0] [1,1] [0,2]
    if not is_win:
        for row in marker:
            # print(row)
            if sum(row) == 3 or sum(row) == -3:
                is_win = True
                break
    # **** 3. verizental *****
    # [0,0] [1,0] [2,0]
    if not is_win:
        for col in range(3):
            total = marker[0][col] + marker[1][col] + marker[2][col]
            if total == 3 or total == -3:
                is_win = True
                break


    # is there aby winner?
    if is_win:
        # print(f'Winner is {player}')
        show_winner()

# ++++++++++ show winner ++++++++++++++
def show_winner():
    # print ('Winner is xxx')
    winner = 'O'
    if player == 1:
        winner = 'X'
    # winning message
    winning_img = font.render('Winner is ' + str(winner), True, font_color, font_bg_color)
    screen.blit(winning_img, (sereen_width/2 -70, sereen_hight/2 -20 ))
    # replay button
    pygame.draw.rect(screen,button_color, replay_rect)
    winning_img = font.render('Replay?', True, replay_color,)
    screen.blit(winning_img, (sereen_width/2 -50, sereen_hight/2 + 40))
    pygame.display.update()

# ++++++++++ replay  ++++++++++++++++++
def replay():
    global marker, player, is_win
    # clear screen and draw grid
    screen.fill(bg_color)
    draw_grid()
    # reset game variable
    marker = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
]
player = 1
is_win = False # flag to check winer

# ---------- Game Starts here ---------
draw_grid()

# game loop
run = True
while run:
    # pygame.display.update()
    # check for user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # print('clicked')
            # get mouse's position
            (mouse_x, mouse_y) =  pygame.mouse.get_pos()
             # check winner
            if is_win:
                margin_x = sereen_width/2 -60
                margin_y = sereen_hight/2 + 35
                # if mouse_x >= sereen_width/2 -60 and mouse_x <= margin_x +130 and mouse_y >= margin_y and mouse_y <= margin_y + 40:
                    #  print('replay') 
                    # replay()
                if replay.rect.collidepoint((mouse_x,mouse_y)):
                    replay()
                continue
            # print(f'{mouse_x} {mouse_y}')
            # if mouse_x < 100:
            #     col = 0
            # elif mouse_x < 200:
            #     col = 1
            # elif mouse_x < 300:
            #     col = 2

            # if mouse_y < 100:
            #     col = 0
            # elif mouse_y < 200:
            #     col = 1
            # elif mouse_y < 300:
            #     col = 2

            row = mouse_y // 100
            col = mouse_x // 100

            # prevent repeated click
            if marker[row][col] == 0:
                marker[row][col] = player
                # draw x or o
                draw_marker(row,col)
                # check winer
                check_winner()
                # switch player
                player *= -1
                
        
            # print(marker)

# pygame.time.delay(3000)
# ------  game end here --------------
pygame.quit()