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

    theDict = {}

    for line in data:
        print(line)
        if line[0] == "$":
            if line[1] == "cd":
                print("change dir")
                theDict.update({'dir':'/'})
            elif line[1] == "ls":
                print("list dir")
        elif line[0] == "dir":
            print("make dir of name %s" % (line[1]))
        elif line[0] == "cd" and line[1] == "..":
            print("go out a dir")
        elif line[0] == "cd" and line[1] == "/":
            print("move to outer dir")
        elif line[0] == "cd":
            print("switch or make dir %s" % (line[1]))
        elif line[0].isnumeric() == True:
            print("make file of size %s" % (line[0]))


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

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
