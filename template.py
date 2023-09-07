import re
import time
import math
import pyperclip
import numpy as np
from aocd import get_data  # module for automating advent of code data get
import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    ans = 0
    print(data)
    print(len(data))
    start_time = time.time()

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
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
    #data = get_data(day=11, year=2022)
    my_file = open("./2022/day14sample.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    my_file.close()

    print(data)
    return data


def main():
    ans = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    print(ans2)
    pyperclip.copy(ans2)
    return 0
main()
