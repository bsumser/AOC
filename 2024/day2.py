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
    new_data = []
    for line in data:
        first = all(x<=y for x, y in zip(line, line[1:]))
        second = all(x>=y for x, y in zip(line, line[1:]))
        if (first == True or second == True):
            ans += 1
            new_data.append(line)
    for line in new_data:
        print(line)
    print(f"ans {ans}")

    for i in range(0,len(new_data)):
        for j in range(1, len(new_data[i])):
            if (abs(new_data[i][j] - new_data[i][j-1]) > 3):
                ans -= 1
                break
            elif (abs(new_data[i][j] - new_data[i][j-1]) < 1):
                ans -= 1
                break
    
    
    
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
    new_data = []
    for line in data:
        first = all(x<=y for x, y in zip(line, line[1:]))
        second = all(x>=y for x, y in zip(line, line[1:]))
        if (first == True or second == True):
            new_data.append(line)
        else:
            #second check
            if (second_check(line)):
                new_data.append(line)
    
    for line in new_data:
        print(line)


    finals = []

    for line in new_data:
        check = all( (1 < abs(x - y) and abs(x - y) < 3) for x,y in zip(line, line[1:]))
        if (check):
            finals.append(line)
        else:
            if(second_chance(line)):
                finals.append(line)

    ans = len(finals)
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    assert ans == 621
    return ans

def second_check(line):
    for i in range(0, len(line)):
        cur = line[:i] + line[i+1 :]
        first = all(x<=y for x, y in zip(cur, cur[1:]))
        second = all(x>=y for x, y in zip(cur, cur[1:]))
        if (first == True or second == True):
            return True

def second_chance(line):
    for l in range(0, len(line)):
        cur = line[:l] + line[l+1 :]
        check = all( (1 <= abs(x - y) and abs(x - y) <= 3) for x,y in zip(cur, cur[1:]))
        if (check):
            print(f"true with {line}")
            return True
    print(f"false with {line}")
    return False
    
    
    

def parse_data():
    #open file and count lines
    file_name = "./day2.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    #data = get_data(day=2, year=2024)
    my_file.close()

    #parse data, array of lines
    data = data.split("\n")
    data = [re.findall(r'\d+', line) for line in data]
    data = [[int(val) for val in line] for line in data]
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
    #ans1 = part_1(data1)
    #submit_check(ans1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)
    submit_check(ans2)


    #pyperclip.copy(ans2)
    return 0

if __name__ == "__main__":
    main()