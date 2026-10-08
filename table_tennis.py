from pygame import *

class Saprite(sprite.Sprite):
    def __init__(self,image_,x_hero,y_hero,hero_size_1,hero_size_2,spd_hero):
        super().__init__()
        self.image = transform.scale(image.load(image_),(hero_size_1,hero_size_2))
        self.speed = spd_hero
        self.rect = self.image.get_rect()
        self.rect.x = x_hero
        self.rect.y = y_hero
        self.size = hero_size_1
        self.size = hero_size_2
    def reset(self):
        tab.blit(self.image,(self.rect.x,self.rect.y))
class Player(Saprite):
    def update_arw(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_let(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed

bg = (74,188,255)
tab = display.set_mode((700,500))
tab.fill(bg)
FPS = 60



game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    while finish != True:
        tab.blit(bg,(0,0))

        display.update()
        time.delay(FPS)