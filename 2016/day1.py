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

    head = "N"
    headNum = 0
    headings = ["N", "E", "S", "W"]

    x = 0
    y = 0

    s = {(0,0)}

    for i in range(0, len(data) - 1, 2):
        turn = 1 if data[i] == "R" else -1
        move = int(data[i+1])
        headNum += turn

        head = headings[headNum % 4]

        if head == 'N':
            y += move
        elif head == 'E':
            x += move
        elif head == 'S':
            y -= move
        elif head == 'W':
            x -= move
        print("turn %s %d move to move %d blocks %s, %d blocks from start" %
              (data[i], turn, move, head, abs(x) + abs(y)))

    print(x,y)
    ans = abs(x) + abs(y)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    head = "N"
    headNum = 0
    headings = ["N", "E", "S", "W"]

    x = 0
    y = 0

    s = {(0,0)}

    for i in range(0, len(data) - 1, 2):
        turn = 1 if data[i] == "R" else -1
        move = int(data[i+1])
        headNum += turn

        head = headings[headNum % 4]

        # you originally only counted the intersections you turned at into the set,
        # instead of every intersection you passed between turns

        for i in range(0, move):
            if head == 'N':
                y += 1
            elif head == 'E':
                x += 1
            elif head == 'S':
                y -= 1
            elif head == 'W':
                x -= 1
            print("turn %s %d move to move %d blocks %s, %d blocks from start, heading is %c" %
                  (data[i], turn, move, head, abs(x) + abs(y), head))
            if ( (x,y) not in s):
                s.add( (x,y) )
            else:
                break;

    print(x,y)
    ans = abs(x) + abs(y)

    print(s)
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day1.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.strip("\n")
    data = data.replace(" ", "")
    data = data.split(",")
    data = [re.split(r"([A-Z])",line) for line in data]
    data = [val for sublist in data for val in sublist if val]

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
