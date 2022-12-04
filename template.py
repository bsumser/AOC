import re
import time
import math
from itertools import groupby
import pyperclip
from aocd import get_data  # module for automating advent of code data get
import aocFunctions

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    loop_length = len(data) - 3
    ans = 0
    for i in range(0, loop_length, 4):
        x, y = set(range(data[i],data[i+1] + 1)), set(range(data[i+2],data[i+3] + 1))
        if (x.issubset(y)):
            ans += 1
        elif (y.issubset(x)):
            ans += 1

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    loop_length = len(data) - 3
    ans = 0
    for i in range(0, loop_length, 4):
        x = set(range(data[i],data[i+1] + 1))
        y = set(range(data[i+2],data[i+3] + 1))
        setans = x.intersection(y)
        #print(xs)
        if (len(setans)):
            #print(setans)
            ans += 1
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def main():
    input_data = get_data(day=4, year=2022)
    ans = 0
    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [line.split(",") for line in data]
    data = [val.split("-") for sublist in data for val in sublist]
    data = [int(val) for sublist in data for val in sublist]
    print(data)
    print(len(data))

    # ---------------Part 1------------------- #
    ans = part_1(data)
    # ---------------Part 2------------------- #
    ans = part_2(data)

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
