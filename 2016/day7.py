#!/usr/bin/env python3
import time
#import re
#import argparse
#from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

OKGREEN = '\033[92m'

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()
    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    passes = []
    for i in range(0, len(data)):
        open_bracket = []
        close_bracket = []
        check = True
        for j in range(0, len(data[i])):
            if (data[i][j] == '['):
                open_bracket.append(j)
            if (data[i][j] == ']'):
                close_bracket.append(j)
        for j in range(0, len(data[i])-3):
            if (data[i][j] == data[i][j+3] and data[i][j+1] == data[i][j+2] and data[i][j] != data[i][j+1]):
                for b in range(0, len(open_bracket)):
                    if (j > open_bracket[b] and j+3 < close_bracket[b]):
                        check = False
        if (check):
            passes.append(data[i])
    print(len(passes))
    double_pass = []
    for i in range(0, len(passes)):
        for j in range(0, len(passes[i])-3):
            if (passes[i][j] == passes[i][j+3] and passes[i][j+1] == passes[i][j+2]):
                if (passes[i][j] != passes[i][j+1]):
                    print(passes[i][0:j] + '\x1b[6;30;42m' + passes[i][j:j+4] + '\033[0m' + passes[i][j+4:])
                    double_pass.append(passes[i])

    ans = len(double_pass)

    assert ans < 151 

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
    file_name = "./day7.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")

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