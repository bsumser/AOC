#!/usr/bin/env python3
import time
import sys
#import re
#import argparse
#from functools import reduce
#import pyperclip
from aocd import get_data  # module for automating advent of code data get
from aocd import submit

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
   
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
   
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    #file_name = "./day.txt"
    #lines = open(file_name, 'r').readlines()
    #num_lines = len(lines)
    #print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    #my_file = open(file_name, "r")
    data = get_data(day=1, year=2019)
    #my_file.close()

    #parse data, array of lines
    data = data.split("\n")
    data = [int(line) for line in data]
    
    # 2d list and convert to ints
    #data = data.split("\n\n")
    #data = [line.split("\n") for line in data]
    #data = [[int(val) for val in line] for line in data]
    
    # examples
    #data = data.replace(" ", "")
    #data = data.split(",")
    #data = [re.split(r"([A-Z])",line) for line in data]
    #data = [val for sublist in data for val in sublist if val]

    print("parsing data for ----reading %d lines of data\n" % len(data))
    print(data[0])
    return data

def submit_check(ans):
    val = input(f"Answer is {ans}, submit? (y/n)\n")

    if (val == 'y' or val == 'Y'):
        submit(ans)
        return 0
    else:
        return 1


def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    submit_check(ans1)
    # ---------------Part 2------------------- #
    #ans2 = part_2(data2)
    #submit_check(ans2)


    #pyperclip.copy(ans2)
    return 0
main()
