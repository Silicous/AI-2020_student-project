import pygame
from math import sqrt
from math import floor
import random
from queue import PriorityQueue
import pygad
from concepts import *
from graphviz import *
import numpy as np
from data import *
from choice_tree import *

from joblib import load
from customertree import objects

#import tensorflow as tf
#from keras import *
import h5py

pygame.init()
project = 0

WIN = 0
LOSSE = 0
DEFINE = 0
IMG_SIZE = 64
COLOR_CHANNELS = 3

CATEGORIES = [
"apple_pie",
"club_sandwich",
"greek_salad",
"hamburger",
"hot_dog",
"ice_cream",
"lasagna",
"pizza",
"steak",
"waffles"
]

#food_model = load("models/food_model.joblib")
#drink_model = load("models/drink_model.joblib")

#model = tf.keras.models.load_model('final1')

with h5py.File('food_10_64x3_test.hdf5', "r") as f:
    a_group_key = list(f.keys())[0]
    data = list(f[a_group_key])
    # print(len(data))
    data = np.array(data)
    X = np.array(data).reshape(-1, 64, 64, 3)
with open('food_10_64x3_test.txt', 'r') as f:
    y = f.read().split()
    temp = []
    for item in y:
        temp.append(int(item))
# print(len(X))
# print(len(y))
menu = []
for i in range(len(X)):
    menu.append([X[i], y[i]])
random.shuffle(menu)

def image_recognition():
    LOSSE += 1
    for _ in range(100):
        photo = random.choice(menu)
        prediction = model.predict(np.expand_dims(photo[0], axis=0))
        max_value = prediction[0].max()
        idx = np.where(prediction[0]==max_value)
        if CATEGORIES[idx[0][0]] == waiter.order_list[-1]:
            WIN += 1
            break
        waiter.order_list.pop()
    #print(WIN, LOSSE - WIN)

# ai settings
#S_IDLE = ("kitchen", "middle", "inplace")
#S_FIRST = ("order", "food")

IDLE = "inplace"
FIRST = "order"

HEIGHT = 10
WIDTH = 10

KITCHEN = (1, 1)
MIDDLE = (floor(WIDTH / 2), floor(HEIGHT / 2))

display = pygame.display.set_mode((WIDTH * 32 + 200, HEIGHT * 32))
tileFoil = pygame.image.load('tile.jpg')
waiterAct = pygame.image.load('act1.png')
tableEmpty = pygame.image.load('table.png')
tableOrder = pygame.image.load('tableOrder.png')
tableDecide = pygame.image.load('tableDecide.png')
tableWait = pygame.image.load('tableWait.png')
tableEat = pygame.image.load('tableEat.png')
wall = pygame.image.load('wall.png')
# eating time
EAT_TIME = 15

tree = build_tree(training_data)
#order_len = len(tree_format)
#print_tree(tree)


def client_ordering():
    order = []

    for i in range(0, len(tree_format)-1):
        tmpr = random.sample(rand_data[i], 1)
        order.append(tmpr[0])

    order.append('order')
    return order
###


class Client:
    def __init__(self):
        self.gender = random.choice(["Man","Woman"])
        self.outfit = random.choice(["Casual","Elegant"])
        self.cash = random.choice([20,20,20,30,30,50,50,70,80,90,100,100,120,
                                   120,150,200,300,500])
        self.time = random.choice(["Afternoon","Evening"])
        self.vege = random.choice(["No","No","No","No","Yes"])
        self.age = random.randint(12,80)

    def __str__(self):
        return (self.gender + "  Age: " + str(self.age) +"  "+ self.outfit+
                "  $"+ str(self.cash)+ "  Vege: "+ self.vege)

