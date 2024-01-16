import pygame
import random


SCREEN= pygame.display.set_mode((1080,604))         #To Create a Window with Dimension 1080 * 604
pygame.display.set_caption("EGG CATCHER")           #SET A CAPTION FOR WINDOW
BACKGROUND =  pygame.transform.scale(pygame.image.load("Assets/home.jpg"),(1080,604))
              #To transform image to 1080*604 dimension 
EGG = pygame.transform.scale(pygame.image.load("Assets/egg1.png"),(70,80))
spatch = pygame.image.load("Assets\spatch.png")
spatch = pygame.transform.scale(spatch,(80,60))
ENTER_KEY=pygame.transform.scale(pygame.image.load("Assets/ENTER.PNG"),(280,85)) 
BG = pygame.transform.scale(pygame.image.load("Assets/bg.png"),(1080,604))
BASKETS = pygame.transform.scale(pygame.image.load("Assets/basket.png"),(120,100))
HEN = pygame.transform.scale(pygame.image.load("Assets/hen.png"),(1080,200))



pygame.init()                                       #Use for initialization.
pygame.mixer.music.load("Sounds/music.mp3")         #For Music
pygame.mixer.music.play(-1)                         #for unlimited music play
WHITE = (255, 255, 255)                             #RGB COLOUR CODE FOR WHITE

FPS = 120                                         #FREAMS PER SECOND

def draw_window():                                                                             
    SCREEN.fill(WHITE)
    SCREEN.blit(BACKGROUND,(0,0))                   #To print a image on screen
    SCREEN.blit(ENTER_KEY,(400,490))

def catch(X,Y1,Y2,Y3,Y4,score):
    if 90<X<150 and 400<Y1<470:
        Y1=100
        score +=1
        pygame.mixer.music.load("Sounds\drop.wav")
        pygame.mixer.music.play(1)
    if 350<X<410 and 400<Y2<470:
        Y2=100
        score +=1
        pygame.mixer.music.load("Sounds\drop.wav")
        pygame.mixer.music.play(1)
    if 600<X<660 and 400<Y3<470:
        Y3=100
        score +=1
        pygame.mixer.music.load("Sounds\drop.wav")
        pygame.mixer.music.play(1)
    if 820<X<880 and 400<Y4<470:
        Y4=100
        score +=1
        pygame.mixer.music.load("Sounds\drop.wav")
        pygame.mixer.music.play(1)

    return X,Y1,Y2,Y3,Y4,score


def new_window(X,Y1,Y2,Y3,Y4):
    SCREEN.blit(BG,(0,0))
    SCREEN.blit(EGG,(140,Y1))
    SCREEN.blit(EGG,(400,Y2))
    SCREEN.blit(EGG,(650,Y3))
    SCREEN.blit(EGG,(870,Y4))
    SCREEN.blit(HEN,(0,-40))
    SCREEN.blit(BASKETS,(X,450))
  

def text(txt,size,x,y,color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(txt, True, color)
    SCREEN.blit(text, (x,y))

def main():                                        #To Quit the Window/Game
    clock = pygame.time.Clock()
    run = True
    showScreen = False
    move_left = False
    move_right = False

    score = 0
    life = 10
    
    frames = 0
    time = 0
    X=540
    Y1=100
    Y2=100
    Y3=100
    Y4=100     
    Y1_spatch=False
    Y2_spatch=False
    Y3_spatch=False
    Y4_spatch=False     
    while run:
        if not showScreen:
            draw_window()
            
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        showScreen = True 

                                     
        if showScreen : 
            new_window(X,Y1,Y2,Y3,Y4)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        move_right = True
                    if event.key == pygame.K_LEFT:
                        move_left = True
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        move_right = False
                    
                    if event.key == pygame.K_LEFT:
                        move_left = False

            if Y1 == 100:
                y1=random.randint(0,5)      # "y1' is the speed of egg which compiler choose from (0 - 2)
                
            if Y2== 100 :
                y2=random.randint(0,2)
                
                
            if Y3 == 100:
                y3=random.randint(0,2)
                
                
            if Y4 == 100:
                y4=random.randint(0,2)


            Y1+=y1
            if time >= 4:        #It is use to generate egg at random position.
                Y2+=y2
            if time >= 3:
                Y3+=y3
            if time >= 2:
                Y4+=y4


            if Y1 > 450:
                life -= 1
                Y1_spatch=True
                Y1 = 100
                pygame.mixer.music.load("Sounds\splash.wav")
                pygame.mixer.music.play(1)
            

            if Y2 > 450:
                life -= 1
                Y2_spatch=True          
                Y2 = 100
                pygame.mixer.music.load("Sounds\splash.wav")
                pygame.mixer.music.play(1)
            
            if Y3 > 450:
                Y3_spatch=True
                life -= 1                
                Y3 = 100
                pygame.mixer.music.load("Sounds\splash.wav")
                pygame.mixer.music.play(1)
            
            if Y4 > 450:
                Y4_spatch=True
                life -= 1
                Y4 = 100
                pygame.mixer.music.load("Sounds\splash.wav")
                pygame.mixer.music.play(1)
            
           

            

            if move_right and X <=950:
                X+=15 
            if move_left and X >=10:
                X-=15

            X,Y1,Y2,Y3,Y4,score = catch(X,Y1,Y2,Y3,Y4,score)

            if life ==0:
                pygame.mixer.music.load("Sounds\game_over.wav")
                pygame.mixer.music.play(1)
                main()

            frames+=1    #to calculate  a time of game
            if frames%FPS ==0:
                time +=1

            if Y1_spatch and Y1 < 200:
                SCREEN.blit(spatch,(140,520))
            if Y2_spatch and Y2 < 200:
                SCREEN.blit(spatch,(400,520))
            if Y3_spatch and Y3 < 200:
                SCREEN.blit(spatch,(650,520))
            if Y4_spatch and Y4 < 200:
                SCREEN.blit(spatch,(870,520))
                

            text(f"Score : {score}",32,20,570,"white")
            text(f"Life : {life}",32,950,570,"white")
        pygame.display.update()  
           

  
    pygame.quit()
main()

