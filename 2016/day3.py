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

    for line in data:
        if (line[0] + line[1] > line[2]) and (line[1] + line[2] > line[0]) and (line[0] + line[2] > line[1]):
            ans += 1


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    for i in range(0, len(data) - 2, 3):
        if (data[i][0] + data[i+1][0] > data[i+2][0]) and (data[i+1][0] + data[i+2][0] > data[i][0]) and (data[i][0] + data[i+2][0] > data[i+1][0]):
            ans += 1
        if (data[i][1] + data[i+1][1] > data[i+2][1]) and (data[i+1][1] + data[i+2][1] > data[i][1]) and (data[i][1] + data[i+2][1] > data[i+1][1]):
            ans += 1
        if (data[i][2] + data[i+1][2] > data[i+2][2]) and (data[i+1][2] + data[i+2][2] > data[i][2]) and (data[i][2] + data[i+2][2] > data[i+1][2]):
            ans += 1


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

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
    data = [line.split() for line in data]
    data = [list(map(int, x)) for x in data]

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
