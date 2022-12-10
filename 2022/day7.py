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
    length = len(data)
    ans = 0



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    length = len(data)
    ans = 0

    lines = map(str.split, open("7.txt").read().splitlines())
    path, dirs = [], defaultdict(int)

    for l in lines:
        if l[0] == "$":
            if l[1] == "cd":
                if l[2] == "..":
                    path.pop()
                else:
                    path.append(l[2])
        elif l[0] != "dir":
            for i in range(len(path)):
                dirs[tuple(path[: i + 1])] += int(l[0])

    print(sum(size for size in dirs.values() if size <= 100000))

    required = 30000000 - (70000000 - dirs[("/",)])

    print(min(size for size in dirs.values() if size >= required))

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return sum

def parse_data():
    data = get_data(day=7, year=2022)
    data = [line.strip() for line in data.split("\n")]  # split into list
    data = [line.split(" ") for line in data]
    #data = [val.split("") for sublist in data for val in sublist]

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
    data2 = parse_data()

    print(data1)
    print(len(data1))

    # ---------------Part 1------------------- #
    ans = part_2(data2)
    # ---------------Part 2------------------- #

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
