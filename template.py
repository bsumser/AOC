import re
import time
import math
import pyperclip
import numpy as np
from aocd import get_data  # module for automating advent of code data get
import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    print(data)
    print(len(data))
    start_time = time.time()
    ans = 0
    min_x = 0
    max_x = 0
    #numpy_data = np.array(data)
    #min_x = min(min(numpy_data[:,0]), min(numpy_data[:,2]))
    #max_x = max(max(numpy_data[:,0]), max(numpy_data[:,2]))
    #print("min x is %d" % min_x)
    #print("max x is %d" % max_x)

    min_x = data[0][0]
    max_x = data[0][0]
    min_y = data[0][1]
    max_y = data[0][1]

    for line in range(0, len(data), 1):
        for val in range(0, len(data[line]) - 1, 2):
            if data[line][val] < min_x: min_x = data[line][val]
            if data[line][val] > max_x: max_x = data[line][val]
            if data[line][val+1] < min_y: min_y = data[line][val+1]
            if data[line][val+1] > max_y: max_y = data[line][val+1]

    print("min x is %d" % min_x)
    print("max x is %d" % max_x)
    print("min y is %d" % min_y)
    print("max y is %d" % max_y)


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
    #data = get_data(day=11, year=2022)
    my_file = open("./2022/day14sample.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    my_file.close()
    data = list(map(lambda line: line.replace("->", ""), data))
    data = list(map(lambda line: line.replace(",", " "), data))
    data = list(map(lambda line: line.replace("  ", " "), data))


    data = [line for line in data if line != '']
    data = [line.split(" ") for line in data]
    data = [list(map(int, line)) for line in data]
    print(data)


    return data


def main():
    ans = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    print(ans2)
    pyperclip.copy(ans2)
    return 0
main()
