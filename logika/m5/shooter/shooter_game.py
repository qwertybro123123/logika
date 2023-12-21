
from pygame import *
from pygame.sprite import Sprite
from pygame.transform import scale, flip
from pygame.image import load
from random import randint

lost = 0
score = 0




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_hight, player_speed):
        super().__init__()
        self.image = scale(load(player_image), (player_width, player_hight))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x <620:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0,620)
            global lost
            lost += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    

win_width = 700
win_height = 500
enemy_skip = 0


window = display.set_mode((win_width,win_height))
background= scale(load("galaxy.jpg"), (win_width, win_height))
ship = Player("rocket.png", 20, win_height-110, 80, 100, 12)

font.init()
font1 = font.SysFont("Arial", 36)

txt_lose = font1.render(f"Lost: {lost}", True, (255,255,255))
txt_score = font1.render(f"Score: {score}", True, (255,255,255))


bullets = sprite.Group()


monsters = sprite.Group()
for i in range(5):
    x = randint(0, win_width-80)
    y = 0
    speed = randint(2,4)
    mon = Enemy("ufo.png", x, y, 80, 50, speed)
    monsters.add(mon)







clock = time.Clock()
FPS = 60
game = True
finish = False

mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.05)
#mixer.music.play(-1)
fire_sound = mixer.Sound("fire.ogg")
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
                fire_sound.play()



    if not finish:
        window.blit(background,(0,0))
        txt_lose = font1.render(f"Lost: {lost}", True, (255,255,255))
        txt_score = font1.render(f"Score: {score}", True, (255,255,255))
        window.blit(txt_lose, (10,50))
        window.blit(txt_score, (10,80))
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        



        
        ship.update()
        monsters.update()
        bullets.update()    







    display.update()
    clock.tick(FPS)