#!/usr/bin/env python3
import time
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get
#import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    print(data)
    start_time = time.time()

    for i in range(0, len(data)):
        l = int( data[i][0] )
        w = int( data[i][1] )
        h = int( data[i][2] )
        side = min( (l*w), (w*h), (h*l) )
        ans += 2*l*w + 2*w*h + 2*h*l + side

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def parse_data():
    my_file = open("./day2.txt", "r")
    data = my_file.read()
    my_file.close()
    data = data.split("\n")
    data = [x for x in data if x]
    data = [x.split("x") for x in data]
    #data = [int(num) for row in data for num in row]


    #print(data)
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


    print(ans1)
    print(ans2)
    #pyperclip.copy(ans2)
    return 0
main()
