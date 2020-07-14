import pygame
import sys

pygame.init()

WIDTH=800
HEIGHT=600

RED=(255,0,0)

Player_pos=[400,300]
player_siz=50


screen=pygame.display.set_mode((WIDTH,HEIGHT))

game_over=False

while not game_over:

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            x=Player_pos[0]
            y=Player_pos[1]
            
            if event.key == pygame.K_LEFT:
                x -=5
            elif event.key == pygame.K_RIGHT:
                x +=5
            Player_pos=[x,y]   
    screen.fill((0,0,0))
    pygame.draw.rect(screen,RED,(Player_pos[0],Player_pos[1],player_siz,player_siz))

    pygame.display.update()