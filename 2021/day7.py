#!/usr/bin/env python3
import time

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
    data = list(set(data))
    data.sort()
    print(data[0])
    print(data[-1])

    mid = (len(data) - 1) // 2
   
    print(data[mid-2:mid+3])
    print(abs(474 - data[0]))
    print(abs(475 - data[-1]))
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    print(data[0])
    start_time = time.time()
    ans = 0
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 



   
   
   
   
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day1.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.strip("\n")
    data = data.split(",")
    data = [int(x) for x in data]

    #print(data[0])
    return data

def check_answer(answer):
    choice = input("ANSWER IS %d; DO YOU WISH TO SUBMIT (y/n)?\n" % (answer))

    if (choice == 'y'):
        try:
            print(submit(answer))
        except:
            print("exception has occurred")
        return 0
    else:
        return 0

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    check_answer(ans1)
    #check_answer(ans2)
    return 0
main()
