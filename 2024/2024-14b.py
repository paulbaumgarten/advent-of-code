import math, random, numpy, os, re, copy, time
import pygame
import random
import sys
import time
from pygame.locals import *
BACKGROUND = (0, 0, 0)

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

class Robot:
    def __init__(self, px, py, vx, vy, w, h):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h

    def move(self):
        self.px = (self.px + self.vx) % self.w
        self.py = (self.py + self.vy) % self.h

    def backward(self):
        self.px = (self.px - self.vx) % self.w
        self.py = (self.py - self.vy) % self.h

    def get_quadrant(self):
        vertical_mid = self.h // 2
        horizontal_mid = self.w // 2
        if self.px < horizontal_mid and self.py < vertical_mid:
            return 1
        elif self.px > horizontal_mid and self.py < vertical_mid:
            return 2
        elif self.px < horizontal_mid and self.py > vertical_mid:
            return 3
        elif self.px > horizontal_mid and self.py > vertical_mid:
            return 4
        return 0
    
class Game:
    def __init__(self, robots, dimensions):
        # Game initialisation
        pygame.init()
        self.dimensions = dimensions
        self.robots = robots
        self.screen = pygame.display.set_mode((dimensions[0]*5, dimensions[1]*5))
        self.clock = pygame.time.Clock()
        self.score = 0

    def draw_map(self):
        # Iterate over the map, drawing the walls and food items
        for i, robot in enumerate(self.robots):
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(robot.px*5, robot.py*5, 5, 5))
        
    def run(self):
        # Main loop for game
        game_running = True
        auto = True
        seconds = 0
        prev_seconds = 0
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        seconds -= 1
                    if event.key == pygame.K_RIGHT:
                        seconds += 1
                    if event.key == pygame.K_SPACE:
                        auto = not auto
            self.screen.fill(BACKGROUND)
            self.draw_map()
            if auto:
                seconds += 1
            if seconds > prev_seconds:
                for s in range(prev_seconds, seconds):
                    for i in range(0, len(robots)):
                        robots[i].move()
                prev_seconds = seconds
            elif seconds < prev_seconds:
                for s in range(seconds, prev_seconds):
                    for i in range(0, len(robots)):
                        robots[i].backward()
                prev_seconds = seconds
            print(seconds)
            pygame.display.update()
            self.clock.tick(30)

def load_robots(raw):
    data = raw[:]
    map_size = {"w":101,"h":103}
    robots = []
    for i,this_robot in enumerate(data):
        px,py,vx,vy = this_robot.replace("p=","").replace(" v=",",").split(",")
        px,py,vx,vy = int(px), int(py), int(vx), int(vy)
        print(px,py,vx,vy)
        robots.append( Robot(px,py,vx,vy, map_size["w"], map_size["h"]) )
    return robots, (map_size["w"], map_size["h"])
    
def part2(robots, dimensions):
    game = Game(robots, dimensions)
    game.run() # 7603

if __name__=="__main__":
    start = time.time()
    robots, dimensions = load_robots(get_data())
    result = part2(robots, dimensions)
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


