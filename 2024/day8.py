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
    data = [re.findall(r'\d+', line) for line in data]
    data = [line for line in data if line]
    data = [[int(val) for val in line] for line in data]

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
