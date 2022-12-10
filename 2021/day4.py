import re
import time
import math
from itertools import groupby
import pyperclip
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions


def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    ans = 0



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
    return sum

def parse_data():
    data = get_data(day=4, year=2021)
    data = data.replace("  ", " ")
    data = data.split("\n\n")
    #data = [line.strip() for line in data.split("\n\n")]  # split into list
    #data = [val.split("\n") for sublist in data for val in sublist]

    #my_file = open("maze.txt", "r")
    #data = my_file.read()
    #data = data.split("\n")
    #data = [list(line) for line in data]
    #my_file.close()

    return data

def list_to_adj_matrix(mazeList):
    width = len(mazeList[2])
    height = len(mazeList) - 6
    wall = "#"
    path = "."

def main():
    ans = 0
    data1 = parse_data()
    nums = data1[0]
    data1.pop(0)
    data1 = [line.split("\n") for line in data1]
    data1 = [val.split(" ") for sublist in data1 for val in sublist]
    data2 = parse_data()

    print(data1)
    print(nums)
    print(len(data1))

    # ---------------Part 1------------------- #
    #ans = part_1(data1)
    # ---------------Part 2------------------- #
    #ans = part_2(data2)

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
