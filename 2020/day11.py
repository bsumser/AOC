import re
import time
import math
from itertools import groupby
import pyperclip
from aocd import get_data  # module for automating advent of code data get
import aocFunctions

def seat_checker(i,j,data):
    for i_i in range(i-1, i+1, 1):
        for j_j in range(j-1, j+1, 1):
            if (data[i_i][j_j]):
                print("index exists")
            else:
                print("index does not exists")

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    listLength = len(data)
    rowLength = len(data[0])
    ans = 0

    for i in range(1, listLength - 1, 1):
        for j in range(1, rowLength - 1, 1):
            seat_checker(i,j,data)


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

def main():
    input_data = get_data(day=11, year=2020)
    ans = 0
    data = [line.strip() for line in input_data.split("\n")]  # split into list
    #data = [int(val) for sublist in data for val in sublist]
    print(data)
    print(len(data))

    # ---------------Part 1------------------- #
    ans = part_1(data)
    # ---------------Part 2------------------- #
    ans = part_2(data)

    print(ans)
    pyperclip.copy(str(ans))
    return ans
main()
