from pygame import *
FPS = 120
SPEED = 10


window = display.set_mode((700, 500))
background = transform.scale(
    image.load("background.png"),(700,500)
)

clock = time.Clock()


sprite1 = transform.scale(image.load("sprite1.png"),(100,100))
x1 = 100
y1 = 400

sprite2 = transform.scale(image.load("sprite2.png"),(100,100))
x2 = 500
y2 = 400

game = True

while game:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))
    
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_LEFT] and x2 > 0:
        x2-=SPEED
    if keys_pressed[K_RIGHT] and x2 < 600:
        x2+=SPEED
    if keys_pressed[K_UP] and y2 > 0:
        y2-=SPEED
    if keys_pressed[K_DOWN] and y2 < 400:
        y2+=SPEED

    if keys_pressed[K_a] and x1 > 0:
        x1-=SPEED
    if keys_pressed[K_d] and x1 < 600:
        x1+=SPEED
    if keys_pressed[K_w] and y1 > 0:
        y1-=SPEED
    if keys_pressed[K_s] and y1 < 400:
        y1+=SPEED

    display.update()
    clock.tick(FPS)