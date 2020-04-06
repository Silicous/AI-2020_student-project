import pygame
import sys
import os
import time
background_image = pygame.image.load("./images/tile.jpg")

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 564
SCREEN_HEIGHT = 564


class Dishes:
    #to do
    x=0
    y=0

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Clients:
    #to do
    x = 0
    y = 0

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Kitchen:
    #to do or delete
    pass


class Order:
    #to do

    x = 0
    y = 0


    def __int__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


def draw():
    screen.blit(background_image, [0, 0])
    screen.blit(player.surf, player.rect)
    player_list.draw(screen)
    pygame.display.flip()

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        super(Player, self).__init__()
        self.index = 0
        self.pkey = ''
        self.surf = pygame.Surface((16, 23))#75, 25
        pygame.sprite.Sprite.__init__(self)
        self.images1 = []
        self.images2 = []
        self.images3 = []
        self.images4 = []
        self.imgList=[]

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','row-4-col-' + str(i) + '.jpg')).convert()
            self.images4.append(img)

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','row-3-col-' + str(i) + '.jpg')).convert()
            self.images3.append(img)

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','row-2-col-' + str(i) + '.jpg')).convert()
            self.images2.append(img)

        for i in range(1,5):
            img = pygame.image.load(os.path.join('images','row-1-col-' + str(i) + '.jpg')).convert()
            self.images1.append(img)
            self.image = self.images1[0]
            self.rect  = self.image.get_rect()

    def onScreen(self):
        if self.rect.left < 0:
            self.rect.left = 27
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH-28
        if self.rect.top <= 0:
            self.rect.top = 27
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT-28

    def step(self, index, newKey):
        self.image = self.imgList[index]
        if newKey == "down":
            self.rect.move_ip(0,7)
        elif newKey == 'up':
            self.rect.move_ip(0, -7)
        elif newKey == 'left':
            self.rect.move_ip(-7, 0)
        elif newKey =='right':
            self.rect.move_ip(7, 0)

    def same(self, newKey, img):
        print(self.pkey, "  ", newKey)
        if self.pkey == newKey:
            self.move(newKey)
        else:
            self.pkey = newKey
            self.index = 0
            self.imgList = img
            self.image = self.imgList[0]

    def move(self, newKey):
        nextFrame = time.clock()
        frame = 0
        i = 0
        while True:
            if time.clock() > nextFrame:
                frame = (frame + 1) % 4
                nextFrame += 0.1
                player.step(frame, newKey)
                draw()
                i += 1
                if i >= 8:
                    self.onScreen()
                    break

    def update(self, pressed_keys):
        newKey = ''
        if pressed_keys[K_DOWN]:
            newKey = 'down'
            self.same(newKey, self.images1)
        elif pressed_keys[K_UP]:
            newKey = 'up'
            self.same(newKey, self.images4)
        elif pressed_keys[K_LEFT]:
            newKey = 'left'
            self.same(newKey, self.images3)
        elif pressed_keys[K_RIGHT]:
            newKey = 'right'
            self.same(newKey, self.images2)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()
player.rect.x = 22
player.rect.y = 22
player_list = pygame.sprite.Group()
player_list.add(player)


running = True
while running:

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    draw()
