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
    dataLength = len(data)
    for line in data:
        for i in range(1, int(line[1])):
            print("test")

    ans = 0

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    dataLength = len(data)
    for line in data:
        print(line)
    ans = 0


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def main():
    input_data = get_data(day=5, year=2022)
    ans = 0
    data = [line.strip() for line in input_data.split("\n\n")]  # split into list
    del data[0]
    data = [line.split("\n") for line in data]
    data = [val.split(" ") for sublist in data for val in sublist]
    #data = [int(val) for sublist in data for val in sublist]
    crates = [["T", "Z", "B"]
    ,["N", "D", "T", "H", "V"]
    ,["D", "M", "F", "B"]
    ,["L", "Q", "V", "W", "G", "J", "T"]
    ,["M", "Q", "F", "V", "P", "G", "D", "M"]
    ,["S", "F", "H", "G", "Q", "Z", "V"]
    ,["W", "C", "T", "L", "R", "N", "S", "Z"]
    ,["M", "R", "N", "J", "D", "W", "H", "Z"]
    ,["S", "D", "F", "L", "Q", "M"]]

    print(data)
    print(crates[0])
    print(len(data))

    # ---------------Part 1------------------- #
    for line in data:
        for i in range(1, int(line[1])):
            crates[line[5]].insert(crates[line[3]]) # append to list
            crates[line[3]] # remove from list
    # ---------------Part 2------------------- #
    #ans = part_2(data)

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
