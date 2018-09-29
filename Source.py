#import Our Packages
import pygame as pg 
import time
import random

#initialize all imported pygame modules
pg.init()

#Our Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
ceil = (19, 229, 240)
yellow = (255, 255, 25)
red2 = (219.3,2.6,14.27)

#Size of Display Window
display_width = 1000
display_height = 680

#Initialize a window or screen for display
gameDisplay = pg.display.set_mode((display_width, display_height))

#Set the current window caption
pg.display.set_caption('Snake')


gameExit = True

snake_length = 10
snake_width = 10
snakeLen = 1

block_size = 20
AppleThickness = 30

FPS = 15
Screen_FPS = 50

clock = pg.time.Clock()

smallfont = pg.font.SysFont('comicsansms', 25)
uppersmallfont = pg.font.SysFont('comicsansms', 35)
medfont = pg.font.SysFont('comicsansms', 50)
largefont = pg.font.SysFont('comicsansms', 75)


img = pg.image.load('Snake Head.png')
apple_img = pg.image.load('Apple.png')
tail_img = pg.image.load('Snake Tail.png')
icon = pg.image.load('Snake Head.png')
pg.display.set_icon(icon)

direction = 'up'


def rotate_tail(x1, y1, x2, y2):
    x = x1 - x2
    y = y1 - y2
    if x > 0:
        return pg.transform.rotate(tail_img, 90)
    elif x < 0:
        return pg.transform.rotate(tail_img, 270)
    elif y > 0:
        return pg.transform.rotate(tail_img, 360)
    elif y < 0:
        return pg.transform.rotate(tail_img, 180)


def snake(block_size, snakeList, snakeTail):
    tail = tail_img
    if direction == 'up':
        head = img
    elif direction == 'right':
        head = pg.transform.rotate(img, 270)
    elif direction == 'left':
        head = pg.transform.rotate(img, 90)
    elif direction == 'down':
        head = pg.transform.rotate(img, 180)


    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    count = 0
    for XnY in snakeList[:-1]:
        if count == 0:
            tail = rotate_tail(snakeList[0][0], snakeList[0][1], snakeList[1][0], snakeList[1][1])
            gameDisplay.blit(tail, (snakeList[0][0], snakeList[0][1]))
            count += 1
        else:
            pg.draw.rect(gameDisplay,red2, [XnY[0], XnY[1], block_size, block_size])

def Apple_Gen(snakeList):
    Valid = False
    while Valid == False:
        appleX = random.randrange(0, display_width - AppleThickness, AppleThickness)
        appleY = random.randrange(0, display_height - AppleThickness, AppleThickness)
        appleXY = [appleX, appleY]
        Valid = Valid_apple(appleXY, snakeList)

    return appleX, appleY


def Valid_apple(appleXY, snakeList):
    for eachpiece in snakeList[:-1]:
        if eachpiece == appleXY:
            return False
    return True


def intro_screen():
    intro = True

    while intro:
        gameDisplay.fill(white)
        msg_to_screen('...Welcome to HamDola...', green, -150, 'large')
        msg_to_screen('Don\'t Think More , Just Do it ' , green, -100, 'medium')
        msg_to_screen('We Here To Eat,Just Feed Us', black, -30, 'medium')
        #msg_to_screen('if U hit edges or yourself, U die.', black, -0, 'upsmall')
        msg_to_screen('...Press C to play ,P to pause ,Q to Quit...', blue, 60, 'medium')
        msg_to_screen('...Press Escape at anytime to Leave...', blue, 100, 'medium')
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    intro = False
                elif event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        clock.tick(Screen_FPS)


def score(score):
    show = uppersmallfont.render("Score: " + str(score), True,ceil)
    gameDisplay.blit(show, (10, 10))


def pause():
    paused = True

    msg_to_screen('Paused', red, -60, 'large')
    msg_to_screen('Let\'s Continue,Just Press C', black, -20, 'medium')
    msg_to_screen('Press Q to Quit', red, 20, 'upsmall')

    pg.display.update()

    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    paused = False
                elif event.key == pg.K_q or event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        clock.tick(FPS)


