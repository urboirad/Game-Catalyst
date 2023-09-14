import pygame
from sys import exit

version = '0.0.0'

class Game:
    def __init__(self, name, client, source):
        self.name = name
        self.client = client
        self.source = source
        
pygame.init()
pygame.font.init()
title = pygame.display.set_caption('GAME-CATALYST')
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Small Font', 30)

# texts
txt_title = font.render('GAME-CATALYST '+'('+version+')' , False, (255,255,255))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #game code
        screen.blit(txt_title,(10,10))


        pygame.display.update()
        clock.tick(60)