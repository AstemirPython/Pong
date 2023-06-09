from pygame import *
font.init()
mixer.init()
clock = time.Clock()
run = True
mw = display.set_mode((1000,700))
display.set_caption('Pong')
background = transform.scale(image.load('fon.png'),(1280,720))
mixer.music.load('music.ogg')
mixer.music.play()
sound1 = mixer.Sound('ball_o.ogg')
sound2 = mixer.Sound('game_over.ogg')
font = font.SysFont(None, 50)
class Bal(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed_y,speed_x):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(65,65))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Paddle(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(30,100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 580:
            self.rect.y += self.speed
    def update_H(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 580:
            self.rect.y += self.speed

ball = Bal('ball.png',500,100,7,10)
paddle1 = Paddle('platform.png',10,300,10)
paddle2 = Paddle('platform.png',950,300,10)
a = 1
while run:
    over1 = font.render('Игрок 1 Проиграл!',True,(255,0,0))
    over2 = font.render('Игрок 2 Проиграл!',True,(255,0,0))
    over3 = font.render('Нажмите клавишу"R" чтобы запустить игру заново!',True,(255,0,0))
    o1 = font.render('Игра #:'+ str(a),True,(0,0,0))
    mw.blit(background,(0,0))
 
    ball.rect.x += ball.speed_x
    ball.rect.y += ball.speed_y

    if ball.rect.y <= 0:
        sound1.play()
        ball.speed_y *= -1
    
    if ball.rect.y >= 600:
        sound1.play()
        ball.speed_y *= -1
    
    if sprite.collide_rect(ball,paddle1) or sprite.collide_rect(ball,paddle2):
        sound1.play()
        ball.speed_x *= -1
    
    if ball.rect.x <= 0:
        sound2.play()
        mw.blit(over1,(350,250))
        mw.blit(over3,(90,350))
        
    if ball.rect.x >= 950:
        sound2.play()
        mw.blit(over2,(350,250))
        mw.blit(over3,(90,350))

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                a += 1
                ball.rect.x = 500
                ball.rect.y = 100
    ball.reset()
    paddle1.reset()
    paddle2.reset()
    paddle1.update()
    paddle2.update_H()
    mw.blit(o1,(0,10))
    display.update()
    clock.tick(60)
