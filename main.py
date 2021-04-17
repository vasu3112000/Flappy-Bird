import random 
import sys 
import pygame 
from pygame.locals import *


FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY= SCREENHEIGHT* 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/images/bird.png'
BACKGROUND = 'gallery/images/back.png'
PIPE = 'gallery/images/pipe.png'
def welcomscreen():
    playerx= int(SCREENWIDTH/5)
    playery= int(SCREENHEIGHT- GAME_SPRITES['player'].get_height()/2)
    messagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_width()-50)
    messagey = int(SCREENHEIGHT*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, 425))    
                pygame.display.update()
                FPSLOCK.tick(FPS)
def mainGame():
    score = 0
    playerx=int(SCREENWIDTH/5)                
    playery=int(SCREENHEIGHT/2)
    basex= 0
    newpipe1= getrandompipe()
    newpipe2= getrandompipe()

    upperpipes= [
        {'x':SCREENWIDTH+200, 'y':newpipe1[0]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newpipe1[0]['y']}
    ]
    lowerpipes= [
        {'x':SCREENWIDTH+200, 'y':newpipe2[1]['y']},
        {'x':SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newpipe2[1]['y']}
    ]
    pipevelx=-4
    playervely=-9
    playermaxvely=10
    playerminvely=-8
    playeraccy=1
    playerflapaccv=-8
    playerflapped = False
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN and(event.key==K_SPACE or event.key==K_UP):
                if playery>0:
                    playervely=playerflapaccv
                    playerflapped=True
                    GAME_SOUNDS['wing'].play()
        crashTest=isCollide(playerx, playery, upperpipes, lowerpipes)
        if crashTest:
            return

        playermid=playerx+GAME_SPRITES['player'].get_width()/2
        for pipe in upperpipes:
            pipemid=pipe['x']+GAME_SPRITES['pipe'][0].get_width()/2
            if pipemid<=playermid<pipemid+4:
                score+=1
                print(f"your score is {score}")
                GAME_SOUNDS['point'].play()


        if playervely<playermaxvely and not playerflapped:
            playervely+=playeraccy
        if playerflapped:
            playerflapped= False
        playerheight=GAME_SPRITES['player'].get_height()
        playery=playery+min(playervely,GROUNDY-playery-playerheight) 
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            upperpipe['x']+=pipevelx
            lowerpipe['x']+=pipevelx
        if 0<upperpipes[0]['x']<5:
            newpipe=getrandompipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])


        if upperpipes[0]['x']< -(GAME_SPRITES['pipe'][0].get_width()):
            upperpipes.pop(0)
            lowerpipes.pop(0)  
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperpipe,lowerpipe in zip(upperpipes,lowerpipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperpipe['x'],upperpipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerpipe['x'],lowerpipe['y']))    

        SCREEN.blit(GAME_SPRITES['base'],(basex,425))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
        mydigits=[int(x) for x in list(str(score))]
        width=0
        for digit in mydigits:
            width+=GAME_SPRITES['numbers'][digit].get_width()
        xoffset=(SCREENWIDTH-width)/2

        for digit in mydigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],(xoffset,SCREENHEIGHT*0.12))
            xoffset+=GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSLOCK.tick(FPS)
def isCollide(playerx, playery, upperpipes, lowerpipes):
    if playery> GROUNDY-25 or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    for pipe in upperpipes:
        pipeheight= GAME_SPRITES['pipe'][0].get_height()
        if(playery<pipeheight+pipe['y']and abs(playerx-pipe['x'])<GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    for pipe in lowerpipes:
        if(playery+GAME_SPRITES['player'].get_height()>pipe['y']) and (abs(playerx-pipe['x'])<GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True


    
    return False

def getrandompipe():
    pipeheight=GAME_SPRITES['pipe'][0].get_height()
    offset= SCREENHEIGHT/3
    y2=offset+random.randrange(0, int(SCREENHEIGHT-GAME_SPRITES['base'].get_height()-1.2*offset))
    pipex=SCREENWIDTH+10
    y1=pipeheight-y2+offset
    pipe=[
        {'x':pipex, 'y':-y1},
        {'x':pipex, 'y':y2}
    ]
    return pipe





if __name__ == "__main__":
    pygame.init()
    FPSLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy bird by vasu')
    GAME_SPRITES['numbers']=(
        pygame.image.load('gallery/images/0.png').convert_alpha(),
        pygame.image.load('gallery/images/1.png').convert_alpha(),
        pygame.image.load('gallery/images/2.png').convert_alpha(),
        pygame.image.load('gallery/images/3.png').convert_alpha(),
        pygame.image.load('gallery/images/4.png').convert_alpha(),
        pygame.image.load('gallery/images/5.png').convert_alpha(),
        pygame.image.load('gallery/images/6.png').convert_alpha(),
        pygame.image.load('gallery/images/7.png').convert_alpha(),
        pygame.image.load('gallery/images/8.png').convert_alpha(),
        pygame.image.load('gallery/images/9.png').convert_alpha())
    GAME_SPRITES['message']=pygame.image.load('gallery/images/start.png').convert_alpha()
    GAME_SPRITES['base']=pygame.image.load('gallery/images/base.png').convert_alpha()
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
        pygame.image.load(PIPE).convert_alpha()
        )
    GAME_SOUNDS['die']= pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit']= pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point']= pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['wing']= pygame.mixer.Sound('gallery/audio/wing.wav')
    GAME_SOUNDS['swoosh']= pygame.mixer.Sound('gallery/audio/swoosh.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomscreen()
        mainGame()
