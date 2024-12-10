#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
from saoc import coord_check_grid

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
       ans += dfs(-1, coord[0], coord[1], data)
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


def dfs(s, row, col, data):
    #check if out of bounds
    if row < 0 or row > len(data) - 1 or col < 0 or col > len(data[0]) - 1:
        return 0
    else:
        c = data[row][col]
        #print(f"moving from {row},{col} with value {c}")
        if c <= s or abs(c-s) >= 2:
            return 0
        elif c == 9:
            print("9")
            return 1
        else:
            print(f"moving from {row},{col} with value {c}")
            return dfs(c, row-1, col, data) + dfs(c, row+1, col, data) + dfs(c, row, col-1, data) + dfs(c, row, col+1, data)


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
