#!/usr/bin/env python3
import time
import sys
import re
import math
sys.path.append('../')
from saoc import coord_check_grid
from functools import reduce
import operator
import itertools

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    starts = []
    for row in range(len(data)):
      for col in range(len(data[0])):
        if data[row][col] == 0:
           starts.append([row,col])
        neighbors = coord_check_grid([row,col], len(data), len(data[0]), False)
        print(f"({row},{col}) {data[row][col]} has neighbors {neighbors}")

    for coord in starts:
       paths = []
       cur = 0
       ans += check_path(coord, data, 0)
    print(starts)
    print("silver answer is: %d\n" % ans)
    return ans

def check_path(origin, data, score):
  row = origin[0]
  col = origin[1]
  if data[row][col] == 9:
    score += 1 
    return score
  neighbors = coord_check_grid([row,col], len(data), len(data[0]), False)

  for neighbor in neighbors:
    if data[neighbor[0]][neighbor[1]] - data[row][col] == 1:
      score = check_path([neighbor[0], neighbor[1]], data, score)
  return score


  print(f"({row},{col}) {data[row][col]} has neighbors {neighbors}")

def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0

    starts = []
    for row in range(len(data)):
      for col in range(len(data[0])):
        if data[row][col] == 0:
           starts.append([row,col])
        neighbors = coord_check_grid([row,col], len(data), len(data[0]), False)

    for coord in starts:
       paths = []
       cur = 0
       ans += check_path(coord, data, 0)
    print("Gold answer is: %d\n" % ans)
    return ans

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    
    # ALL numbers to 2d list
    #data = [re.findall(r'\d+', line) for line in data]
    data = [list(line) for line in data if line]
    data = [[int(val) for val in line] for line in data]

    #split on every char 
    #data = list(data)
    #data = [int(val) for val in data]

    print(data)
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
