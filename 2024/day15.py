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
    data = open(sys.argv[1], "r").read().split("\n\n")
    
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
