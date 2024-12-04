#!/usr/bin/env python3
import time
import sys
import regex as re
from functools import reduce
from operator import add, mul
from aocd import get_data  # module for automating advent of code data
from aocd import submit
import numpy as np

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    data = np.array(data)
    rows, cols = data.shape
    print(data)
    for line in data:
        cur = "".join(line)
        matches = re.findall(r'XMAS|SAMX', cur, overlapped=True)
        #for match in matches: print(match)
        ans += len(matches)
    
    for col in range(0, cols):
        cur = "".join(data[0:rows, col])
        print(cur)
        matches = re.findall(r'XMAS|SAMX', cur, overlapped=True)
        #for match in matches: print(match)
        ans += len(matches)
    x,y = cols,rows
    diags = [data[::-1,:].diagonal(i) for i in range(-data.shape[0]+1,data.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(data.diagonal(i) for i in range(data.shape[1]-1,-data.shape[0],-1))

    # Another list comp to convert back to Python lists from numpy arrays,
    # so it prints what you requested.
    print ([n.tolist() for n in diags])

    for n in diags:
        cur = "".join(n)
        print(cur)
        matches = re.findall(r'XMAS|SAMX', cur, overlapped=True)
        #for match in matches: print(match)
        ans += len(matches)


    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    #assert ans == 173529487

    #big boy assertion
    #assert ans == 518
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    data = np.array(data)
    rows, cols = data.shape

    for row in range(1, len(data) - 1):
        for col in range(1, len(data[0]) - 1):
            if (data[row][col] == "A"):
                print("A has been found")
                diag1 = [data[row-1, col-1], data[row, col], data[row+1, col+1]]
                diag1 = "".join(diag1)
    
                diag2 = [data[row-1, col+1], data[row, col], data[row+1, col-1]]
                diag2 = "".join(diag2)

                if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                    ans += 1
    


    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    #assert ans == 99532691

    #big boy assertion
    #assert ans == 776
    return ans

def diag_finder(data, row, col):
    print("diag called")

def parse_data():
    start_time = time.time()

    # open file and read in data
    file_name = "./day4.txt"
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()
    
    #data = get_data(day=4, year=2024)

    data = data.split("\n")
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def parse_data_2():
    start_time = time.time()

    # open file and read in data
    #file_name = "./day4.txt"
    #print(f"parsing data for {file_name}")
    #my_file = open(file_name, "r")
    #data = my_file.read()
    #my_file.close()
    
    data = get_data(day=4, year=2024)

    data = data.split("\n")
    
    for line in data:
        print(data)

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

    # ---------------Part 1------------------- #
    data1 = parse_data()
    ans1 = part_1(data1)
    submit_check(ans1)
    # ---------------Part 2------------------- #
    data2 = parse_data()
    ans2 = part_2(data2)
    submit_check(ans2)

    return 0

if __name__ == "__main__":
    main()
