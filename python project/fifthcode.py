import pygame
import sys
import random

pygame.init()

WIDTH=800
HEIGHT=600

RED=(255,0,0)
YELLOW=(0,0,255)

BACKGOUND_COLOR=(0,0,0)

player_siz=50
Player_pos=[WIDTH/2,HEIGHT-2*player_siz]

enemy_siz=50
enemy_pos=[random.randint(0,WIDTH-enemy_siz),0]
enemy_list=[enemy_pos]


SPEED=10

screen=pygame.display.set_mode((WIDTH,HEIGHT))

game_over=False

clock=pygame.time.Clock()

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,YELLOW,(enemy_pos[0],enemy_pos[1],enemy_siz,enemy_siz))   

def drop_enemies(enemy_list):
    delay=random.random()
    if len(enemy_list)<10 and delay<0.5:
        x_pos=random.randint(0,WIDTH-enemy_siz)
        y_pos=0
        enemy_list.append([x_pos,y_pos])

def update_enemy_position(enemy_list):
    for idx,enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1]<HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)

def collision_check(enemy_list,Player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,Player_pos):                     
           return True
    return False

def detect_collision(Player_pos,enemy_pos):
    p_x=Player_pos[0]
    p_y=Player_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x>=p_x and e_x<(p_x+player_siz)) or (p_x >= e_x and p_x<(e_x+enemy_siz)):
        if (e_y>=p_y and e_y<(p_y+player_siz)) or (p_y >= e_y and p_y <(e_y+enemy_siz)) :
           return True 
    return False

while not game_over:

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            x=Player_pos[0]
            y=Player_pos[1]
            
            if event.key == pygame.K_LEFT:
              
                x -=player_siz
            elif event.key == pygame.K_RIGHT:
              
                x +=player_siz
            Player_pos=[x,y]   
    
    screen.fill(BACKGOUND_COLOR)

    #update the position of enemy
    if enemy_pos[1] >= 0 and enemy_pos[1]<HEIGHT:
       enemy_pos[1] += SPEED
    else:
        enemy_pos[0]=random.randint(0, WIDTH-enemy_siz)
        enemy_pos[1]=0

    if detect_collision(Player_pos,enemy_pos):
        game_over=True
        break

    drop_enemies(enemy_list)
    update_enemy_position(enemy_list)

    if collision_check(enemy_list,Player_pos):
        game_over=True
        break 

    draw_enemies(enemy_list)

    pygame.draw.rect(screen,RED,(Player_pos[0],Player_pos[1],player_siz,player_siz))

    clock.tick(30)

    pygame.display.update()