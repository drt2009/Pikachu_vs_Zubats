#The Pikachu class controls everything for the person playing keeps scores what level
#they are on and updates the pictures to get the walking motion
import pygame

class Pikachu(pygame.sprite.Sprite):
    
    imageBackground = (246,246,246)
    
    x_speed=0
    y_speed=0

    currentImage=0

    pikaScore=0
    level=1

    #constructor
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Holds all of the pika images
        self.pikas=[]

        #Reads in the pictures for the sprite of the player
        for i in range (1,9):
            tempPika = pygame.image.load("Pictures/Pikachu/pik"+str(i)+".png").convert()
            tempPika.set_colorkey(self.imageBackground)
            self.pikas.append(tempPika)

        #Starts the images so it is facing right
        self.image=self.pikas[5]

        #gets the rectangle around the picture
        self.rect=self.image.get_rect()

    #Changes the speed so the pikachu can move
    def changespeed(self,x,y):
        self.x_speed+=x
        self.y_speed+=y

    #changes the position of the image on the screen and then cycles through the images and changes sides
    #based on what way the speed is going
    def update(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        #Decides what image to display
        if self.x_speed<0:
            self.currentImage+=1
            if self.currentImage >3*4:
                self.currentImage=0
            self.image=self.pikas[self.currentImage//4]
        elif self.x_speed>0:
            self.currentImage+=1
            if self.currentImage >3*4:
                self.currentImage=0
            self.image=self.pikas[self.currentImage//4+4]
