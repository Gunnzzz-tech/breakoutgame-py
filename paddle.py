from config import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import BLUE
import pygame

class Paddle:
    def __init__(self):
        self.width=100
        self.height=20
        self.x=(SCREEN_WIDTH-self.width)//2
        self.y=(SCREEN_HEIGHT-30)
        self.speed=10

    def move(self,keys):
        if keys[pygame.K_LEFT] and self.x>0:
            self.x-=self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self,screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))