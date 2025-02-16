import pygame
import os
import random
#Game Initialisation
pygame.init()
pygame.mixer.init()

#Setting game window and name
screen_width=900
screen_height=500
Game_window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My game")
bgimage=pygame.image.load("snake.jpg")
bgimage=pygame.transform.scale(bgimage,(screen_width,screen_height)).convert_alpha()
clock=pygame.time.Clock()
fps=60

def plot_rec(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,(0,128,0),[x,y,snake_size,snake_size])

font=pygame.font.SysFont(None,50)
def show_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    Game_window.blit(screen_text,[x,y])
def Welcome():
    
    pygame.mixer.music.load("GameLoop.mp3")
    pygame.mixer.music.play(-1)
    exit_game=False
    Welcome=pygame.display.set_mode((screen_width,screen_height))
    Welcome.fill((25,25,112))
    Game_window.blit(bgimage,(0,0))
    show_score("Welcome to Snake Wizard!!",(170,51,106),screen_width/8,screen_height/3)
    show_score("Press Enter To Play The Game",(170,51,106),screen_width/8,screen_height/2)
    while(not exit_game):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                exit_game=True
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_RETURN):
                    Gameloop()
        pygame.display.update()
        clock.tick(fps)                
            


def Gameloop():
    #Game variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=87
    velocity_x=0
    velocity_y=0
    snake_size=15
    food_x=random.randint(30,int(screen_width/2))
    food_y=random.randint(30,int(screen_height/2))
    food_size=15
    init_velocity=4
    score=0
    #Game colors with rgb values
    white=(255,255,255)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,128,0)

     
    if(not os.path.exists("HighScore.txt")):
         with open("HighScore.txt","w") as f:
            f.write("0")
    with open("HighScore.txt","r") as f:
        High_Score=f.read()


    snk_list=[]
    snake_len=1
    while(not exit_game):
        if(game_over):
            Game_window.fill(black)
            show_score("Score: "+str(score),red,5,5)
            show_score("High Score: "+str(High_Score),red,200,5)
            show_score("Game Over!! Press Enter for New Game",red,screen_width/8,screen_height/3)
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RETURN):
                        Welcome()  
        else:
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    exit_game=True
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_RIGHT):
                        velocity_x=init_velocity
                        velocity_y=0
                    if(event.key==pygame.K_LEFT):
                        velocity_x=-init_velocity
                        velocity_y=0        
                    if(event.key==pygame.K_UP):
                        velocity_y=-init_velocity
                        velocity_x=0
                    if(event.key==pygame.K_DOWN):
                        velocity_y=init_velocity
                        velocity_x=0

                    if(event.key==pygame.K_a):#Cheat
                        score+=10    
                                        
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if((abs(snake_x-food_x)<6)and(abs(snake_y-food_y)<6)):
                score+=10
                snake_len+=5
                food_x=random.randint(30,int(screen_width/2))
                food_y=random.randint(30,int(screen_height/2))
                
            Game_window.fill(black)
            show_score("Score: "+str(score),red,5,5)
            show_score("High Score: "+str(High_Score),red,200,5)
            pygame.draw.rect(Game_window,red,[food_x,food_y,food_size,food_size])
            Head=[]
            Head.append(snake_x)
            Head.append(snake_y)
            snk_list.append(Head)

            if(len(snk_list)>snake_len):
                del snk_list[0]

            if Head in snk_list[:-1]:
                pygame.mixer.music.load("GameOver.mp3")
                pygame.mixer.music.play()
                game_over=True

            if((snake_x<0)or(snake_x>screen_width)or(snake_y<0)or(snake_y>screen_height)):
                pygame.mixer.music.load("GameOver.mp3")
                pygame.mixer.music.play()
                game_over=True
            if(score>int(High_Score)):
                High_Score=f"{score}"
                with open("HighScore.txt","w") as f:
                    f.write(f"{score}")
            # pygame.draw.rect(Game_window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_rec(Game_window,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()                   
Welcome()