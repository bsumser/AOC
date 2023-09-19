#!/usr/bin/env python3
import time
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get
#import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    lights = [[-1] * 1000 for i in range(1000)]

    for line in data:
        start_row = int(line[2])
        start_col = int(line[1])
        end_row = int(line[4])
        end_col = int(line[3])

        #print("%sing lights from %d,%d to %d,%d" %
        #      (line[0], start_row, end_row, start_col, end_col))

        for i in range (start_row, end_row+1):
            for j in range (start_col, end_col+1):
                match line[0]:
                    case 'toggle':
                        lights[i][j] *= -1
                    case 'off':
                        if lights[i][j] == 1:
                            lights[i][j] = -1
                    case 'on':
                        if lights[i][j] == -1:
                            lights[i][j] = 1
    ans = sum(x.count(1) for x in lights)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    lights = [[0] * 1000 for i in range(1000)]

    for line in data:
        start_row = int(line[2])
        start_col = int(line[1])
        end_row = int(line[4])
        end_col = int(line[3])

        #print("%sing lights from %d,%d to %d,%d" %
        #      (line[0], start_row, end_row, start_col, end_col))

        for i in range (start_row, end_row+1):
            for j in range (start_col, end_col+1):
                match line[0]:
                    case 'toggle':
                        lights[i][j] += 2
                    case 'off':
                        if lights[i][j] > 0:
                            lights[i][j] -= 1
                    case 'on':
                        lights[i][j] += 1
    ans = sum(map(sum, lights))

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def parse_data():
    my_file = open("./day6.txt", "r")
    data = my_file.read()
    my_file.close()
    data = data.strip("\n\n")
    data = data.replace(" through", "")
    data = data.replace("turn ", "")
    data = data.replace(",", " ")
    data = data.split("\n")
    data = [x.split(" ") for x in data]


    print(data)
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
