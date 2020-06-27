import pygame
from math import sqrt
from math import floor
import random
from queue import PriorityQueue
import pygad
from concepts import *
from graphviz import *
import numpy as np
import pandas as pd
import csv
from sklearn.metrics import mean_squared_error, confusion_matrix, accuracy_score, classification_report
from sklearn.tree import DecisionTreeClassifier
from data import *
from choice_tree import *

pygame.init()

# ai settings
S_IDLE = ("kitchen", "middle", "inplace")
S_FIRST = ("order", "food")

IDLE = random.choice(S_IDLE)
FIRST = random.choice(S_FIRST)

HEIGHT = 10
WIDTH = 10

KITCHEN = (1, 1)
MIDDLE = (floor(WIDTH / 2), floor(HEIGHT / 2))

display = pygame.display.set_mode((WIDTH * 32 + 200, HEIGHT * 32))
tileFoil = pygame.image.load('tile.jpg')
waiterAct = pygame.image.load('act1.png')
waiterAct.set_colorkey((255, 255, 255))

# eating time
EAT_TIME = 15

#### Menu
tree = build_tree(training_data)
print_tree(tree)


def client_ordering():
    #generate an order
    order = []

    for i in range(0, len(tree_format)-1):
        tmpr = random.sample(rand_data[i], 1)
        order.append(tmpr[0])

    order.append('order')
    return order
###
class Tile:
    def __init__(self, x, y, canwalk, table, kitchen):
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


class Restaurant:
    def __init__(self, tables, clients):
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
                    new.append(Tile(ih, iw, False, False, False))
                else:
                    new.append(Tile(ih, iw, True, False, False))
            self.tiles.append(new)
        # random walls
        for i in range(3):
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
        self.dir = 1 #1234 NorWesSouEas
        self.path = []
        self.idle = True
        self.orders = []
        self.food = False
        self.ordered_food = []
        self.goal = (0,0)

    def walk(self):
        #'''
        t = self.path.pop(0)
        self.x = t[0]
        self.y = t[1]
        if not self.path:
            self.idle = True

        '''
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
        if not self.path:
            waiter.goal = (random.randint(1, 8), random.randint(1, 8))
        '''

    def BFS(self, goal):
        restaurant.flush()
        queue = [(self.x, self.y)]
        while len(queue) > 0:
            n = queue.pop(0)
            restaurant.tiles[n[1]][n[0]].visited = True
            if n == goal:
                while not n == (self.x, self.y):
                    self.path.insert(0, n)
                    n = restaurant.tiles[n[1]][n[0]].parent
                return
            adj = restaurant.adjacent(n[1], n[0])
            for item in adj:
                x = item.x
                y = item.y
                if restaurant.tiles[y][x].canwalk and not restaurant.tiles[y][x].visited:
                    queue.append((x, y))
                    restaurant.tiles[y][x].parent = n

    def wait(self):
        self.idle = True

    def getTask(self):
        if waiter.orders:
            self.BFS(KITCHEN)
            self.idle = False
            return True
        if FIRST == "order":
            for table in restaurant.tables:
                if restaurant.tiles[table[1]][table[0]].clientState == "order":
                    self.BFS((table[0], table[1]))
                    self.idle = False
                    return True
            if not waiter.food:
                for t in restaurant.kitchen:
                    if not t[2]:
                        waiter.BFS(KITCHEN)
                        self.idle = False
                        return True
        elif FIRST == "food":
            if not waiter.food:
                for t in restaurant.kitchen:
                    if not t[2]:
                        waiter.BFS(KITCHEN)
                        self.idle = False
                        return True
            for table in restaurant.tables:
                if restaurant.tiles[table[1]][table[0]].clientState == "order":
                    self.BFS((table[0], table[1]))
                    self.idle = False
                    return True
        return False


