import re
import time
import math
from itertools import groupby
import pyperclip
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions
from collections import namedtuple

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    ans = 0
    monkeys = [[],[],[],[],[],[],[],]


    print(data)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def parse_data():
    data = get_data(day=11, year=2022)
    #my_file = open("sample.txt", "r")
    #data = my_file.read()
    data = data.split("\n\n")
    #my_file.close()
    for line in data:
        line.replace("\n", "")
        line.replace("Starting items:", "")
    print(data)

    return data

def main():
    ans = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    #ans2 = part_2(data2)

    #total_ans = str(ans1) + str(ans2)

    print(ans)
    pyperclip.copy(ans1)
    return 0
main()
