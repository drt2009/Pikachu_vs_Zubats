def HighScore(initials, player):

    #Opens the HighScore file for reading
    highScore=open('HighScore.txt','r')

    isFirstLine = True
    firstline=""
    highScores={}
    #Reads in the file
    for line in highScore:
        #Reads in the header line
        if(isFirstLine):
            firstline=line
            isFirstLine = False
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
    #then will bump the person at the spot down one
    for x in range((len(highScores))+1):
        print highScores[str(len(highScores)-x)+")"]
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
