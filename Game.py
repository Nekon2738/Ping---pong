from pygame import *
from random import *
window = display.set_mode((700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, scale_x, scale_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (scale_x, scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.scale_x = scale_x
        self.scale_y = scale_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Area:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Lpl(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 320:
            self.rect.y += self.speed
     

class Rpl(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > -10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 320:
            self.rect.y += self.speed
     

class Picture(Area):
    def __init__(self, x, y, width, height, filename):
        super().__init__(x, y, width, height)
        self.image = transform.scale(image.load(filename), (width, height))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

        


win_width = 700
win_height = 500


player_speed = 25




window = display.set_mode((win_width, win_height))
display.set_caption('Ping - pong')
background = transform.scale(image.load('background.jpg'), (700, 500))

LPlat = Lpl('plat.png',630, 180, 8, 80, 120)
RPlat = Rpl('plat2.png',-10, 180, 8, 80, 120)
PlasmaBall = Picture(310, 220, 58, 50, 'PLBall.png')




game = True
finish = False
clock = time.Clock()
FPS = 120

speed_x = randint(-4, 4)
speed_y = randint(-4, 4)

mixer.init()
mixer.music.load('AriaMath.ogg')
mixer.music.play(-1)
sm = mixer.Sound('smash.ogg')
cl = mixer.Sound('collide.ogg')
end = mixer.Sound('End.ogg')
font.init()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    #Выход на Escape
    keys = key.get_pressed()
    if keys[K_ESCAPE]:
        game = False
        
    if finish != True:
        window.blit(background, (0, 0))
        PlasmaBall.rect.x += speed_x 
        PlasmaBall.rect.y += speed_y 
        if PlasmaBall.rect.x < RPlat.rect.x - 52:
            font1 = font.SysFont('verdana', 40)
            text = font1.render('Game Over\n\nLeft player lose', True, (255, 0, 0))
            window.blit(text, (45, 200))
            mixer.music.stop()
            end.play()
            speed_x, speed_y = 0, 0
            finish = True
            #game = False
        if PlasmaBall.rect.x > LPlat.rect.x + 67:
            font1 = font.SysFont('verdana', 40)
            text = font1.render('Game Over\n\nRight player lose', True, (0, 0, 255))
            window.blit(text, (28, 200))
            mixer.music.stop()
            end.play()
            speed_x, speed_y = 0, 0
            finish = True
        #if PlasmaBall.rect.x > 650 or PlasmaBall.rect.x < 0:
            #speed_x *= -1
            #cl.play()
        if PlasmaBall.rect.y <= 10:
            speed_y *= -1
            cl.play()
        if PlasmaBall.colliderect(LPlat.rect):
            speed_x = - speed_x
            sm.play()
        if PlasmaBall.rect.y >= 450:
            speed_y *= -1
            cl.play()
        if PlasmaBall.colliderect(RPlat.rect):
            speed_x = - speed_x
            sm.play()


        LPlat.update()
        RPlat.update()
        LPlat.reset()
        RPlat.reset()
        PlasmaBall.reset()
        display.update()
        clock.tick(FPS)
    
    
    




