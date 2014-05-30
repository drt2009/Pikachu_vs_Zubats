'''
Created on May 29, 2014

@author: Don
'''

import pygame

class Background(pygame.sprite.Sprite):
    imageBackground = (246,246,246)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Pictures/moon.jpg")
        self.image.set_colorkey(self.imageBackground)
        self.rect = self.image.get_rect()