def order_drink(clt):
    frame = []
    if clt.gender == "Man":
        frame.append(0)
    else:
        frame.append(1)
    if clt.age  > 17:
        frame.append(0)
    else:
        frame.append(1)
    if clt.outfit == "Casual":
        frame.append(0)
    else:
        frame.append(1)
    if clt.cash > 100:
        frame.append(0)
    else:
        frame.append(1)
    if clt.time == "Evening":
        frame.append(0)
    else:
        frame.append(1)
    if clt.vege == "No":
        frame.append(0)
    else:
        frame.append(1)

    drink_predict = drink_model.predict([frame])
    drink_index = drink_predict[0]

    return  objects[-1][drink_index]

def order_food(clt):
    frame = []
    if clt.gender == "Man":
        frame.append(0)
    else:
        frame.append(1)
    if clt.age  > 17:
        frame.append(0)
    else:
        frame.append(1)
    if clt.outfit == "Casual":
        frame.append(0)
    else:
        frame.append(1)
    if clt.cash > 100:
        frame.append(0)
    else:
        frame.append(1)
    if clt.time == "Evening":
        frame.append(0)
    else:
        frame.append(1)
    if clt.vege == "No":
        frame.append(0)
    else:
        frame.append(1)

    food_predict = food_model.predict([frame])
    food_index = food_predict[0]

    return objects[-2][food_index]

###
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
    def __eq__(self, other):
        return True
    def __lt__(self, other):
        return True

class Tile:
    def __init__(self, x, y, canwalk, table, kitchen, cost):
        self.x = x
        self.y = y
        self.canwalk = canwalk
        self.table = table
        self.kitchen = kitchen
        self.client = False
        self.clientState = False
        self.visited = False
        self.path = False
        self.parent = (0, 0)
        self.cost = cost


