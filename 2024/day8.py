#!/usr/bin/env python3
import time
import sys
import re
sys.path.append('../')
import saoc
from functools import reduce
import operator
from itertools import product

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def __repr__(self):
        return f"Node(val='{self.val}', children={self.children})"

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    check_dict = {}

    for row in range(len(data)):
        for col in range(len(data[row])):
            cur = data[row][col]
            if cur == '.':
                continue
            elif cur in check_dict:
                check_dict[cur].append( (row,col) )
            else:
                check_dict[cur] = [(row,col)]

    for key,val in check_dict.items():
        print(key, val)

    dist_dict = {}

    for key in check_dict.keys():
        coords = [val for val in check_dict[key]]
        for row in coords:
            first = list(row)
            for col in coords:
                second = list(col)
                print(first, second)
                dist = abs(first[0] - second[0]) + abs(first[1] - second[1])
                if key in dist_dict:
                    dist_dict[key].append(dist)
                else:
                    dist_dict[key] = [dist]

    for key, val in dist_dict.items():
        print(key,val)

    print("Part 1 answer is: %d\n" % ans)
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
    
    # GET ALL THE NUMBERS IN A LINE
    #data = [re.findall(r'\d+', line) for line in data]

    #REMOVE TRAILING EMPTY LISTS
    data = [list(line) for line in data if line]
    #data = [[int(val) for val in line] for line in data]

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
