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
    ans = 0
    start_time = time.time()

    # list to store memory banks and og index
    banks = []

    # store permutations of memory banks
    perms = set()

    for i in range(0, len(data)):
        cur = [i, data[i]]
        banks.append(cur)
    print(banks)

    done = False
    while(not done):
        cur = list(max(banks, key=lambda x: (x[1], -x[0])))
        #print(cur)
        banks[cur[0]] = [cur[0], 0]
        #print(banks[cur[0]])
        i = (cur[0] + 1)
        if (i >= len(banks)):
            i = (i % len(banks)) - 1 
        while(cur[1]):
            banks[i][1] += 1
            cur[1] -= 1
            print("added 1 block to bank %s cur = %s" % (banks[i], cur))

            if (i == len(banks) - 1):
                i = 0
            else:
                i += 1

        print(banks) 
        ans += 1
        temp_set = [x[1] for x in banks]
        print(temp_set)
        temp_set = tuple(temp_set)
        if (temp_set in perms):
            done = True
        else:
            perms.add(temp_set)
            print(perms)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day6s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.strip("\n")
    data = data.split()
    data = [int(x) for x in data]

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