class Restaurant:
    def __init__(self, tables, clients, spots, walls):
        self.h = HEIGHT
        self.w = WIDTH
        self.tiles = []
        self.tables = []
        self.clients = clients
        self.kitchen = []
        self.left = clients
        for ih in range(HEIGHT):
            new = []
            for iw in range(WIDTH):
                if ih == 0 or ih == HEIGHT - 1 or iw == 0 or iw == WIDTH - 1:
                    new.append(Tile(ih, iw, False, False, False, 1))
                else:
                    new.append(Tile(ih, iw, True, False, False, 1))
            self.tiles.append(new)
        # random walls
        for i in range(walls):
            w = random.randint(1, 2)
            h = random.randint(4, HEIGHT - 5)
            for j in range(random.randint(1, 3)):
                ad = self.adjacent(w, h)
                t = random.choice(ad)
                w = t.x
                h = t.y
                self.tiles[w][h].canwalk = False
        # random tables
        i = 0
        while i < tables:
            w = random.randint(2, WIDTH - 3)
            h = random.randint(2, HEIGHT - 3)
            if not self.tiles[h][w].table and self.tiles[h][w].canwalk:
                self.tiles[h][w].table = True
                i = i + 1
                self.tables.append((w, h))
        # random spots
        i = 0
        while i < spots:
            w = random.randint(2, WIDTH - 3)
            h = random.randint(2, HEIGHT - 3)
            self.tiles[h][w].cost = 5
            i = i + 1
        self.tiles[1][1].kitchen = True

    def putClient(self):
        for t in self.tables:
            if not self.tiles[t[1]][t[0]].clientState:
                self.tiles[t[1]][t[0]].client = 30
                self.tiles[t[1]][t[0]].clientState = "decide"
                self.clients = self.clients - 1
                break

    def flush(self):
        for ih in range(HEIGHT):
            for iw in range(WIDTH):
                self.tiles[ih][iw].visited = False
                self.tiles[ih][iw].parent = (0, 0)

    def adjacent(self, x, y):
        tiles = []
        if x == 0 or y == 0 or x == WIDTH or y == HEIGHT:
            tiles.append(self.tiles[y][x])
            return tiles
        tiles.append(self.tiles[y][x - 1])
        tiles.append(self.tiles[y - 1][x])
        tiles.append(self.tiles[y + 1][x])
        tiles.append(self.tiles[y][x + 1])
        return tiles


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 1 #1234 NWSE
        self.path = []
        self.idle = True
        self.orders = []
        self.food = False
        self.goal = (0,0)
        self.order_list = []
        self.order_to_kitchen = []

    def walk(self):
        if self.path:
            t = self.path.pop(0)
            if t[0] == "rotate":
                if t[1] == "right":
                    self.dir = self.dir - 1
                    if self.dir == 0:
                        self.dir = 4
                else:
                    self.dir = self.dir + 1
                    if self.dir == 5:
                        self.dir = 1
            else:
                if self.dir == 1:
                    self.y = self.y - 1
                elif self.dir == 2:
                    self.x = self.x - 1
                elif self.dir == 3:
                    self.y = self.y + 1
                else:
                    self.x = self.x + 1

    def canWalk(self, state):
        x = state[0]
        y = state[1]
        if state[2] == 1:
            y = y - 1
        elif state[2] == 2:
            x = x - 1
        elif state[2] == 3:
            y = y + 1
        elif state[2] == 4:
            x = x + 1
        return restaurant.tiles[y][x].canwalk

    def goaltest(self, state):
        if (state[0] == self.goal[0]) and (state[1] == self.goal[1]):
            return True
        return False

    def succ(self, state):
        s = []

        r = state[2] - 1
        if r == 0:
            r = 4
        s.append((("rotate", "right"), (state[0], state[1], r)))

        l = state[2] + 1
        if l == 5:
            l = 1
        s.append((("rotate", "left"), (state[0], state[1], l)))
        if self.canWalk(state):
            if state[2] == 1:
                w = state[1] - 1
                s.append((("walk"), (state[0], w, state[2])))
            elif state[2] == 2:
                w = state[0] - 1
                s.append((("walk"), (w, state[1], state[2])))
            elif state[2] == 3:
                w = state[1] + 1
                s.append((("walk"), (state[0], w, state[2])))
            elif state[2] == 4:
                w = state[0] + 1
                s.append((("walk"), (w, state[1], state[2])))
        return s

    def f(self, node):
        cost = restaurant.tiles[self.goal[1]][self.goal[0]].cost
        return heuristic((node.state[0], node.state[1]), self.goal) + cost

    def astar(self, goal):
        self.goal = goal
        #stan = (x, y, dir)
        fringe = PriorityQueue()
        explored = []
        start = Node((self.x, self.y, self.dir), False, False)
        fringe.put((1, start))

        while True:
            if fringe.empty():
                return False
            elem = fringe.get()[1]
            if self.goaltest(elem.state):
                self.path = []
                while elem.action is not False:
                    self.path.insert(0, elem.action)
                    elem = elem.parent
                return True
            explored.append(elem.state)
            for (akcja, stan) in self.succ(elem.state):
                x = Node(stan, elem, akcja)
                p = self.f(x)
                if not(stan in fringe.queue) and not(stan in explored):
                    fringe.put((p, x))
                elif (stan in fringe.queue):
                    fringe.queue.remove(elem)
                    fringe.put((p, x))


    def wait(self):
        self.idle = True

    def getTask(self):
        #jesli ktos chce zamowic to do niego idzie
        if not self.orders and not self.food:
            for table in restaurant.tables:
                if restaurant.tiles[table[1]][table[0]].clientState == "order":
                    self.astar((table[0], table[1]))
                    self.idle = False
                    return True
        #jesli trzyma zamowienie to idzie do kuchni
        if self.orders:
            self.astar(KITCHEN)
            self.idle = False
            return True
        #jesli w kuchni jest gotowe danie to po nie idzie
        for t in restaurant.kitchen:
            if t[2] == 0:
                self.astar(KITCHEN)
                self.idle = False
                return True
        #jesli ktos chce jedzenie a kelner je trzyma
        for table in restaurant.tables:
            if restaurant.tiles[table[1]][table[0]].clientState == "wait" and waiter.food:
                self.astar((table[0], table[1]))
                self.idle = False
                return True
        return False

    def endTask(self):
        #jesli sie zatrzymal na stoliku ktory chce zamowic to bierze zamowienie
        if restaurant.tiles[waiter.y][waiter.x].clientState == "order" and not waiter.food and not waiter.orders:
            restaurant.tiles[waiter.y][waiter.x].clientState = "wait"
            waiter.orders = (waiter.x, waiter.y)
        #jesli sie zatrzymal w kuchni z zamowieniem to oddaje zamowienie
        if waiter.x == 1 and waiter.y == 1 and waiter.orders:
            restaurant.kitchen.append([waiter.orders[0], waiter.orders[1], 50])
            waiter.orders = False 
        #jesli sie zatrzymal w kuchni bez zamowienia to bierze jedzenie
        if waiter.x == 1 and waiter.y == 1 and not waiter.orders:
            for t in restaurant.kitchen:
                if t[2] == 0:
                     restaurant.kitchen.remove(t)
                     waiter.food = True
        #jesli sie zatrzymal na stoliku z jedzeniem to je daje
        if restaurant.tiles[waiter.y][waiter.x].clientState == "wait" and waiter.food and not waiter.orders:
            restaurant.tiles[waiter.y][waiter.x].clientState = "eat"
            self.food = False
        self.idle = True

