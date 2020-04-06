ALPHA = (0, 255, 0)

# Import the pygame module
import pygame
import sys
import os # new code below
background_image = pygame.image.load("images/tile.jpg")
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 564
SCREEN_HEIGHT = 564

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((56, 56))#75, 25
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()


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













    # Move the sprite based on user keypresses
    #60
    def update(self, pressed_keys):
        #when the update method is called, we will increment the index


        #finally we will update the image that will be displayed
    #    self.image = self.images[self.index]
        nkey = ''
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 56)
            nkey = 'up'
            if self.pkey == nkey:
                self.index += 1
                if self.index >= 4:
                    self.index = 0

            else:
                self.pkey = nkey
                self.index = 0
            self.image = self.images1[self.index]

        elif pressed_keys[K_UP]:
            self.rect.move_ip(0, -56)
            nkey = 'down'
            if self.pkey == nkey:
                self.index += 1
                if self.index >= 4:
                    self.index = 0
            else:
                self.pkey = nkey
                self.index = 0
            self.image = self.images4[self.index]

        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-56, 0)
            nkey = 'left'
            if self.pkey == nkey:
                self.image = self.images3[self.index]
                self.index += 1
                if self.index >= 4:
                    self.index = 0
            else:
                self.pkey = nkey
                self.index = 0

        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(56, 0)
            nkey = 'right'
            if self.pkey == nkey:
                self.image = self.images2[self.index]
                self.index += 1
                if self.index >= 4:
                    self.index = 0
            else:
                self.pkey = nkey
                self.index = 0

        else:
            return False
        #
        # if self.index >= len(self.images):
        #     self.index = 0
        #     if self.pkey == nkey:
        #         self.image = self.images[self.index]
        #         self.index += 1
        #     else:
        #         self.pkey = nkey


       # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


        #if the index is larger than the total images

        return True

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()
player.rect.x = 25   # go to x
player.rect.y = 25   # go to y




player_list = pygame.sprite.Group()
player_list.add(player)



# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # guard = False
    # while guard is False:
        # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
    guard = player.update(pressed_keys)

    # Fill the screen with black
    screen.blit(background_image, [0, 0])
    #screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, player.rect)
    player_list.draw(screen) # draw player
    # Update the display
    pygame.display.flip()
    clock.tick(30)
