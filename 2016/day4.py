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

    for line in data:
        #count frequency of chars in string
        freq = {i: line[0].count(i) for i in set(line[0])}

        # sort by frequency, then by alphabetical on ties of frequency
        freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        print(freq)

        # get just the letters ordered by freq/alpha
        freq = [x[0] for x in freq]

        #slice first 5 elements
        freq = freq[0:5]
        print(freq)

        #compare set of slice to set of checksum, add sector ID if they match
        if (set(freq) == set(line[2])):
            ans += int(line[1])


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    for line in data:
        offset = int(line[1]) % 26
        for i in range(0, len(line[0])):
            if (line[0][i] == '-'):
                cur_str = list(line[0])
                cur_str[i] = ' '
                line[0] = ''.join(cur_str)
            else:
                cur_char = line[0][i]
                cur_char = ord(cur_char)
                if (cur_char + offset > 122):
                    cur_char = (cur_char + offset) - 26
                else:
                    cur_char = cur_char + offset
                cur_str = list(line[0])
                cur_str[i] = chr(cur_char)
                line[0] = ''.join(cur_str)

    print(data)
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day4dash.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    data = [line.split(",") for line in data]

    print(data)
    return data


def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    #ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()
