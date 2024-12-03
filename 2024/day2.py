#!/usr/bin/env python3
import time
import sys
import re
#import argparse
#from functools import reduce
from aocd import get_data  # module for automating advent of code data
from aocd import submit

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    data = list(filter(filter_helper_refined, data))
    ans = len(data)
    
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    #assert ans == 591

    #big boy assertion
    assert ans == 518
    return ans

def filter_helper_refined(line):
    diffs = []
    for i in range(1, len(line)):
        cur_diff = line[i] - line[i-1]
        if not(1 <= abs(cur_diff) and abs(cur_diff) <= 3):
            return False
    return True

def filter_helper(line):
    first = all(x<=y for x, y in zip(line, line[1:]))
    second = all(x>=y for x, y in zip(line, line[1:]))
    if (first == True or second == True):
        check = all( (1 <= abs(x - y) and abs(x - y) <= 3) for x,y in zip(line, line[1:]))
        if (check):
            return True
    return False


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    # You checked if removing a single index makes the report safe, twice.
    # It could be the same index, or different ones. this led to getting a higher
    # answer 
    data = list(filter(filter_helper_2, data))


    ans = len(data)
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    #assert ans == 621

    #big boy assertion
    assert ans == 776
    return ans


def filter_helper_2(line):
    idx = -1
    ret = False
    first = all(x < y for x, y in zip(line, line[1:]))
    second = all(x > y for x, y in zip(line, line[1:]))
    third = all( (1 <= abs(x - y) and abs(x - y) <= 3) for x,y in zip(line, line[1:]))
    # case 1: no removal needed
    if ((first or second) and (third)):
        return True
    
    #case 2: remove idx to close gap
    elif ((first or second) and not (third)):
        for l in range(0, len(line)):
            cur = line[:l] + line[l+1 :]
            check = all( (1 <= abs(x - y) and abs(x - y) <= 3) for x,y in zip(cur, cur[1:]))
            if (check):
                return True
    
    #case 2: remove idx to make monotonic
    elif (not (first or second) and (third)):
        for l in range(0, len(line)):
            cur = line[:l] + line[l+1 :]
            first = all(x < y for x, y in zip(cur, cur[1:]))
            second = all(x > y for x, y in zip(cur, cur[1:]))
            if (first or second):
                return True
    
    #case 2: remove idx to make monotonic and remove gap
    elif (not first and not second and not third):
        idx = -1
        
        #check for monotonic
        for l in range(0, len(line)):
            cur = line[:l] + line[l+1 :]
            first = all(x < y for x, y in zip(cur, cur[1:]))
            second = all(x > y for x, y in zip(cur, cur[1:]))
            if (first or second):
                idx = l
        
        # check for gap
        for l in range(0, len(line)):
            cur = line[:l] + line[l+1 :]
            check = all( (1 <= abs(x - y) and abs(x - y) <= 3) for x,y in zip(cur, cur[1:]))
            if (check):
                if (l == idx):
                    return True
    
    return False
    

def parse_data():
    start_time = time.time()
    #open file and count lines
    file_name = "./day2bigboy.txt"
    print(f"parsing data for {file_name}")

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    #data = get_data(day=2, year=2024)
    my_file.close()

    #parse data, array of lines
    data = data.split("\n")
    for i in range(0, len(data)):
        line = data[i]
        line = line.split(" ")
        line = list(filter(None, line))
        line = list(map(int, line))
        data[i] = line
    #data = [re.findall(r'\d+', line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    # remove trailing empty list
    data.pop()
    #data = [line.split("   ") for line in data]
    
    # 2d list and convert to ints
    #data = data.split("\n\n")
    #data = [line.split("\n") for line in data]
    #data = [[int(val) for val in line] for line in data]
    
    # examples
    #data = data.replace(" ", "")
    #data = data.split(",")
    #data = [re.split(r"([A-Z])",line) for line in data]
    #data = [val for sublist in data for val in sublist if val]

    print("Parsing done in %s seconds" % (time.time() - start_time))
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
    data = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data)
    submit_check(ans1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data)
    submit_check(ans2)

    return 0

if __name__ == "__main__":
    main()
