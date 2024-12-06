#!/usr/bin/env python3
import time
import sys
import re
from functools import reduce
from operator import add, mul

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    ans = sum(map(lambda sublist: reduce(lambda x,y: x*y, sublist), data))
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    ans = reduce(add, map(lambda line: reduce(add, map(lambda xy: xy[0]*xy[1], line)), data), 0)
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data_1():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().strip("\n")
    data = re.findall(r'mul\(\d+,\d+\)', data)
    data = [[int(val) for val in re.findall(r'\d+', line)] for line in data]
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

def main():
    # ---------------Part 1------------------- #
    part_1(parse_data_1())
    # ---------------Part 2------------------- #
    part_2(parse_data_2())

    return 0

if __name__ == "__main__":
    main()
