import pygame

class Zubat(pygame.sprite.Sprite):
    speed = 0
    currentImage=0
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.zubs=[]

        for i in range (1,9):
            tempZub = pygame.image.load("Pictures/Zubats/zub"+str(i)+".png").convert()
            tempZub.set_colorkey((255,128,0))
            self.zubs.append(tempZub)

        self.image=self.zubs[5]
        self.rect = self.image.get_rect()

    def update(self):
        if self.speed<0:
            self.currentImage+=1
            if self.currentImage >3*4:
                self.currentImage=0
            self.image=self.zubs[self.currentImage//4]
        elif self.speed>0:
            self.currentImage+=1
            if self.currentImage >3*4:
                self.currentImage=0
            self.image=self.zubs[self.currentImage//4+4]


