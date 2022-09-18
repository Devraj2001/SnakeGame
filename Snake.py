import pygame
import random
pygame.init()

#colour
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
#Window
gameWindow=pygame.display.set_mode((600,400))
pygame.display.set_caption("Hello Snake")
pygame.draw.rect(gameWindow,blue,[10,10,20,20])

#welcome
font=pygame.font.SysFont(None,55)
def welcome():
    gameWindow.fill(white)
    screen_text = font.render("Welcome to Snake Game", True, blue)
    screen_text2 = font.render("Press Space to Start", True, blue)
    gameWindow.blit(screen_text, [75, 155])
    gameWindow.blit(screen_text2, [105, 220])
    pygame.display.update()

#game variables
x=300
y=200
s=20
arr=[[x,y]]
food_x=random.randint(10,590)
food_y=random.randint(40,390)
food_s=20
exit_game=False
game_over=False
move_left=False
move_right=False
move_up=False
move_down=False
restart=False
clock=pygame.time.Clock()
fps=17

#score
score=0
high_score=0
font=pygame.font.SysFont(None,55)

def screen_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

#high score
def highest_score(score,color,high_score):
    screen_text1=font.render(f"Highest Score: {high_score}",True,color)
    screen_text2=font.render(f"Your Score: {score}",True,color)
    screen_text3=pygame.font.SysFont(None,45).render(f"Game Over! Press Space to continue",True,red)
    gameWindow.blit(screen_text1,[170,75])
    gameWindow.blit(screen_text2,[170,150])
    gameWindow.blit(screen_text3,[25,250])

k=True
while k:
    welcome()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
            k=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                k=False
print("K")
#Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT and move_left== False:
                move_left = False
                move_right = True
                move_up = False
                move_down = False
            elif event.key==pygame.K_LEFT and move_right == False:
                move_left = True
                move_right = False
                move_up = False
                move_down = False
            elif event.key==pygame.K_UP and move_down==False:
                move_left = False
                move_right = False
                move_up = True
                move_down = False
            elif event.key==pygame.K_DOWN and move_up==False:
                move_left = False
                move_right = False
                move_up = False
                move_down = True
    if move_left==True:
        x-=10
    elif move_right==True:
        x+=10
    elif move_up==True:
        y-=10
    elif move_down==True:
        y+=10
    if abs(x-food_x)<=s//1.5 and abs(y-food_y)<=s//1.5:
        score+=1
        food_x = random.randint(0, 590)
        food_y = random.randint(40, 390)
        arr.append([x,y])
    else:
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr.pop()
        arr.append([x,y])
    gameWindow.fill(white)
    screen_score(f"score: {score}", black, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_s, food_s])
    for i in arr:
        pygame.draw.rect(gameWindow, black, [i[0], i[1], s, s])
    pygame.display.update()
    clock.tick(fps)
    if x > 600 or y > 400 or x < 0 or y < 40:
        game_over = True
        restart=False

    for i in arr[:max(0,len(arr)-2)]:
        if abs(x-i[0])<=9 and abs(y-i[1])<=9 and len(arr)>2:
            game_over=True
    while game_over and not exit_game and not restart:
        gameWindow.fill(white)
        high_score=max(high_score,score)
        highest_score(score, blue,high_score)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    x = 300
                    y = 200
                    s = 20
                    arr = [[x, y]]
                    food_x = random.randint(10, 590)
                    food_y = random.randint(40, 390)
                    food_s = 20
                    exit_game = False
                    game_over = False
                    move_left = False
                    move_right = False
                    move_up = False
                    move_down = False
                    score = 0
                    restart=True
pygame.quit()
quit()