#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    check_set = {}

    for i in range(0, len(data)):
        rectA = Rect(data[i][1], data[i][2], data[i][3] + data[i][1], data[i][4] + data[i][2])
        count = 0
        print(rectA.__dict__)
        for j in range(1, len(data)):
            if (i == j):
                break
            if (j not in check_set):
                check_set.update({j:0})
            if (check_set.get(j) >= 2):
                break
            rectB = Rect(data[j][1], data[j][2], data[j][3] + data[j][1], data[j][4] + data[j][2])
            print(rectB.__dict__)
            # overlapping rectangel algorithm
            overlap = part2_helper(rectA, rectB)
            if (overlap):
                ans += overlap
                check_set.update({j: (check_set.get(j) + 1)})

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part2_helper(rectA, rectB):
    rectA_x_dist = abs(rectA.x1 - rectA.x2)
    rectA_y_dist = abs(rectA.y1 - rectA.y2)
    rectA_area = rectA_x_dist * rectA_y_dist

    rectB_x_dist = abs(rectB.x1 - rectB.x2)
    rectB_y_dist = abs(rectB.y1 - rectB.y2)
    rectB_area = rectB_x_dist * rectB_y_dist

    x_dist = min(rectA.x2, rectB.x2) - max(rectA.x1, rectB.x1)
    y_dist = min(rectA.y2, rectB.y2) - max(rectA.y1, rectB.y1)

    if (x_dist < 0 or y_dist < 0):
        return 0;

    area_overlap = x_dist * y_dist

    return area_overlap

def part_2(data):
    '''Function that takes data and performs part 2'''
    method_start = "part 2 starting----reading %d lines of data\n" % len(data)
    print(method_start)
    start_time = time.time()
    ans = 0


    method_end = "Part 2 done in %s seconds\n" % (time.time() - start_time) + "Part 2 answer is: %d\n" % ans
    print(method_end)
    return method_start + method_end

def parse_data():
    #open file and count lines
    file_name = "./day3.txt"
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
    data = [line.split(" ") for line in data]
    data = ( [list( map(int,i) ) for i in data] )

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
