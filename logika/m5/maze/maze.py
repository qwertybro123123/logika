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

class Wall(sprite.Sprite):
    def __init__(self, wall_x, wall_y, wall_widht, wall_height):
        super().__init__()
        self.width = wall_widht
        self.height = wall_height

        self.image = Surface((self.width, self.height))


        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

        self.image.fill((0,200,0))
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


win_widht = 700
win_height = 500

window = display.set_mode((win_widht,win_height))
background = scale(load("background.png"), (win_widht, win_height))

player = Player("player.jpg", 20, win_height-80, 4)
monster = Enemy("enemy.jpg", 600, 350, 2)
treasure = GameSprite("treasure.png", win_widht-80, win_height-80, 0)
wall1 = Wall(100,100,20,400)
wall2 = Wall(100,80,300,20)
wall3 = Wall(400,80,20,600)
wall4 = Wall(400,300,150,20)
wall5 = Wall(550,200,150,20)
walls = [wall1,wall2,wall3,wall4,wall5]

clock = time.Clock()
FPS = 120
game = True
finish = False

font.init()
f =font.Font(None, 70)
win = f.render("You win!", True, (255,215,0))
lose = f.render("You lose!", True, (255,0,0))

mixer.init()
mixer.music.load("jungles.mp3")
mixer.music.play()
money = mixer.Sound("money.mp3")
kick = mixer.Sound("kick.mp3")



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
        for wall in walls:
            wall.reset()


        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            mixer.music.stop()
            money.play()
        for wall in walls:
            if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall):
                finish = True
                window.blit(lose, (200, 200))
                mixer.music.stop()
                kick.play()
            

            

    display.update()
    clock.tick(FPS)

