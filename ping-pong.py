from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,  player_y, player_x,  player_speed):
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
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed











player = Player('',  100, 100, 3)

window = display.set_mode((700, 500))
display.set_caption('pp')
backgrournd = transform.scale(image.load('фон.jpg'), (800, 500))
game = True
finish = False
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
        player.update()
        player.reset()
        display.update()
        clock.tick(FPS)