def drawScreen():
    pygame.draw.rect(display, (0, 0, 0), (0, 0, HEIGHT * 32, WIDTH * 32))
    for ih in range(HEIGHT):
        for iw in range(WIDTH):
            tile = restaurant.tiles[ih][iw]
            if tile.canwalk:
                #pygame.draw.rect(display, (128, 128, 128), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                display.blit(tileFoil, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                if tile.cost == 5:
                    pygame.draw.circle(display, (128, 128, 255), (iw * 32 + 17, ih * 32 + 17), 8)
				if tile.table:
                    if tile.clientState:
                        if tile.clientState == "decide":
                            pygame.draw.rect(display, (0, 128, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                            #display.blit(tableDecide, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "order":
                            pygame.draw.rect(display, (0, 255, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                            #display.blit(tableOrder, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "wait":
                            pygame.draw.rect(display, (255, 128, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                            #display.blit(tableWait, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "eat":
                            pygame.draw.rect(display, (128, 64, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                            #display.blit(tableEat, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                    else:
                        pygame.draw.rect(display, (64, 64, 64), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        #display.blit(tableEmpty, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                if tile.kitchen:
                    pygame.draw.rect(display, (255, 0, 255), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                # if tile.visited:
                #   pygame.draw.rect(display, (64,0,64), (iw * 32 + 1, ih * 32+1, 14, 14))
            else:
                pygame.draw.rect(display, (128, 0, 128), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
    pygame.draw.circle(display, (255, 255, 255), (waiter.x * 32 + 16, waiter.y * 32 + 16), 16)
    #display.blit(waiterAct, (waiter.x * 32 + 8, waiter.y * 32 + 8))
    #1234 NWSE
    xx = 0
    yy = 0
    if waiter.dir == 1:
        yy = -16
    elif waiter.dir == 2:
        xx = -16
    elif waiter.dir == 3:
        yy = 16
    elif waiter.dir == 4:
        xx = 16
    pygame.draw.circle(display, (255, 0, 0), (waiter.x * 32 + 16+xx, waiter.y * 32 + 16+yy), 8)

    textsurface = font.render(str(restaurant.clients), False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 80, 300))

    pygame.draw.rect(display, (0, 0, 0), (WIDTH * 32 + 80, 332, HEIGHT * 32, WIDTH * 32))
    textsurface = font.render(str(ticks), False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 80, 332))


restaurant = Restaurant(0, 0, 0, 0)
waiter = Agent(1,1)
clientTime = 10
totaltime = 0
clock = pygame.time.Clock()
ticks = 0


# draw info
help = True
if help:
    font = pygame.font.SysFont('Arial', 18)
    textsurface = font.render("kelner", False, (255, 255, 255))
    pygame.draw.circle(display, (255, 255, 255), (WIDTH * 32 + 26, 16), 16)
    display.blit(textsurface, (WIDTH * 32 + 50, 0))
    textsurface = font.render("sciana", False, (255, 255, 255))
    pygame.draw.rect(display, (128, 0, 128), (WIDTH * 32 + 10, 32, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 32))
    textsurface = font.render("stolik - pusty", False, (255, 255, 255))
    pygame.draw.rect(display, (64, 64, 64), (WIDTH * 32 + 10, 64, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 64))
    textsurface = font.render("stolik - decyduje", False, (255, 255, 255))
    pygame.draw.rect(display, (0, 128, 0), (WIDTH * 32 + 10, 96, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 96))
    textsurface = font.render("stolik - zamawia", False, (255, 255, 255))
    pygame.draw.rect(display, (0, 255, 0), (WIDTH * 32 + 10, 128, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 128))
    textsurface = font.render("stolik - czeka", False, (255, 255, 255))
    pygame.draw.rect(display, (255, 128, 0), (WIDTH * 32 + 10, 160, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 160))
    textsurface = font.render("stolik - je", False, (255, 255, 255))
    pygame.draw.rect(display, (128, 64, 0), (WIDTH * 32 + 10, 192, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 192))
    textsurface = font.render("kuchnia", False, (255, 255, 255))
    pygame.draw.rect(display, (255, 0, 255), (WIDTH * 32 + 10, 224, 32 - 1, 32 - 1))
    display.blit(textsurface, (WIDTH * 32 + 50, 224))
    textsurface = font.render("kaluza", False, (255, 255, 255))
    pygame.draw.circle(display, (128, 128, 255), (WIDTH * 32 + 26, 272), 8)
    display.blit(textsurface, (WIDTH * 32 + 50, 256))

    textsurface = font.render("klienci:", False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 20, 300))
    textsurface = font.render("czas:", False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 20, 332))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                project = 0
            if event.key == pygame.K_1:
                project = 1
            #Execute project
            if event.key == pygame.K_2:
                print("Passed: %s. Prediction: %s" % (client_ordering(), print_leaf(classify(client_ordering(), tree))))
            if event.key == pygame.K_F4:
                pygame.quit()
            if event.key == pygame.K_F5:
                restaurant = Restaurant(3, 3, 10, 3)
                waiter = Agent(2, 2)
                clientTime = 10
                ticks = 0
                totaltime = 0
            if event.key == pygame.K_g:
                t = random.choice(restaurant.tables)
                waiter.BFS(t)
            if event.key == pygame.K_w:
                waiter.walk()

    # update restaurant
    if restaurant.clients > 0:
        clientTime = clientTime - 1
        if clientTime == 0:
            clientTime = 10
            restaurant.putClient()
    for t in restaurant.kitchen:
        if t[2] > 0:
            t[2] = t[2] - 1

    # update tables
    for table in restaurant.tables:
        if restaurant.tiles[table[1]][table[0]].clientState:
            if restaurant.tiles[table[1]][table[0]].clientState == "decide":
                restaurant.tiles[table[1]][table[0]].client = restaurant.tiles[table[1]][table[0]].client - 1
                if restaurant.tiles[table[1]][table[0]].client == 0:
                    restaurant.tiles[table[1]][table[0]].clientState = "order"
            elif restaurant.tiles[table[1]][table[0]].clientState == "eat":
                restaurant.tiles[table[1]][table[0]].client = restaurant.tiles[table[1]][table[0]].client - 1
                waiter.order_to_kitchen.clear()
                if restaurant.tiles[table[1]][table[0]].client == 0:
                    restaurant.tiles[table[1]][table[0]].clientState = False
                    totaltime = totaltime + ticks
                    restaurant.left = restaurant.left - 1
    #update waiter         
    if project == 0:
        if waiter.idle:
            waiter.getTask()
        else:
            waiter.walk()
            if not waiter.path:
                waiter.endTask()

    drawScreen()
    pygame.display.update()
    clock.tick(15)
    ticks = ticks + 1