def drawScreen():
    pygame.draw.rect(display, (0, 0, 0), (0, 0, HEIGHT * 32, WIDTH * 32))
    for ih in range(HEIGHT):
        for iw in range(WIDTH):
            tile = restaurant.tiles[ih][iw]
            if tile.canwalk:
                #pygame.draw.rect(display, (128, 128, 128), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                display.blit(tileFoil, (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                if tile.table:
                    if tile.clientState:
                        if tile.clientState == "decide":
                            pygame.draw.rect(display, (0, 128, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "order":
                            pygame.draw.rect(display, (0, 255, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "wait":
                            pygame.draw.rect(display, (255, 128, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                        elif tile.clientState == "eat":
                            pygame.draw.rect(display, (128, 64, 0), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                    else:
                        pygame.draw.rect(display, (64, 64, 64), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                if tile.kitchen:
                    pygame.draw.rect(display, (255, 0, 255), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
                # if tile.visited:
                #   pygame.draw.rect(display, (64,0,64), (iw * 32 + 1, ih * 32+1, 14, 14))
            else:
                pygame.draw.rect(display, (128, 0, 128), (iw * 32 + 1, ih * 32 + 1, 32 - 1, 32 - 1))
    #pygame.draw.circle(display, (255, 255, 255), (waiter.x * 32 + 16, waiter.y * 32 + 16), 16)
    display.blit(waiterAct, (waiter.x * 32 + 8, waiter.y * 32 + 8))

    '''
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
    pygame.draw.circle(display, (255, 0, 0), (waiter.x * 32 + 16 + xx, waiter.y * 32 + 16 + yy), 8)
    '''


    textsurface = font.render(str(restaurant.clients), False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 80, 300))

    pygame.draw.rect(display, (0, 0, 0), (WIDTH * 32 + 80, 332, HEIGHT * 32, WIDTH * 32))
    textsurface = font.render(str(ticks), False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 80, 332))


restaurant = Restaurant(3, 5)
waiter = Agent(2, 2)
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

    textsurface = font.render("klienci:", False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 20, 300))
    textsurface = font.render("czas:", False, (255, 255, 255))
    display.blit(textsurface, (WIDTH * 32 + 20, 332))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4:
                pygame.quit()
            if event.key == pygame.K_F5:
                restaurant = Restaurant(3, 5)
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
                waiter.ordered_food.clear()
                if restaurant.tiles[table[1]][table[0]].client == 0:
                    restaurant.tiles[table[1]][table[0]].clientState = False
                    totaltime = totaltime + ticks
                    restaurant.left = restaurant.left - 1
                    if restaurant.left == 0:

                        restaurant = Restaurant(3, 5)
                        waiter = Agent(2, 2)
                        clientTime = 10
                        ticks = 0
                        totaltime = 0
                        IDLE = random.choice(S_IDLE)
                        FIRST = random.choice(S_FIRST)

    # update waiter
    if waiter.idle:
        if not waiter.getTask():
            if not waiter.path:
                if IDLE == "kitchen":
                    waiter.BFS(KITCHEN)
                elif IDLE == "middle":
                    waiter.BFS(MIDDLE)
                else:
                    waiter.wait()
            else:
                waiter.walk()
    elif waiter.path:
        waiter.walk()
    if not waiter.orders and restaurant.tiles[waiter.y][waiter.x].clientState == "order" and not waiter.path:
        restaurant.tiles[waiter.y][waiter.x].clientState = "wait"
        waiter.orders = (waiter.x, waiter.y)
        waiter.ordered_food.append(client_ordering())
    if (waiter.x, waiter.y) == KITCHEN:
        if waiter.orders:
            restaurant.kitchen.append([waiter.orders[0], waiter.orders[1], 50])
            waiter.orders = False
            for order in waiter.ordered_food:
                print("Passed: %s. Prediction: %s" % (order, print_leaf(classify(order, tree))))
            #waiter.ordered_food.clear()
        elif not waiter.food:
            for t in restaurant.kitchen:
                if not t[2]:
                    waiter.BFS((t[0], t[1]))
                    restaurant.kitchen.remove(t)
                    waiter.food = True
                    waiter.idle = False
                    break
    elif waiter.food and not waiter.path:
        restaurant.tiles[waiter.y][waiter.x].clientState = "eat"
        restaurant.tiles[waiter.y][waiter.x].client = 30
        waiter.food = False

    if ticks > 1500:
        restaurant = Restaurant(3, 5)
        waiter = Agent(2, 2)
        clientTime = 10
        ticks = 0
        totaltime = 0
        IDLE = random.choice(S_IDLE)
        FIRST = random.choice(S_FIRST)

    drawScreen()
    pygame.display.update()
    clock.tick(1500)
    ticks = ticks + 1
