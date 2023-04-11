from pygame import *

w, h = 700, 500
window = display.set_mode((w, h))
display.set_caption('Игра шутер')

class GameSprite(sprite.Sprite):
    def  __init__(self, imagefile, x, y, w, h, speed):
       super().__init__()
       self.image = transform.scale(image.load(imagefile),(w, h))
       self.speed = speed
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Raketka(GameSprite):
    def update_L(self):
        k = key.get_pressed()
        if k[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k[K_z] and self.rect.y < h -80:
            self.rect.y += self.speed

    def update_R(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y >  0:
            self.rect.y -= self.speed
        if k[K_DOWN] and self.rect.y < h -80:
            self.rect.y += self.speed

raketka_L = Raketka('raketka1.png', 10, 20, 50, 80, 15)
raketka_R = Raketka('raketka2.png', 640, 320, 50, 80, 15)


game  = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((0, 114, 180))

    raketka_L.reset()
    raketka_L.update_L()

    raketka_R.reset()
    raketka_R.update_R()

    display.update()
    time.delay(50)