import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import RED


class Ball:
    def __init__(self):
        self.radius=10
        self.x=SCREEN_WIDTH//2
        self.y=SCREEN_HEIGHT//2
        self.speed_x=5
        self.speed_y=-5

    def move(self):
        self.x+=self.speed_x
        self.y+=self.speed_y

        if self.x<=0 or self.x>=SCREEN_WIDTH:
            self.speed_x=-self.speed_x
        if self.y<=0:
            self.speed_y=-self.speed_y

    def draw(self,screen):
        pygame.draw.circle(screen,RED,(self.x,self.y),self.radius)
