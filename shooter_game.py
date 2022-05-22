#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size1 = 20
        self.size2 = 20
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
    def fire(self):
        bullet1 = Bullet('bullet.png', self.rect.x, self.rect.y, 7, 10, 10)
        Bullets.add(bullet1)
        
        


lost = 0
lost2 = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= 500:
            self.rect.y += self.speed
        else:
            lost = lost + 1
            lost2 = lost + 1
            self.rect.x = randint(0, 600)
            self.rect.y = 0
            
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y == 0:
            self.kill()





monsters = sprite.Group()
cyborg1 = Enemy('ufo.png', 200, 0, 3, 65, 65)
cyborg2 = Enemy('ufo.png', 200, 0, 3, 65, 65)
cyborg3 = Enemy('ufo.png', 200, 0, 3, 65, 65)
cyborg4 = Enemy('ufo.png', 200, 0, 3, 65, 65)
cyborg5 = Enemy('ufo.png', 200, 0, 3, 65, 65)
asteroid = sprite.Group()
ast1 = Enemy('asteroid.png', 200, 0, 3, 50, 50)
ast2 = Enemy('asteroid.png', 200, 0, 3, 50, 50)
ast3 = Enemy('asteroid.png', 200, 0, 3, 50, 50)
monsters.add(cyborg1)
monsters.add(cyborg2)
monsters.add(cyborg3)
monsters.add(cyborg4)
monsters.add(cyborg5)
monsters.add(ast1)
monsters.add(ast2)
monsters.add(ast3)
Bullets = sprite.Group()


player = Player('rocket.png', 100, 420, 7, 65, 0)
enemy = Enemy('ufo.png', 200, 0, 4, 65, 65)
enemy2 = Enemy('asteroid.png', 200, 0, 4, 50, 50)
font.init()
font1 = font.SysFont(('Arial'), 36)
win = font1.render('U WiN!!!!!!!!!!', True, (5, 229, 245))
lose2= font1.render(' YOU LOSE', 1, (255, 0, 0))

window = display.set_mode((700, 500))
display.set_caption('shooter')
backgrournd = transform.scale(image.load('galaxy.jpg'), (800, 500))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


win = 0
lost = 0
#str(lost2)

finish = False
game = True
clock = time.Clock()
FPS = 60
clock.tick(FPS)
while game :
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if finish != True:
        window.blit(backgrournd, (0, 0))
        lose = font1.render('Пропущено врагов:' + str(lost), True, (102, 0, 204, 36))
        lost2 = font1.render('Побеждено вргов:' , True, (0, 204, 0, 36))
        window.blit(lose, (10, 10))
        window.blit(lost2, (400, 10))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        monsters.draw(window)
        monsters.update()
        Bullets.update()
        Bullets.draw(window)
        if sprite.spritecollide(player, monsters, False):
            finish = True
            window.blit(lose2,(290, 250))
        if win == 10:
            window.blit(win,(0,0))
            finish = True
        if sprite.groupcollide(monsters, Bullets, True, True):
            win = win + 1
            monster = Enemy('ufo.png', randint(80, 400), -40, 2, 50, randint(80, 50))
            monsters.add(monster)
        display.update()
        clock.tick(FPS)
    
           
