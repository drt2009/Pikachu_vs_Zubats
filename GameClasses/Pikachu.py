import pygame

class Pikachu(pygame.sprite.Sprite):
    imageBackground = (246,246,246)
    x_speed=0
    y_speed=0
    currentImage=0
    pikaScore=0
    level=0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pikas=[]
        for i in range (1,9):
            tempPika = pygame.image.load("Pictures/Pikachu/pik"+str(i)+".png").convert()
            tempPika.set_colorkey(self.imageBackground)
            self.pikas.append(tempPika)
        self.image=self.pikas[5]
        self.rect=self.image.get_rect()

    def changespeed(self,x,y):
        self.x_speed+=x
        self.y_speed+=y

    def selectPicture(self):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        self.currentImage+=1
        if self.currentImage >3*4:
            self.currentImage=0
        #Starts back at the beginning of the image for that direction
        if self.x_speed<0:
            self.image=self.pikas[self.currentImage//4]
        elif self.x_speed>0:
            self.image=self.pikas[self.currentImage//4+4]
