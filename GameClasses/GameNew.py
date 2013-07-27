import pygame
import random
import time
from Pikachu import Pikachu
from Zubat import Zubat
from Bullet import Bullet
from Background import Background
import os

class Game():
    #lastHit=1 for right and 0 for left
    lastHit=1
    done=False
    isMuted=False
    screen_width=700
    screen_height=500
    
    def __setupBackground(self):
        background = Background()
        background.rect.width=self.screen_width
        background.rect.height=self.screen_height
        background.rect.y=-150
        background.rect.x=-150
        backgroundPlain = pygame.sprite.RenderPlain()
        backgroundPlain.add(background)
        #draws the background to the screen
        backgroundPlain.draw(self.screen)
        pygame.display.flip()

    def __instructions(self):

        myfont = pygame.font.Font(None, 32)
        text1 = myfont.render("Pikachu vs. Zubats", True, (180,0,16))
        text2 = myfont.render("Instructions", True, (180,0,16))
        text3 = myfont.render("Arrow Keys: Move in Direction", True, (180,0,16))
        text4 = myfont.render("Space Bar: Shoots lightning bolt", True, (180,0,16))
        text5 = myfont.render("Press ENTER to continue", True, (180,0,16))
        
        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()
        text3_rect = text3.get_rect()
        text4_rect = text4.get_rect()
        text5_rect = text5.get_rect()

        text1x=self.screen_width/2-text1_rect.width/2
        text1y=self.screen_height/2-text1_rect.height/2-text4_rect.height-text3_rect.height-text2_rect.height\
                -text1_rect.height

        text2x=self.screen_width/2-text2_rect.width/2
        text2y=self.screen_height/2-text2_rect.height/2-text4_rect.height-text3_rect.height

        text3x=self.screen_width/2-text3_rect.width/2
        text3y=self.screen_height/2-text3_rect.height/2-text4_rect.height

        text4x=self.screen_width/2-text4_rect.width/2
        text4y=self.screen_height/2-text4_rect.height/2

        text5x=self.screen_width/2-text5_rect.width/2
        text5y=self.screen_height/2-text5_rect.height/2+text4_rect.height+text4_rect.height

        self.screen.blit(text1, (text1x,text1y))
        self.screen.blit(text2, (text2x,text2y))
        self.screen.blit(text3, (text3x,text3y))
        self.screen.blit(text4, (text4x,text4y))
        self.screen.blit(text5, (text5x,text5y))

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that shows game is over
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def __setupSpritesLists(self):
        self.all_sprites_list = pygame.sprite.RenderPlain()
        self.playerList= pygame.sprite.RenderPlain()
        self.bulletListRight= pygame.sprite.RenderPlain()
        self.bulletListLeft= pygame.sprite.RenderPlain()
        self.zubats=pygame.sprite.RenderPlain()

    def __createPlayer(self):
        self.player = Pikachu()
        self.player.rect.x=(self.screen_width/2)-(self.player.rect.width/2)
        self.player.rect.y=(self.screen_height/2)-(self.player.rect.height/2)
        self.all_sprites_list.add(self.player)
        self.playerList.add(self.player)
    
    def __setupGame(self):
        self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])
        self.__instructions()
        if self.done:
            return
        self.__createPlayer()
        self.__setupBackground()
        self.__setupSpritesLists()
    
    def __preLevelSetup(self):
        self.maxZubatsPerLevel=random.randrange((4*self.player.level),(7*self.player.level))
        self.zubatsSpawnWaitTime=random.randrange(10)/float(self.player.level)
        
    def __preLevelDisplayInfo(self):
        myfont = pygame.font.Font(None, 36)
        text = myfont.render(("Level "+str(self.player.level)), True, (180,0,16))
        text2 = myfont.render(("Repels' effect wore off..."), True, (180,0,16))
        text_rect = text.get_rect()
        text_rect2=text2.get_rect()
        textx = self.screen.get_width()/2 - text_rect.width/2
        texty = self.screen.get_height()/2 - text_rect.height/2
        text2x = self.screen.get_width()/2 - text_rect2.width/2
        text2y = self.screen.get_height()/2 - text_rect.height/2+text_rect.height
        self.screen.blit(text, (textx,texty))
        if self.waitTime==0:
            self.screen.blit(text2, (text2x,text2y))

        pygame.display.flip()
        time.sleep(2)
    
    #TODO: Finish This is where i stopped    
    def levelLoop(self):
        while True:
            numOfZubats=0
            oldTime=time.clock()
        
            if(self.done==True):
                return
            self.player.level+=1
    
    def __init__(self):
        self.__setupGame()
        if self.done:
            return
        self.clock=pygame.time.Clock();
        os.system("pause")
    
    