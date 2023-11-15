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

    fabric = [ [0]*1000 for i in range(1000)]

    for num in range(0, len(data)):
        row_start = data[num][2]
        row_end = row_start + data[num][4]
        col_start = data[num][1]
        col_end = col_start + data[num][3]
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                fabric[i][j] += 1
    ans = sum(x > 1 for line in fabric for x in line)

    for line in fabric:
        print(*line, sep='')
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans


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
