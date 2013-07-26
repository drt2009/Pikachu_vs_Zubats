import pygame
import random
import time
from Pikachu import Pikachu
from Zubat import Zubat
from Bullet import Bullet
from Background import Background

#lastHit=1 for right and 0 for left
lastHit=1
done=False
isMuted=False

#Function that does all the programming for the game.  Starts a window
#Has end game game takes in initials and displays them to the screen
#to update high scores
def Game():

    #allows the gloabal variables to be changed
    global lastHit
    global done
    global isMuted

    #This funciton will define and call a funciton to get initals and print
    #them to the screen
    def endGame():
        def askForInitials():
            screen.fill((0,0,0))
            myfont = pygame.font.Font(None, 36)
            text = myfont.render("Please enter you initials", True, (180,0,16))
            text2= myfont.render((""+initials+blankInitials[count:]),True, (180,0,16))
            text_rect = text.get_rect()
            text2_rect = text2.get_rect()
            screen.blit(text,(screen_width/2-text_rect.width/2,screen_height/2-text_rect.height/2\
                          -text_rect.height-text_rect.height-text_rect.height-text_rect.height\
                          -text_rect.height))
            screen.blit(text2,(screen_width/2-text2_rect.width/2,screen_height/2-text_rect.height/2\
                          -text_rect.height-text_rect.height-text_rect.height-text_rect.height))
            pygame.display.flip()

        #Sets a flag for the while loop
        playAgain=False

        #sets variables for the intitials and blank spots that will get printed to
        #the screen when getting initials
        blankInitials="---"
        initials=""

        #Sets a flag for the loop that will allow it to be ran three times
        #This is needed because while loops work great with stopping pygame
        #code so nothing else runs(That is why a for loop didnt work)
        initialsEntered=False
        count=0

        #Loops to ask for initials and will only take the lower case letters
        #with the if for the ascii key numbers
        while not(initialsEntered):
            screen.fill((0,0,0))
            askForInitials()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key>=97 and event.key<=122:
                        initials+=pygame.key.name(event.key).upper()

                        count+=1
                    if count==3:
                        askForInitials()
                        initialsEntered=True
                        break

        #Opens the HighScore file for reading
        highScore=open('HighScore.txt','r')

        fileLine=0
        firstline=""
        highScores={}
        #Reads in the file
        for line in highScore:
            #Reads in the header line
            if(fileLine==0):
                firstline=line
                fileLine+=1
                continue
            #Gets the name,level, and score of the players
            temp=[]
            #splits the info into 3 different parts then save them to
            #the dictionary
            split=line.split("\t\t")
            temp.append(split[1])
            temp.append(split[2])
            temp.append(int(split[3]))
            highScores[split[0]]=temp

        #closes the read on the highscore list
        highScore.close()
        playerStats=[]
        #makes a list of the current player stats so they can be comparied against
        #the list
        playerStats.append(initials)
        playerStats.append(str(player.level))
        playerStats.append(player.pikaScore)

        #goes through the dictionary and sees where the current player needs to get added
        #then will bump the person at the spot move down one
        for x in range((len(highScores))):
            if (highScores[str(len(highScores)-x)+")"][2]<player.pikaScore):
                highScores[str(len(highScores)-x+1)+")"]=highScores[str(len(highScores)-x)+")"]
                highScores[str(len(highScores)-x)+")"]=playerStats

        #Opens a high score list for writing that will delete the old list
        #then replace it with the new names that go on it
        highScore=open('HighScore.txt','w')
        highScore.write(firstline)
        for x in range(1,11):
            highScore.write(str(x)+")\t\t"+highScores[str(x)+")"][0]+"\t\t"\
                            +highScores[str(x)+")"][1]+"\t\t"+str(highScores[str(x)+")"][2])+"\t\t\n")

        #closes the high score list
        highScore.close()

        while playAgain==False:
            myfont = pygame.font.Font(None, 36)

            #makes four lines to print to the screen
            text = myfont.render("Game Over", True, (180,0,16))
            text1 = myfont.render(("Level: "+str(player.level)), True, (180,0,16))
            text2 = myfont.render(("Score: "+str(player.pikaScore)), True, (180,0,16))
            text3 = myfont.render("Press ENTER to play again", True, (180,0,16))

            text_rect = text.get_rect()
            text1_rect = text1.get_rect()
            text2_rect = text2.get_rect()
            text3_rect = text3.get_rect()

            text1x = screen.get_width()/2 - text1_rect.width/2
            text1y = screen.get_height()/2 - text1_rect.height

            textx=(text1x+text1_rect.width/2)-text_rect.width/2
            texty=text1y-text_rect.height
            text2x=(text1x+text1_rect.width/2)-text2_rect.width/2
            text2y=text1y+text1_rect.height
            text3x=(text1x+text1_rect.width/2)-text3_rect.width/2
            text3y=text2y+text2_rect.height

            screen.blit(text, (textx,texty))
            screen.blit(text1, (text1x,text1y))
            screen.blit(text2, (text2x,text2y))
            screen.blit(text3, (text3x,text3y))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    global done
                    done=True # Flag that shows game is over
                    playAgain=True #Flag that they entered something to get out of loop

                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        playAgain=True #Flag to show they want to play again



        if done==False:
            Game()
    #Prints instructions to the screen
    def instructions():
        global done

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

        text4x=screen_width/2-text4_rect.width/2
        text4y=screen_height/2-text4_rect.height/2

        text3x=screen_width/2-text3_rect.width/2
        text3y=screen_height/2-text3_rect.height/2-text4_rect.height

        text2x=screen_width/2-text2_rect.width/2
        text2y=screen_height/2-text2_rect.height/2-text4_rect.height-text3_rect.height

        text5x=screen_width/2-text5_rect.width/2
        text5y=screen_height/2-text5_rect.height/2+text4_rect.height+text4_rect.height

        text1x=screen_width/2-text1_rect.width/2
        text1y=screen_height/2-text1_rect.height/2-text4_rect.height-text3_rect.height-text2_rect.height\
                -text1_rect.height

        screen.blit(text1, (text1x,text1y))
        screen.blit(text2, (text2x,text2y))
        screen.blit(text3, (text3x,text3y))
        screen.blit(text4, (text4x,text4y))
        screen.blit(text5, (text5x,text5y))

        pygame.display.flip()
        while True:
            goToGame=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that shows game is over
                    goToGame=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        goToGame=True
            if goToGame:
                break

    # Initialize Pygame
    pygame.init()

    # Set the height and width of the screen
    screen_width=700
    screen_height=500
    screen=pygame.display.set_mode([screen_width,screen_height])

    #Sets the game window title
    pygame.display.set_caption("Pikachu vs. Zubats")

    #calls the instructions which will print the instructions to the screen
    instructions()

    #creats the backgound then adds it to a background list
    background = Background()
    background.rect.width=screen_width
    background.rect.height=screen_height
    background.rect.y=-150
    background.rect.x=-150

    backgroundPlain = pygame.sprite.RenderPlain()
    backgroundPlain.add(background)

    #draws the background to the screen
    backgroundPlain.draw(screen)

    # This is a list of every sprite.
    all_sprites_list = pygame.sprite.RenderPlain()

    playerList= pygame.sprite.RenderPlain()

    # Create a pikachu player
    player = Pikachu()
    player.rect.x=(screen_width/2)-(player.rect.width/2)
    player.rect.y=(screen_height/2)-(player.rect.height/2)
    all_sprites_list.add(player)
    playerList.add(player)


    # Used to manage how fast the screen updates
    clock=pygame.time.Clock()

    #Creats a sprite list that will then be able to loop through
    bulletListRight= pygame.sprite.RenderPlain()
    bulletListLeft= pygame.sprite.RenderPlain()
    zubats=pygame.sprite.RenderPlain()

   

    while True:

        #Counts the number of zubats that were sent out in the current level
        numOfZubats=0

        #The max number of zubats for the level
        maxZubatsPerLevel=random.randrange((4*player.level),(7*player.level))

        #The to wait between when zubats will be sent out
        waitTime=random.randrange(10)/float(player.level)

        #the time on the clock to know when to send out the first zubat
        oldTime=time.clock()

        #Prints the level and then if repels effect wore off when the spawn time
        #is 0
        myfont = pygame.font.Font(None, 36)
        text = myfont.render(("Level "+str(player.level)), True, (180,0,16))
        text2 = myfont.render(("Repels' effect wore off..."), True, (180,0,16))

        text_rect = text.get_rect()
        text_rect2=text2.get_rect()
        textx = screen.get_width()/2 - text_rect.width/2
        texty = screen.get_height()/2 - text_rect.height/2
        text2x = screen.get_width()/2 - text_rect2.width/2
        text2y = screen.get_height()/2 - text_rect.height/2+text_rect.height
        screen.blit(text, (textx,texty))
        if waitTime==0:
            screen.blit(text2, (text2x,text2y))

        pygame.display.flip()
        time.sleep(2)

        # -------- Main Program Loop -----------
        while done==False:

            myfont = pygame.font.Font(None, 24)
            text = myfont.render(("Score: "+str(player.pikaScore))\
                                    , True, (180,0,16))
            text_rect = text.get_rect()
            textx = screen_width-text_rect.width
            texty = 1
            screen.blit(text, (textx,texty))

            pygame.display.flip()


            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop



                if event.type == pygame.KEYDOWN:
                    #The first four control the speed of the player based on direction key
                    if event.key == pygame.K_LEFT:
                        player.changespeed(-4,0)
                        lastHit=0
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(4,0)
                        lastHit=1
                    if event.key == pygame.K_UP:
                        player.changespeed(0,-3)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0,3)

                    #Checks to see if space is pressed, if it is and the number of bullets in the direct is not
                    #already maxed out will shoot a bullet in the last direction pikachu was facing
                    if event.key == pygame.K_SPACE:
                        bullet=Bullet()
                        if lastHit==1:
                            bullet.speed=(5+(player.x_speed/2.0))
                            bullet.rect.x = player.rect.x+player.rect.width
                            bullet.rect.y = player.rect.y+(player.rect.height/4)+2
                            if len(bulletListRight)<5:
                                all_sprites_list.add(bullet)
                                bulletListRight.add(bullet)
                        else:
                            bullet.speed=(-5+(player.x_speed/2.0))
                            bullet.rect.x = player.rect.x-10
                            bullet.rect.y = player.rect.y+(player.rect.height/2)
                            if len(bulletListLeft)<5:
                                all_sprites_list.add(bullet)
                                bulletListLeft.add(bullet)
                    #Test code to check if zubats are working, or code if you just want to make the current level
                    #harder it will just add more zubats at a random point on the screen
                    if event.key == pygame.K_LALT:
                        z=Zubat()
                        z.rect.x = random.randrange(screen_width)
                        z.rect.y = random.randrange(screen_height)
                        zubats.add(z)
                        all_sprites_list.add(z)



                # Reset speed of pikachu when key is released
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed(4,0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed(-4,0)
                    if event.key == pygame.K_UP:
                        player.changespeed(0,3)
                    if event.key == pygame.K_DOWN:
                        player.changespeed(0,-3)
                    #checks to see if the game is paused or not and then does
                    #the oppisite, also it pauses the music while paused
                    if event.key == pygame.K_p:
                        pygame.mixer.music.pause()
                        myfont = pygame.font.Font(None, 36)
                        text = myfont.render(("Pause"), True, (180,0,16))
                        text_rect = text.get_rect()
                        textx = screen.get_width()/2 - text_rect.width/2
                        texty = screen.get_height()/2 - text_rect.height/2
                        screen.blit(text, (textx,texty))

                        pygame.display.flip()

                        while True:
                            unpause=False
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT: # If user clicked close
                                    done=True # Flag that shows game is over
                                    unpause=True
                                if event.type == pygame.KEYUP:
                                    if event.key == pygame.K_p:
                                        unpause=True
                            if unpause:
                                pygame.mixer.music.unpause()
                                break
                    #Checks to see if the music is muted or unmuted then does the oppiset
                    if event.key == pygame.K_m:
                        if isMuted:
                            pygame.mixer.music.play(-1,.5)
                            isMuted=False
                        else:
                            pygame.mixer.music.stop()
                            isMuted=True

            #Spawns new zubats if the number of zubats is under the level max
            if(numOfZubats<maxZubatsPerLevel):
                currentTime=time.clock()-oldTime
                #Checks to see if the wait time was passed if it was will spawn a zubat on the edge of the screen
                if(currentTime>waitTime):
                    #sets the old time to the current time on the clock
                    oldTime=time.clock()
                    z=Zubat()
                    #decides what side of the screen to spawn from
                    temp=random.randrange(2)
                    if(temp==0):
                        z.rect.x=0-z.rect.width
                        z.rect.y = random.randrange(screen_height)
                    else:
                        z.rect.x=screen_width
                        z.rect.y = random.randrange(screen_height)
                    zubats.add(z)
                    all_sprites_list.add(z)
                    numOfZubats+=1
            #Checks the position of Pikachu, when Pikachu goes
            #off the screen he will loop around to the opposite end of the screen
            for player in playerList:
                if(player.rect.x <0-player.rect.width):
                    player.rect.x=screen_width
                if(player.rect.x >screen_width):
                    player.rect.x=0-player.rect.width
                if(player.rect.y < 0-player.rect.height):
                    player.rect.y = screen_height
                if(player.rect.y > screen_height):
                    player.rect.y=0-player.rect.height


            #Loops through zubat to move them and check if they hit pikachu or get hit by a lightning bolt
            for zubat in zubats:
                #checks the x postion of zubat and pikachu and moves zubat towards pikachu
                #also sets the speed which is used to flip the zubat picture opsite direction
                if(zubat.rect.x+(zubat.rect.width/2)>player.rect.x+(player.rect.width/2)):
                    zubat.rect.x-=2
                    zubat.speed=-1
                elif(zubat.rect.x+(zubat.rect.width/2)<player.rect.x+(player.rect.width/2)):
                    zubat.rect.x+=2
                    zubat.speed=1
                #checks the y postion of zubat and pikachu and moves zubat towards pikachu
                if(zubat.rect.y+(zubat.rect.height/2)>player.rect.y+(player.rect.height/2)):
                    zubat.rect.y-=1
                elif(zubat.rect.y+(zubat.rect.height/2)<player.rect.y+(player.rect.height/2)):
                    zubat.rect.y+=1
                #Checks to see if zubat kills(hit) pikachu
                if(pygame.sprite.collide_circle(player,zubat)):
                        #empyt the sprites list so nothing is on the screen
                        all_sprites_list.empty()
                        endGame()
                        done=True
                #These two loops checks to see if a zubat is hit by a bullet going either direction
                for bullet in bulletListRight:
                    if pygame.sprite.collide_rect(bullet,zubat):
                        bulletListRight.remove(bullet)
                        zubats.remove(zubat)
                        all_sprites_list.remove(bullet)
                        all_sprites_list.remove(zubat)
                        score=random.randrange(75,125)
                        player.pikaScore+=score
                for bullet in bulletListLeft:
                    if pygame.sprite.collide_rect(bullet,zubat):
                        bulletListLeft.remove(bullet)
                        zubats.remove(zubat)
                        all_sprites_list.remove(bullet)
                        all_sprites_list.remove(zubat)
                        score=random.randrange(75,125)
                        player.pikaScore+=score
                #Calls the update to move them and check to see if the picture needs flipping
                zubat.selectPicture()
            #These two for loops move the bullets o
            for bullet in bulletListRight:
                bullet.rect.x += bullet.speed
                if bullet.rect.x > screen_width:
                        bulletListRight.remove(bullet)

            for bullet in bulletListLeft:
                bullet.rect.x += bullet.speed
                if bullet.rect.x < 0-(bullet.rect.width):
                    bulletListLeft.remove(bullet)

            # Clear the screen
            screen.fill((0,0,0))
            player.selectPicture()
            backgroundPlain.draw(screen)
            # Draw all the spites
            all_sprites_list.draw(screen)

            # Limit to 20 frames per second
            clock.tick(20)

            # Updates Screen.
            pygame.display.flip()
            if(len(zubats)==0 and numOfZubats==maxZubatsPerLevel):
                break
        if(done==True):
            break
        else:
            player.level+=1

    pygame.quit()