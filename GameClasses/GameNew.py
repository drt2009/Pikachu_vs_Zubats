import pygame
import random
import time
from Pikachu import Pikachu
from Zubat import Zubat
from Bullet import Bullet
from Background import Background

#TODO: figure out why loop isnt working
class Game():
    #lastHit=1 for right and 0 for left
    lastHit=1
    isMuted=False
    screen_width=700
    screen_height=500
    
    def __setupBackground(self):
        background = Background()
        background.rect.width=self.screen_width
        background.rect.height=self.screen_height
        background.rect.y=-150
        background.rect.x=-150
        self.backgroundPlain = pygame.sprite.RenderPlain()
        self.backgroundPlain.add(background)
        #draws the background to the screen
        self.backgroundPlain.draw(self.screen)
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
                if event.type == pygame.QUIT:
                    self.done=True
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
        self.done=False
        self.__instructions()
        if self.done:
            return
        self.__setupSpritesLists()
        self.__createPlayer()
        self.__setupBackground()
    
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
        if self.zubatsSpawnWaitTime==0:
            self.screen.blit(text2, (text2x,text2y))
        pygame.display.flip()
        time.sleep(2)
    
    
    def __displayScoreOnScreen(self):
        myfont = pygame.font.Font(None, 24)
        text = myfont.render(("Score: "+str(self.player.pikaScore)), True, (180,0,16))
        text_rect = text.get_rect()
        textx = self.screen_width-text_rect.width
        texty = 1
        self.screen.blit(text, (textx,texty))
        pygame.display.flip()
    
    def __addBulletToList(self, bullet, bulletList):
        if len(bulletList)<5:
                self.all_sprites_list.add(bullet)
                bulletList.add(bullet)

    def __keyDownEvents(self, event):
        if event.key == pygame.K_LEFT:
            self.player.changespeed(-4,0)
            self.lastHit=0
        elif event.key == pygame.K_RIGHT:
            self.player.changespeed(4,0)
            self.lastHit=1
        elif event.key == pygame.K_UP:
            self.player.changespeed(0,-3)
        elif event.key == pygame.K_DOWN:
            self.player.changespeed(0,3)
        elif event.key == pygame.K_SPACE:
            bullet=Bullet()
            if self.lastHit==1:
                bullet.speed=(5+(self.player.x_speed/2.0))
                bullet.rect.x = self.player.rect.x+self.player.rect.width
                bullet.rect.y = self.player.rect.y+(self.player.rect.height/4)+2
                self.__addBulletToList(bullet, self.bulletListRight)
            else:
                bullet.speed=(-5+(self.player.x_speed/2.0))
                bullet.rect.x = self.player.rect.x-10
                bullet.rect.y = self.player.rect.y+(self.player.rect.height/2)
                self.__addBulletToList(bullet, self.bulletListLeft)
    
    def __pauseGame(self):
        pygame.mixer.music.pause()
        myfont = pygame.font.Font(None, 36)
        text = myfont.render(("Pause"), True, (180,0,16))
        text_rect = text.get_rect()
        textx = self.screen.get_width()/2 - text_rect.width/2
        texty = self.screen.get_height()/2 - text_rect.height/2
        self.screen.blit(text, (textx,texty))
        pygame.display.flip()
        unpause=False
        while not unpause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done=True
                    unpause=True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        unpause=True
        pygame.mixer.music.unpause()
    
    def __keyUpEvents(self, event):
        if event.key == pygame.K_LEFT:
            self.player.changespeed(4,0)
        elif event.key == pygame.K_RIGHT:
            self.player.changespeed(-4,0)
        elif event.key == pygame.K_UP:
            self.player.changespeed(0,3)
        elif event.key == pygame.K_DOWN:
            self.player.changespeed(0,-3)
        elif event.key == pygame.K_p:
            self.__pauseGame()
        elif event.key == pygame.K_m:
            if self.isMuted:
                pygame.mixer.music.play(-1,.5)
                self.isMuted=False
            else:
                pygame.mixer.music.stop()
                self.isMuted=True
    
    def __spawnZubats(self):
        if(self.numOfZubats<self.maxZubatsPerLevel):
            currentTime=time.clock()-self.oldTime
            if(currentTime>self.zubatsSpawnWaitTime):
                #sets the old time to the current time on the clock
                self.oldTime=time.clock()
                z=Zubat()
                #decides what side of the screen to spawn from
                temp=random.randrange(2)
                if(temp==0):
                    z.rect.x=0-z.rect.width
                    z.rect.y = random.randrange(self.screen_height)
                else:
                    z.rect.x=self.screen_width
                    z.rect.y = random.randrange(self.screen_height)
                self.zubats.add(z)
                self.all_sprites_list.add(z)
                self.numOfZubats+=1
                    
    def __checkAndLoopPlayerAroundScreen(self, player):
        if(player.rect.x <0-player.rect.width):
            player.rect.x=self.screen_width
        if(player.rect.x >self.screen_width):
            player.rect.x=0-player.rect.width
        if(player.rect.y < 0-player.rect.height):
            player.rect.y = self.screen_height
        if(player.rect.y > self.screen_height):
            player.rect.y=0-player.rect.height
    
    def __moveZubatAtPikachu(self, zubat):
        if(zubat.rect.x+(zubat.rect.width/2)>self.player.rect.x+(self.player.rect.width/2)):
            zubat.rect.x-=2
            zubat.speed=-1
        elif(zubat.rect.x+(zubat.rect.width/2)<self.player.rect.x+(self.player.rect.width/2)):
            zubat.rect.x+=2
            zubat.speed=1
        if(zubat.rect.y+(zubat.rect.height/2)>self.player.rect.y+(self.player.rect.height/2)):
            zubat.rect.y-=1
        elif(zubat.rect.y+(zubat.rect.height/2)<self.player.rect.y+(self.player.rect.height/2)):
            zubat.rect.y+=1
    
    def __bulletHitsZubat(self, zubat, bullet, bulletList):
        bulletList.remove(bullet)
        self.zubats.remove(zubat)
        self.all_sprites_list.remove(bullet)
        self.all_sprites_list.remove(zubat)
        score=random.randrange(75,125)
        self.player.pikaScore+=score
    
    def __checkAndUpdatesHighScore(self, initials):  
        isFirstLine = True
        highScores={}
        highScore=open('HighScore.txt','r')
        for line in highScore:
            if(isFirstLine):
                firstline=line
                isFirstLine = False
                continue
            temp=[]
            split=line.split("\t\t")
            temp.append(split[1])
            temp.append(split[2])
            temp.append(int(split[3]))
            highScores[split[0]]=temp
        highScore.close()
        playerStats=[]
        playerStats.append(initials)
        playerStats.append(str(self.player.level))
        playerStats.append(self.player.pikaScore)
        #goes through the dictionary and sees where the current player needs to get added
        #then will bump the person at the spot move down one
        for x in range((len(highScores))):
            if (highScores[str(len(highScores)-x)+")"][2]<self.player.pikaScore):
                highScores[str(len(highScores)-x+1)+")"]=highScores[str(len(highScores)-x)+")"]
                highScores[str(len(highScores)-x)+")"]=playerStats
        highScore=open('HighScore.txt','w')
        highScore.write(firstline)
        for x in range(1,11):
            highScore.write(str(x)+")\t\t"+highScores[str(x)+")"][0]+"\t\t"\
                            +highScores[str(x)+")"][1]+"\t\t"+str(highScores[str(x)+")"][2])+"\t\t\n")
        highScore.close()

    def __gameEndStats(self):
        playAgain = False
        while playAgain==False:
            myfont = pygame.font.Font(None, 36)
    
            #makes four lines to print to the screen
            text = myfont.render("Game Over", True, (180,0,16))
            text1 = myfont.render(("Level: "+str(self.player.level)), True, (180,0,16))
            text2 = myfont.render(("Score: "+str(self.player.pikaScore)), True, (180,0,16))
            text3 = myfont.render("Press ENTER to play again", True, (180,0,16))
    
            text_rect = text.get_rect()
            text1_rect = text1.get_rect()
            text2_rect = text2.get_rect()
            text3_rect = text3.get_rect()
    
            text1x = self.screen.get_width()/2 - text1_rect.width/2
            text1y = self.screen.get_height()/2 - text1_rect.height
    
            textx=(text1x+text1_rect.width/2)-text_rect.width/2
            texty=text1y-text_rect.height
            text2x=(text1x+text1_rect.width/2)-text2_rect.width/2
            text2y=text1y+text1_rect.height
            text3x=(text1x+text1_rect.width/2)-text3_rect.width/2
            text3y=text2y+text2_rect.height
    
            self.screen.blit(text, (textx,texty))
            self.screen.blit(text1, (text1x,text1y))
            self.screen.blit(text2, (text2x,text2y))
            self.screen.blit(text3, (text3x,text3y))
    
            pygame.display.flip()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    self.done=True # Flag that shows game is over
                    playAgain=True #Flag that they entered something to get out of loop
    
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Game()
                        self.done=True
                        playAgain=True #Flag to show they want to play again

    
    def __endGame(self):
        def askForInitials():
            self.screen.fill((0,0,0))
            myfont = pygame.font.Font(None, 36)
            text = myfont.render("Please enter you initials", True, (180,0,16))
            text2= myfont.render((""+initials+blankInitials[numberOfInitials:]),True, (180,0,16))
            text_rect = text.get_rect()
            text2_rect = text2.get_rect()
            self.screen.blit(text,(self.screen_width/2-text_rect.width/2,self.screen_height/2-text_rect.height/2\
                          -text_rect.height-text_rect.height-text_rect.height-text_rect.height\
                          -text_rect.height))
            self.screen.blit(text2,(self.screen_width/2-text2_rect.width/2,self.screen_height/2-text_rect.height/2\
                          -text_rect.height-text_rect.height-text_rect.height-text_rect.height))
            pygame.display.flip()
        blankInitials="---"
        initials=""
        initialsEntered=False
        numberOfInitials=0  
        while not(initialsEntered):
            self.screen.fill((0,0,0))
            askForInitials()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key>=97 and event.key<=122:
                        initials+=pygame.key.name(event.key).upper()
                        numberOfInitials+=1
                    if numberOfInitials ==3:
                        askForInitials()
                        initialsEntered=True
        self.__checkAndUpdatesHighScore(initials)
        self.__gameEndStats()
        
      
    def __zubatLogic(self, zubat):
        self.__moveZubatAtPikachu(zubat)
        if(pygame.sprite.collide_circle(self.player,zubat)):
                self.all_sprites_list.empty()
                self.__endGame()
                self.done=True
        for bullet in self.bulletListRight:
            if pygame.sprite.collide_rect(bullet,zubat):
                self.__bulletHitsZubat(zubat, bullet, self.bulletListRight)
        for bullet in self.bulletListLeft:
            if pygame.sprite.collide_rect(bullet,zubat):
                self.__bulletHitsZubat(zubat, bullet, self.bulletListLeft)
        zubat.selectPicture() 
                        
    def __levelLoop(self):
        while(len(self.zubats)!=0 or self.numOfZubats!=self.maxZubatsPerLevel):
            self.__displayScoreOnScreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done=True
                    return
                elif event.type == pygame.KEYDOWN:
                    self.__keyDownEvents(event)
                elif event.type == pygame.KEYUP:
                    self.__keyUpEvents(event)
            self.__spawnZubats()
            for player in self.playerList:
                self.__checkAndLoopPlayerAroundScreen(player)
            for zubat in self.zubats:
                self.__zubatLogic(zubat)
            for bullet in self.bulletListRight:
                bullet.rect.x += bullet.speed
                if bullet.rect.x > self.screen_width:
                        self.bulletListRight.remove(bullet)
            for bullet in self.bulletListLeft:
                bullet.rect.x += bullet.speed
                if bullet.rect.x < 0-(bullet.rect.width):
                    self.bulletListLeft.remove(bullet)
            self.screen.fill((0,0,0))
            self.player.selectPicture()
            self.backgroundPlain.draw(self.screen)
            self.all_sprites_list.draw(self.screen)
            # Limit to 20 frames per second
            self.clock.tick(20)

    def __gameLoop(self):
        while not self.done:
            self.player.level+=1
            self.__preLevelSetup()
            self.__preLevelDisplayInfo()
            self.numOfZubats=0
            self.oldTime=time.clock()
            self.__levelLoop()
        return
    
    def __init__(self):
        self.__setupGame()
        if self.done:
            return
        self.clock=pygame.time.Clock();
        self.__gameLoop()