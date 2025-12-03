#!/usr/bin/env python3
import time
import sys
import re
import math
from collections import deque
from saoc import coord_check_grid
sys.path.append('../')
sys.setrecursionlimit(10000)
from saoc import coord_check_grid

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    start = [0,0]
    end = [0,0]

    for row in range(0, len(data)):
        for col in range(0, len(data[0])):
            if data[row][col] == 'S':
                start = [row, col]
            elif data[row][col] == 'E':
                end = [row, col]
    print(path_recur(data, set(), start[0], start[1], sys.maxsize, 0, 1, 0, 0))

    print(f"start {start}")
    print(f"end {end}")


    print("silver answer is: %d\n" % ans)
    return ans

def path_recur(data, visited, row, col, min_dist, dist, dir, turned, steps):
    dirs = ['N', 'E', 'S', 'W']  # Direction indices: 0=N, 1=E, 2=S, 3=W
    
    if data[row][col] == 'E':  # Found the end
        print(f"Found destination in {steps} steps with {turned} turns.")
        return min(min_dist, dist)
    
    visited.add((row, col))
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W offsets
    for new_dir, (dr, dc) in enumerate(deltas):
        new_row, new_col = row + dr, col + dc
        if check_safe(data, visited, new_row, new_col):
            # Calculate turn cost
            turns = abs(new_dir - dir) % 4
            if turns > 2:  # Handle wraparound for modular arithmetic
                turns = 4 - turns
            offset = 0 if turns == 0 else 1000 * turns
            
            # Recurse
            min_dist = path_recur(data, visited, new_row, new_col, 
                                  min_dist, dist + offset + 1, 
                                  new_dir, turned + turns, steps + 1)
    
    visited.remove((row, col))  # Backtrack
    return min_dist

def check_safe(data, visited, row, col):
    #print(row >= 0 and row < len(data) and col >= 0 and col < len(data[0]) and (data[row][col] == '.' or data[row][col] == 'E')  and ( (row, col) not in visited))
    return (row >= 0 and row < len(data) and col >= 0 and col < len(data[0]) and (data[row][col] == '.' or data[row][col] == 'E') and ( (row, col) not in visited))


def bfs(data, vis, row, col):
    q = deque()

    q.append( (row, col) )
    vis.add( (row,col) )

    if data[row][col] == 'E':
        print("found")
        return 0
    
    else:
        while len(q) > 0:
            cell = q.popleft()
            print_grid(data, vis)
            row = cell[0]
            col = cell[1]
            
            if data[row][col] == 'E':
                print("found")
                return 0

            neighbors = coord_check_grid((row, col), len(data) - 1, len(data[0]) - 1, False)
            neighbors = [spot for spot in neighbors if data[spot[0]][spot[1]] is not '#' and tuple(spot) not in vis]
            print(f"({row, col}) has neighbors: {neighbors}")

            for val in neighbors:
                q.append(val)
                vis.add(tuple(val))
    return 1

def print_grid(data, vis):
    for row in range(0, len(data)):
        for col in range(0, len(data[0])):
            if (row, col) in vis:
                print(f"{bcolors.OKGREEN}{data[row][col]}{bcolors.ENDC}", end="")
            else:
                print(f"{bcolors.FAIL}{data[row][col]}{bcolors.ENDC}", end="")
        print(f"\n", end="") 


def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0
    

    
    print("Gold answer is: %d\n" % ans)
    return ans


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    
    # ALL numbers to 2d list
    #data = [line.split("\n") for line in data]
    #data = [re.findall(r'-?\d+', line) for line in data]
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    #split on every char 
    #data = list(data)
    #data = [int(val) for val in data]

    for line in data:
        print(line)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    silver(parse_data())
    # ---------------Part 2------------------- #
    gold(parse_data())

    return 0

if __name__ == "__main__":
    main()
