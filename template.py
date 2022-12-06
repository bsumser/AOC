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
    size = 14

    for i in range(0, length - size - 1, 1):
        print(data[i:i+size])
        print(len(set(data[i:i+size])))
        if (len(set(data[i:i+size])) == size):
            print("4 non repeating at %d" % (i+size))
            ans = i+size
            break


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def parse_data():
    #data = get_data(day=20, year=2019)
    #data = [line.strip() for line in data.split("\n")]  # split into list
    #data = [list(line) for line in data]
    #data = [val.split("") for sublist in data for val in sublist]

    my_file = open("maze.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    data = [list(line) for line in data]
    my_file.close()

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

    print(data1[2])
    print(len(data1))

    # ---------------Part 1------------------- #
    ans = part_1(data1)
    # ---------------Part 2------------------- #
    #ans = part_2(data2)

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
