#!/usr/bin/env python3
import time
#import re
#import argparse
#from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    wire_1_x = 0
    wire_1_y = 0
    wire_2_x = 0
    wire_2_y = 0

    wire_1_set = set()
    wire_2_set = set()
    assert len(data[0]) == len(data[1])

    for i in range(0, len(data[0])):

        wire_1_dir = data[0][i][0]
        wire_1_dist = int(data[0][i][1:])
        #print(wire_1_dir, wire_1_dist)

        while(wire_1_dist):
            match wire_1_dir:
                case "U":
                    wire_1_y += 1
                case "D":
                    wire_1_y -= 1
                case "R":
                    wire_1_x += 1
                case "L":
                    wire_1_x -= 1
            wire_1_dist -= 1
            wire_1_set.add((wire_1_x, wire_1_y))
        
        
        wire_2_dir = data[1][i][0]
        wire_2_dist = int(data[1][i][1:])
        while(wire_2_dist):
            match wire_2_dir:
                case "U":
                    wire_2_y += 1
                case "D":
                    wire_2_y -= 1
                case "R":
                    wire_2_x += 1
                case "L":
                    wire_2_x -= 1
            wire_2_dist -= 1
            wire_2_set.add((wire_2_x, wire_2_y))


    # get the intersection of sets
    inter = wire_1_set.intersection(wire_2_set)

    min_dist = 10000000000

    for val in inter:
        cur_dist = abs(0 - val[0]) + abs(0 - val[1])
        
        min_dist = cur_dist if cur_dist < min_dist else min_dist
    ans = min_dist 
   
   
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    assert ans == 1084
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    wire_1_x = 0
    wire_1_y = 0
    wire_2_x = 0
    wire_2_y = 0

    wire_1_set = set()
    wire_1_dict = {}
    wire_2_set = set()
    wire_2_dict = {}
    
    wire_1_steps = 0
    for i in range(0, len(data[0])):

        wire_1_dir = data[0][i][0]
        wire_1_dist = int(data[0][i][1:])
        #print(wire_1_dir, wire_1_dist)

        while(wire_1_dist):
            match wire_1_dir:
                case "U":
                    wire_1_y += 1
                case "D":
                    wire_1_y -= 1
                case "R":
                    wire_1_x += 1
                case "L":
                    wire_1_x -= 1
            wire_1_dist -= 1
            wire_1_steps += 1
            wire_1_set.add((wire_1_x, wire_1_y))
            if ((wire_1_x, wire_1_y) not in wire_1_dict):
                wire_1_dict[(wire_1_x, wire_1_y)] = wire_1_steps
        
    wire_2_steps = 0
    for i in range(0, len(data[1])):
        
        wire_2_dir = data[1][i][0]
        wire_2_dist = int(data[1][i][1:])
        while(wire_2_dist):
            match wire_2_dir:
                case "U":
                    wire_2_y += 1
                case "D":
                    wire_2_y -= 1
                case "R":
                    wire_2_x += 1
                case "L":
                    wire_2_x -= 1
            wire_2_dist -= 1
            wire_2_steps += 1
            wire_2_set.add((wire_2_x, wire_2_y))
            if ((wire_2_x, wire_2_y) not in wire_2_dict):
                wire_2_dict[(wire_2_x, wire_2_y)] = wire_2_steps


    # get the intersection of sets
    inter = wire_1_set.intersection(wire_2_set)

    min_dist = 10000000000

    for val in inter:
        print(val, wire_1_dict[val], wire_2_dict[val])
        cur_dist = wire_1_dict[val] + wire_2_dict[val]
        
        min_dist = cur_dist if cur_dist < min_dist else min_dist
    ans = min_dist 

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data_part_1():
    #open file and count lines
    file_name = "./day3.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    data[0] = data[0].split(",")
    data[1] = data[1].split(",")
    #data = data.replace(" ", "")
    #data = [re.split(r"([A-Z])",line) for line in data]
    #data = [val for sublist in data for val in sublist if val]

    print(data[0][0])
    print(data[1][0])
    return data

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data_part_1()
    data2 = parse_data_part_1()


    # ---------------Part 1------------------- #
    #ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()