def textObjects(msg, color, size='small'):
    if size == 'small':
        textSurface = smallfont.render(msg, True, color)
    elif size == 'medium':
        textSurface = medfont.render(msg, True, color)
    elif size == 'upsmall':
        textSurface = uppersmallfont.render(msg, True, color)
    elif size == 'large':
        textSurface = largefont.render(msg, True, color)
    return textSurface, textSurface.get_rect()


'''
Old Version :

def msg_to_screen(msg,color) : 
    screen_text = font.render(msg,True,color)
    gameDisplay.bilt(screen_text,[display_wigth/2,display_height/2])
'''
def msg_to_screen(msg, color, y_display=0, size='small'):
    textSurface, textRect = textObjects(msg, color, size)
    textRect.center = (display_width // 2), (display_height // 2) + y_display
    gameDisplay.blit(textSurface, textRect)

def gameloop():
    gameExit = True
    gameover = True

    change_x = 0
    change_y = 0

    lead_x = display_width // 2
    lead_y = display_height // 2

    snakeList = []
    global snakeLen
    snakeLen = 1
    appleX, appleY = Apple_Gen(snakeList)

    global direction
    global Screen_FPS

    event_key_temp = ''

    while gameExit:
        if gameover == False:
            msg_to_screen('Oh No Sorry...Game Over', black, -60, 'large')
            msg_to_screen('Don\'t Give Up ,Try again Just Press C',red, 60, 'medium')
            msg_to_screen('Press Q to quit',red, 100, 'medium')
            pg.display.update()

        while not gameover:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameover = True
                    gameExit = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        gameloop()
                    elif event.key == pg.K_q or event.key == pg.K_ESCAPE:
                        gameover = True
                        gameExit = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    if event_key_temp == 'left':
                        direction = 'left'
                        change_x = -block_size
                    else:
                        direction = 'right'
                        change_x = block_size
                    change_y = 0
                elif event.key == pg.K_LEFT:
                    if event_key_temp == 'right':
                        direction = 'right'
                        change_x = block_size
                    else:
                        direction = 'left'
                        change_x = -block_size
                    change_y = 0
                elif event.key == pg.K_UP:
                    if event_key_temp == 'down':
                        direction = 'down'
                        change_y = block_size
                    else:
                        direction = 'up'
                        change_y = -block_size
                    change_x = 0
                elif event.key == pg.K_DOWN:
                    if event_key_temp == 'up':
                        direction = 'up'
                        change_y = -block_size
                    else:
                        direction = 'down'
                        change_y = block_size
                    change_x = 0
                elif event.key == pg.K_p:
                    pause()

                event_key_temp = direction

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()
                quit()

        if lead_x >= display_width or lead_x <= -1 or lead_y >= display_height or lead_y <= -1:
            gameover = False

        lead_x += change_x
        lead_y += change_y

        if lead_x >= appleX and lead_x <= appleX + AppleThickness or lead_x + block_size >= appleX and lead_x + block_size <= appleX + AppleThickness:
            if lead_y >= appleY and lead_y <= appleY + AppleThickness or lead_y + block_size >= appleY and lead_y + block_size <= appleY + AppleThickness:
                appleX, appleY = Apple_Gen(snakeList)
                snakeLen += 1

        gameDisplay.fill(white)
        gameDisplay.blit(apple_img, (appleX, appleY))

        snakeHead = [lead_x, lead_y]
        snakeTail = [lead_x, lead_y + snakeLen * 20]
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLen:
            del snakeList[0]
        snake(block_size, snakeList, snakeTail)

        for eachpiece in snakeList[:-1]:
            if eachpiece == snakeHead:
                gameover = False

        score(snakeLen - 1)

        pg.display.update()
        clock.tick(FPS)

    # uninitialize all pygame modules
    pg.quit()
    quit()


intro_screen()
gameloop()
