#!/usr/bin/env python3
import time
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get
#import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    print(data)
    start_time = time.time()

    start = (0, 0)

    Dict = {}

    for direct in data:
        start = list(start)
        if direct == '^':
            start[1] += 1
        elif direct == 'v':
            start[1] -= 1
        elif direct == '<':
            start[0] -= 1
        elif direct == '>':
            start[0] += 1

        start = tuple(start)

        if start in Dict.keys():
            Dict[start] += 1
            print("%s hit again value is %d" % start, Dict[start])
        else:
            Dict[start] = 1

    ans = list(filter(lambda x: x >= 1, list(Dict.values())))
    ans = len(ans)
    print(ans)

    #print("Part 1 done in %s seconds" % (time.time() - start_time))
    #print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def parse_data():
    my_file = open("./day3.txt", "r")
    data = my_file.read()
    my_file.close()
    data = data.strip("\n")
    data = [x for x in data]
    #data = [x.split("x") for x in data]
    #data = [int(num) for row in data for num in row]


    #print(data)
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


    print(ans1)
    print(ans2)
    #pyperclip.copy(ans2)
    return 0
main()
