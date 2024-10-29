#!/usr/bin/env python3
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque as queue
#import re
#import argparse
#from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    check_list = [ [-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1] ]
    
    #increase all octopus energy by 1
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            data[i][j] += 1
    
    #check for octopi that flash
    que = []
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if (data[i][j] > 9):
                for coord in check_list:
                    i_1 = i + coord[0]
                    j_1 = j + coord[1]
                    if ( 0 <= i_1 <= len(data) - 1 and 0 <= j_1 <= len(data[i]) - 1):
                        print("valid at %d %d" % (i_1, j_1))
                        data[i][j] += 1

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 1
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    check_list = [ [-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1] ]


    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    file_name = "./day11s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    for i in range(0, len(data)):
        data[i] = list(data[i])
        for j in range(0, len(data[i])):
            data[i][j] = int(data[i][j])

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