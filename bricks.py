import pygame

from constants import WHITE


class Brick:
    def __init__(self,x,y,width,height):
        self.rect=pygame.Rect(x,y,width,height)
        self.color=WHITE
        self.active=True

    def draw(self,screen):
        if self.active:
            pygame.draw.rect(screen,self.color,self.rect)
