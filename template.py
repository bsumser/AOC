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
    cover_set = set()
    numpy_data = np.array(data)
    min_x = min(min(numpy_data[:,0]), min(numpy_data[:,2]))
    max_x = max(max(numpy_data[:,0]), max(numpy_data[:,2]))
    print("min x is %d" % min_x)
    print("max x is %d" % max_x)
    for beacon in data:
        x1 = beacon[0]
        x2 = beacon[2]
        y1 = beacon[1]
        y2 = beacon[3]
        y = 2000000
        offset = 9000000
        beacon_dist = abs(x1 - x2) + abs(y1 - y2)
        #print(beacon_dist)

        for x in range(min_x - offset, max_x+offset, 1):
            if (x == x2 and y == y2):
                continue
            check_dist = abs(x1 - x) + abs(y1 - y)
            if (check_dist <= beacon_dist):
                cover_set.add(x)
    ans = len(cover_set)

    assert ans == 4748135

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def parse_data():
    #data = get_data(day=11, year=2022)
    my_file = open("input.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    my_file.close()
    data = list(map(lambda line: line.replace("Monkey ", ""), data))
    data = list(map(lambda line: line.replace("Sensor at x=", ""), data))
    data = list(map(lambda line: line.replace(", y=", " "), data))
    data = list(map(lambda line: line.replace("closest beacon is at x=", ""), data))
    data = list(map(lambda line: line.replace(":", ""), data))


    data = [line.split(" ") for line in data]
    data = [line for line in data if line != ['']]
    print(data)
    data = [list(map(int, line)) for line in data]
    #data = [line.split("\n") for line in data]
    #data = [val.strip() for line in data for val in line]
    #data = [line.split(" ") for line in data]


    return data


def main():
    ans = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    print(ans)
    pyperclip.copy(ans1)
    return 0
main()
