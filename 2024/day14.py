#!/usr/bin/env python3
import time
import sys
import re
import math
sys.path.append('../')
sys.set_int_max_str_digits(10000)
sys.setrecursionlimit(3000)
from saoc import coord_check_grid

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0
    tick = 99

    max_x = 101
    max_y = 103
    mid_x = (101-1 / 2)
    mid_y = (103-1 / 2)

    while tick > 0:
        for i in range(0, len(data)):
            line = data[i]
            line[0], line[1] = (line[0] + line[2]) % max_x, (line[1] + line[3]) % max_y
            data[i] = line
            print(f"{line}")
        tick -= 1

    ans += len([line for line in data if line[0] != mid_x and line[1] != mid_y])

    print("silver answer is: %d\n" % ans)
    return ans


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
    data = [re.findall(r'-?\d+', line) for line in data]
    #data = [list(line) for line in data]
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
