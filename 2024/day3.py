#!/usr/bin/env python3
import time
import sys
import re
from functools import reduce
from operator import add, mul
from aocd import get_data  # module for automating advent of code data
from aocd import submit

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    ans = sum(map(lambda sublist: reduce(lambda x,y: x*y, sublist), data))
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    assert ans == 173529487

    #big boy assertion
    #assert ans == 518
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    ans += reduce(add, map(lambda line: reduce(add, map(lambda xy: xy[0]*xy[1], line)), data), 0)
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    assert ans == 99532691

    #big boy assertion
    #assert ans == 776
    return ans

def parse_data_1():
    start_time = time.time()

    # open file and read in data
    file_name = "./day3.txt"
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    data = data.strip("\n")
    data = re.findall(r'mul\(\d+,\d+\)', data)
    data = [re.findall(r'\d+', line) for line in data]
    data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def parse_data_2():
    start_time = time.time()

    # open file and read in data
    file_name = "./day3.txt"
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    data = data.strip("\n")
    data = data.replace("do()", "doGO")
    data = data.replace("don't()", "dontSTOP")
    data = re.split(r'(do|dont)', data)
    data = [line.replace("ntSTOP", "STOP") for line in data]
    data = [line for line in data if line != "do"]

    ret_data = []
    for i in range(0, len(data)):
        if (data[i][0] is 'S'):
            continue
        cur = re.findall(r'mul\(\d+,\d+\)', data[i])
        cur = [re.findall(r'\d+', line) for line in cur]
        cur = [[int(val) for val in line] for line in cur]
        ret_data.append(cur)

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return ret_data

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

    # ---------------Part 1------------------- #
    data1 = parse_data_1()
    ans1 = part_1(data1)
    submit_check(ans1)
    # ---------------Part 2------------------- #
    data2 = parse_data_2()
    ans2 = part_2(data2)
    submit_check(ans2)

    return 0

if __name__ == "__main__":
    main()
