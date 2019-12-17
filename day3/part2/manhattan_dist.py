from colorama import Fore
import copy
import numpy as np
import sys

class Coord:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Cell:
    def __init__(self, wire1 = False, wire1_length = [], wire2 = False, wire2_length = []):
        self.wire1 = wire1
        self.wire2 = wire2
        self.wire1_length = wire1_length
        self.wire2_length = wire2_length

def get_dist(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)

class Grid:
    grid = [[]]
    origin = Coord(0,0)
    intersections = []
    def __init__(self,x,y,origin):
        self.grid = np.full((x,y),Cell(wire1=False, wire2=False))
        self.origin = origin
    
    def find_closest_intersection_dist(self):
        shortest = len(self.grid)*len(self.grid[0])
        for i,j in self.intersections:
            dist = get_dist(Coord(i,j), self.origin)
            print("lengths",self.grid[i][j].wire1_length,self.grid[i][j].wire2_length)
            if dist < shortest:
                print("intersection dist",dist,self.grid[i][j].wire1_length,self.grid[i][j].wire2_length)
                shortest = dist

        return shortest
    
    def minimize_length(self):
        shortest = sys.maxint
        for i,j in self.intersections:
            length = self.grid[i][j].wire1_length[0] + self.grid[i][j].wire2_length[0]
            if length < shortest:
                shortest = length
        
        return shortest
    
    def print_grid(self, color=Fore.RESET):
        for j in range(len(self.grid[0])):
            line = ""
            for i in range(len(self.grid)):
                if i == self.origin.x and j == self.origin.y:
                    line += Fore.GREEN
                    line += "[%d,%d] " % (self.grid[i][j].wire1, self.grid[i][j].wire2)
                    line += Fore.RESET
                elif self.grid[i][j].wire1:
                    line += Fore.RED
                    line += "[%d,%d] " % (self.grid[i][j].wire1, self.grid[i][j].wire2)
                    line += Fore.RESET
                elif self.grid[i][j].wire2:
                    line += Fore.BLUE
                    line += "[%d,%d] " % (self.grid[i][j].wire1, self.grid[i][j].wire2)
                    line += Fore.RESET
                else:
                    line += "[%d,%d] " % (self.grid[i][j].wire1, self.grid[i][j].wire2)
            print (line)
    
    def put_cell(self, coord, cell, step):
        if cell.wire1:
            self.grid[coord.x][coord.y] = Cell(wire1=True,
                                               wire1_length=self.grid[coord.x][coord.y].wire1_length+[step],
                                               wire2=self.grid[coord.x][coord.y].wire2,
                                               wire2_length=self.grid[coord.x][coord.y].wire2_length)

        if cell.wire2:
            self.grid[coord.x][coord.y] = Cell(wire1=self.grid[coord.x][coord.y].wire1,
                                               wire1_length=self.grid[coord.x][coord.y].wire1_length,
                                               wire2=True,
                                               wire2_length=self.grid[coord.x][coord.y].wire2_length+[step])

        if self.grid[coord.x][coord.y].wire1 and self.grid[coord.x][coord.y].wire2 and coord.x is not self.origin.x and coord.y is not self.origin.y:
            self.intersections.append([coord.x, coord.y])

instructions = []
with open("input.txt",'r') as f:
    temp = f.readlines()
    instructions.append(temp[0].split(','))
    instructions.append(temp[1].split(','))
for i in instructions[0]:
    direction = i[0]
    travel = int(i[1:])

x_total = 0
y_total = 0
x_pos = 0
x_neg = 0
y_pos = 0
y_neg = 0
for line in range(len(instructions)):
    x = 0
    y = 0
    x_pos_tmp = 0
    x_neg_tmp = 0
    y_pos_tmp = 0
    y_neg_tmp = 0
    for i in instructions[line]:
        direction = i[0]
        travel = int(i[1:])
        if direction is "R":
            x += travel
        elif direction is "L":
            x -= travel
        elif direction is "U":
            y -= travel
        elif direction is "D":
            y += travel
        if x > x_pos_tmp:
            x_pos_tmp = x
        if x < x_neg_tmp:
            x_neg_tmp = x
        if y > y_pos_tmp:
            y_pos_tmp = y
        if y < y_neg_tmp:
            y_neg_tmp = y
    x_pos = x_pos_tmp if x_pos_tmp > x_pos else x_pos
    x_neg = x_neg_tmp if x_neg_tmp < x_neg else x_neg
    y_pos = y_pos_tmp if y_pos_tmp > y_pos else y_pos
    y_neg = y_neg_tmp if y_neg_tmp < y_neg else y_neg

x_total = abs(x_neg-x_pos)
y_total = abs(y_neg-y_pos)
g = Grid(x_total+1,y_total+1,Coord(x_total-x_pos,y_total-y_pos))

cur_loc = copy.deepcopy(g.origin)
step = 0
for i in instructions[0]:
    direction = i[0]
    travel = int(i[1:])
    print (direction, travel)
    for i in range(travel):
        cur_loc.x += 1 if direction == "R" else -1 if direction == "L" else 0
        cur_loc.y += 1 if direction == "D" else -1 if direction == "U" else 0
        step += 1
        g.put_cell(cur_loc,Cell(wire1=True),step)

cur_loc = copy.deepcopy(g.origin)
step = 0
for i in instructions[1]:
    direction = i[0]
    travel = int(i[1:])
    print (direction, travel)
    for i in range(travel):
        cur_loc.x += 1 if direction == "R" else -1 if direction == "L" else 0
        cur_loc.y += 1 if direction == "D" else -1 if direction == "U" else 0
        step += 1
        g.put_cell(cur_loc,Cell(wire2=True), step)

print ("closest intersection: %d" % g.find_closest_intersection_dist())
print ("minimized length: %d" % g.minimize_length())