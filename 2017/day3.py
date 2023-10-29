#!/usr/bin/env python3
import time
import re
import argparse
import math
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    #print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    (x,y,cur) = part1_helper(325489)

    print(x,y,cur)

    ans = ( abs(x-0) + abs(y-0))


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part1_helper(num):
    x = 0
    y = 0
    cur = 1
    inc = 0

    move_list = [1, 1, 2, 2, 2]
    dir_list = ["x+", "y+", "x-", "y-", "x++"]

    while (cur <= num):
        for i in range (0, len(move_list)):
            print(move_list[i], dir_list[i])
            match dir_list[i]:
                case "x+":
                    for j in range (0, move_list[i]):
                        cur += 1
                        x += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "y+":
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        y += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "x-":
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        x -= 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "y-":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        y -= 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "x++":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        x += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
            print("\t%d" % (cur))
            if (i == len(move_list) - 1):
                i = 0
                inc += 2
    return (x,y,cur)

def part_2(data):
    '''Function that takes data and performs part 2'''
    #print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    x_i = 200
    y_i = 200

    buckets = [[0 for col in range(400)] for row in range(400)]
    print(buckets)

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def part2_helper(num):
    x = 0
    y = 0
    cur = 1
    inc = 0

    move_list = [1, 1, 2, 2, 2]
    dir_list = ["x+", "y+", "x-", "y-", "x++"]

    while (cur <= num):
        for i in range (0, len(move_list)):
            print(move_list[i], dir_list[i])
            match dir_list[i]:
                case "x+":
                    for j in range (0, move_list[i]):
                        cur += 1
                        x += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "y+":
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        y += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "x-":
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        x -= 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "y-":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        y -= 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
                case "x++":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        cur += 1
                        x += 1
                        print("\t i=%d %d,%d" % (i,x,y))
                        if (cur == num):
                            return (x,y,cur)
            print("\t%d" % (cur))
            if (i == len(move_list) - 1):
                i = 0
                inc += 2
    return (x,y,cur)

def part2_idx_check(x, y, buckets):
    neighbors = (-1, 0), (1, 0), (0, -1), (0, 1)
    for near in neighbors:
        buckets[x][y] += buckets[x+near[0]][y+near[11]]


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
