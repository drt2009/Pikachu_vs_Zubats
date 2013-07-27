import pygame
from GameNew import Game

pygame.init()
pygame.display.set_caption("Pikachu vs. Zubats")

pygame.mixer.init()
pygame.mixer.music.load("Music/music.mp3")
pygame.mixer.music.play(-1,0.5)
Game()
pygame.quit()
