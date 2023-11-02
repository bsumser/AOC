#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = []
    start_time = time.time()

    numpad = [[1,2,3], [4,5,6], [7,8,9]]

    i = 1
    j = 1

    for line in data:
        for dir in line:
            match dir:
                case "U":
                    if (i - 1 >= 0):
                        i -= 1
                case "D":
                    if (i + 1 <= 2):
                        i += 1
                case "L":
                    if (j - 1 >= 0):
                        j -= 1
                case "R":
                    if (j + 1 <= 2):
                        j += 1
        if (i <= 2 and j <= 2):
            ans.append(numpad[i][j])



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %s\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = []

    numpad = [
        [" ", " ", "1", " ", " "],
        [" ", "2", "3", "4", " "],
        ["5", "6", "7", "8", "9"],
        [" ", "A", "B", "C", " "],
        [" ", " ", "D", " ", " "]
    ]
    
    i = 2
    j = 0

    for line in data:
        for dir in line:
            match dir:
                case "U":
                    if (i-1 >= 0 and numpad[i - 1][j] != " "):
                        i -= 1
                        print(numpad[i][j])
                case "D":
                    if (i+1 <= 4 and numpad[i + 1][j] != " "):
                        i += 1
                        print(numpad[i][j])
                case "L":
                    if (j-1 >= 0 and numpad[i][j - 1] != " "):
                        j -= 1
                        print(numpad[i][j])
                case "R":
                    if (j+1 <= 4 and numpad[i][j + 1] != " "):
                        j += 1
                        print(numpad[i][j])
        if (numpad[i][j] != " "):
            ans.append(numpad[i][j])


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %s\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day2.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    data = [list(line) for line in data]

    print(data)
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


    #pyperclip.copy(ans2)
    return 0
main()
