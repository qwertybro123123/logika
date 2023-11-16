#створи гру "Лабіринт"!
from pygame import *

from pygame.transform import scale, flip
from pygame.image import load
from random import randint

import pygame

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



win_widht = 700
win_height = 500

window = display.set_mode((win_widht,win_height))
background = scale(load("background.jpg"), (win_widht, win_height))

player = GameSprite("hero.png", 20, win_height-80, 4)
monster = GameSprite("cyborg.png", 600, 350, 2)


clock = time.Clock()
FPS = 60
game = True

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()


while game:
    window.blit(background, (0,0))
    player.reset()
    monster.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    display.update()
    clock.tick(FPS)

