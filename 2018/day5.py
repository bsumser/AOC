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
    data = list(data[0])
    print(data)

    stack = []
    message = ""

    stack.append(data.pop(0))
    while(len(data) is not 0):
        #print(data[0], stack)
        if (len(stack) == 0 and len(data) != 0):
            stack.append(data.pop(0))
        elif ( abs(ord(stack[-1]) - ord(data[0])) == 32 ):
            message = stack[-1] + data[0] + " react"
            stack.pop()
            data.pop(0)
        else:
            message = stack[-1] + data[0] + " no react"
            stack.append(data.pop(0))
        #print(message)
        if(len(data) == 0):
            break
    #print(str(data), str(stack))

    ans = len(stack)

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
    shortest = 1000000000000000000000000000000
    data = list(data[0])
    for i in range(0, 26):
        char1 = chr(65 + i)
        char2 = chr(97 + i)
        stack = []
        cur_data = []
        for char in data:
            if char != char1 and char != char2:
                cur_data.append(char)
        message = ""

        #print(data)

        stack.append(cur_data.pop(0))
        while(len(cur_data) is not 0):
            #print(cur_data[0], stack)
            if (len(stack) == 0 and len(cur_data) != 0):
                stack.append(cur_data.pop(0))
            elif ( abs(ord(stack[-1]) - ord(cur_data[0])) == 32 ):
                message = stack[-1] + cur_data[0] + " react"
                stack.pop()
                cur_data.pop(0)
            else:
                message = stack[-1] + cur_data[0] + " no react"
                stack.append(cur_data.pop(0))
            #print(message)
            if(len(cur_data) == 0):
                break
        #print(str(cur_data), str(stack))
        print("remove " + char1 + char2 + str(len(stack)))
        if ( len(stack) < shortest):
            shortest = len(stack)

    ans = shortest

    assert ans < 9348 
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day5.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    
    return data

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()


    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()