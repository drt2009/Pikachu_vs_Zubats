import pygame

class Bullet(pygame.sprite.Sprite):
    imageBackground = (246,246,246)
    
    #Holds speed so the bolt always goes the direction it was shot
    speed = 0
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        #Reads in the picture for the bullet
        self.image = pygame.image.load("Pictures/bolt.png")
        self.image.set_colorkey(self.imageBackground)
        self.rect = self.image.get_rect()
