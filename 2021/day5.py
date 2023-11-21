#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    grid = [ [0]*10 for i in range(10)]

    for line in range(0, len(data)):
        x1 = min(data[line][0], data[line][2])
        x2 = max(data[line][0], data[line][2])
        y1 = min(data[line][1], data[line][3])
        y2 = max(data[line][1], data[line][3])

        print("line is: %d,%d to %d,%d" % (x1, y1, x2, y2))
        
        # x coord is the same
        if (x1 == x2):
            for row in range(y1, y2+1):
                grid[row][x1] += 1
            
        # y coord is the same
        elif (y1 == y2):
            for col in range(x1, x2+1):
                grid[y1][col] += 1

    for line in grid:
        print(*line, sep='')
    print("\n\n")

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day5s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    #data = data.replace(" ", "")
    #data = data.split(",")
    data = [line.split(",") for line in data]
    data = ([list(map(int, i) ) for i in data])


    print(data)
    return data


def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()
