'''
Created on May 29, 2014

@author: Don
'''
import pygame
from Game import Game

pygame.mixer.init()
pygame.mixer.music.load("Music/music.mp3")
pygame.mixer.music.play(-1,0.5)
Game()