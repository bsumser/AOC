import time
import re
from scanf import scanf #https://pypi.org/project/scanf/
import math
import numpy as np
import sys

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
from aocd import submit
from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    prev = []
    ans = minCost(data, len(data)-1, len(data[0])-1, prev)


    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)

def minCost(cost, row, col, prev):
    offset = 100000
     # For 1st column
    for i in range(1, row):
        cost[i][0] += cost[i - 1][0]
 
    # For 1st row
    for j in range(1, col):
        cost[0][j] += cost[0][j - 1]
 
    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, col):
            prev.insert(0, (i,j))
            if (len(prev) > 4):
                prev.pop(-1)
            if (len(prev) > 3):
                length = len(prev)
                last1 = prev[1]
                last2 = prev[2]
                last3 = prev[3]
                #print(last1, last2, last3)

                # same row
                if (last1[0] == last2[0] == last3[0] == row):
                    cost[i][j] += offset + (min(cost[i - 1][j], cost[i][j - 1]))

                # same col
                elif (last1[1] == last2[1] == last3[1] == row):
                    cost[i][j] += offset + (min(cost[i - 1][j], cost[i][j - 1]))

                else:
                    cost[i][j] += (min(cost[i - 1][j], cost[i][j - 1]))
 
    # Returning the value in
    # last cell
    return cost[row - 1][col - 1]
    
def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    
                    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''

    end_time = time.time() - start_time
    print("Part 2 done in %s seconds" % (end_time))
    print("Part 2 answer is: %d\n" % ans)
    return (ans, end_time)

def parse_data():
    #open file and count lines
    file_name = "./day17s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()


    '''-------------------------------PARSE BLOCK START------------------------------------------'''

    # split on newline
    data = data.split("\n")
    data = [list(map(int, list(line))) for line in data]
    
    #for i in range(0, len(data)):
    #    data[i] = list(map(int, data[i]))
    
    # convert to 2d array on every char
    #data = [list(line) for line in data]

    #filter out letters and leave only numbers
    # data = [''.join(filter(str.isdigit, val)) for val in data]

    # split on comma
    #data = data.split(",")

    # scanf for specific pattern
    #pattern = 'Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d'
    #data = [scanf(pattern, line) for line in data]

    # remove spaces
    #data = data.replace(" ", "")

    # regex
    #data = [re.split(r"([A-Z])",line) for line in data]

    # double list comp
    #data = [val for sublist in data for val in sublist if val]
    '''-------------------------------PARSE BLOCK END--------------------------------------------'''

    # print check
    for line in data:
        print(line)
    return data

def check_answer(answer):
    choice = input("ANSWER IS %d; DO YOU WISH TO SUBMIT (y/n)?\n" % (answer))

    if (choice == 'y'):
        try:
            print(submit(answer))
            print("submitted")
        except:
            print("answer is wrong")
        return 0
    else:
        return 0

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1, part1time = part_1(data1)
    # ---------------Part 2------------------- #
    ans2, part2time = part_2(data2)


    #check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
