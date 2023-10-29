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

    num = 325489

    (x,y,ans) = part2_helper(num)

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def part2_helper(num):
    x = 1000
    y = 1000
    cur = 1
    inc = 0

    size = 2000
    
    buckets = [[0 for col in range(size)] for row in range(size)]
    buckets[1000][1000] = 1
    print(buckets)

    move_list = [1, 1, 2, 2, 2]
    dir_list = ["x+", "y+", "x-", "y-", "x++"]
    neighbors = (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)

    while (num >= cur):
        for i in range (0, len(move_list)):
            #print(move_list[i], dir_list[i])
            match dir_list[i]:
                case "x+":
                    for j in range (0, move_list[i]):
                        x += 1
                        for near in neighbors:
                            buckets[x][y] += buckets[x+near[0]][y+near[1]]
                        cur = buckets[x][y]
                        print("\t cur=%d %d,%d" % (cur,x,y))
                        if (cur > num):
                            return (x,y,cur)
                case "y+":
                    for j in range (0, move_list[i] + inc):
                        y += 1
                        for near in neighbors:
                            buckets[x][y] += buckets[x+near[0]][y+near[1]]
                        cur = buckets[x][y]
                        print("\t cur=%d %d,%d" % (cur,x,y))
                        if (cur > num):
                            return (x,y,cur)
                case "x-":
                    for j in range (0, move_list[i] + inc):
                        x -= 1
                        for near in neighbors:
                            buckets[x][y] += buckets[x+near[0]][y+near[1]]
                        cur = buckets[x][y]
                        print("\t cur=%d %d,%d" % (cur,x,y))
                        if (cur > num):
                            return (x,y,cur)
                case "y-":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        y -= 1
                        for near in neighbors:
                            buckets[x][y] += buckets[x+near[0]][y+near[1]]
                        cur = buckets[x][y]
                        print("\t cur=%d %d,%d" % (cur,x,y))
                        if (cur > num):
                            return (x,y,cur)
                case "x++":
                    print("check = %d" % (move_list[i] + inc))
                    for j in range (0, move_list[i] + inc):
                        x += 1
                        for near in neighbors:
                            buckets[x][y] += buckets[x+near[0]][y+near[1]]
                        cur = buckets[x][y]
                        print("\t cur=%d %d,%d" % (cur,x,y))
                        if (cur > num):
                            return (x,y,cur)
            print("\t%d" % (cur))
            if (i == len(move_list) - 1):
                i = 0
                inc += 2
    print(buckets)
    return (x,y,cur)

def part2_idx_check(x, y, buckets):
    neighbors = (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)
    for near in neighbors:
        buckets[x][y] += buckets[x+near[0]][y+near[1]]

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

    ans1 = 0
    ans2 = 0

    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    return 0
main()
