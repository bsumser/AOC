#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/
#
#started at 1698354885
#finished at

def part_1(data):
    '''Function that takes data and performs part 1'''
    #print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    x = 0
    y = 0
    cur = 1
    inc = 0

    f_right = 1
    up = 1
    left = 2
    down = 2
    right = 2

    move_list = [1, 1, 2, 2, 2]

    while (cur <= 325489):
        cur += f_right
        x += f_right

        cur += up + inc
        y += up + inc

        cur += left + inc
        x -= left + inc

        cur += down + inc
        y -= down + inc

        cur += right + inc
        x += right + inc

        inc += 2
    print(cur, x, y)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    #print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    #file_name = "./day3.txt"
    #lines = open(file_name, 'r').readlines()
    #num_lines = len(lines)
    #print("parsing data for ----reading %d lines of data\n" % num_lines)

    ##open file and read in data
    #my_file = open(file_name, "r")
    #data = my_file.read()
    #my_file.close()

    #parse data
    data = 325489


    #print(data)
    return data


def main():
    #track time taken to get working
    part1start = 1698356551
    part2start = 0
    part2finish = 0
    star1 = (part2start - part1start) / 60
    star2 = (part2finish - part2start) / 60

    ans1 = 0
    ans2 = 0

    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    print("current timestamp is %d\n" % time.time())
    print("part 1 finished in %d mins\n" % (star1))
    print("part 2 finished in %d mins\n" % (star2))
    return 0
main()
