#створи гру "Лабіринт"!
from typing import Any
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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_height-70:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x <620:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed

        if self.direction == "right":
            self.rect.x += self.speed


        if self.rect.x <= 450:
            self.direction = "right"
        if self.rect.x >= win_widht-70:
            self.direction = "left"

win_widht = 700
win_height = 500

window = display.set_mode((win_widht,win_height))
background = scale(load("background.jpg"), (win_widht, win_height))

player = Player("hero.png", 20, win_height-80, 4)
monster = Enemy("cyborg.png", 600, 350, 2)
treasure = GameSprite("treasure.png", win_widht-80, win_height-80, 0)

clock = time.Clock()
FPS = 120
game = True
finish = False
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        treasure.reset()

            

    display.update()
    clock.tick(FPS)

