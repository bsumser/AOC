#!/usr/bin/env python3
import time
import sys
sys.setrecursionlimit(1500)
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    ranges, ing = list(map(parser, (data[0].split("\n")))), list(map(int, (data[1].split("\n"))))
    print(ranges, ing)

    for item in ing:
        for range in ranges:
            if item >= range[0] and item <= range[1]:
                ans += 1
                break

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def parser(range):
    range = range.split("-")
    first, second = int(range[0]), int(range[1])
    return [first, second]

def mergeOverlap(arr):
    n = len(arr)

    arr.sort()
    res = []

    # Checking for all possible overlaps
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # Skipping already merged intervals
        if res and res[-1][1] >= end:
            continue

        # Find the end of the merged range
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
        res.append([start, end])
    
    return res


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    ranges, ing = list(map(parser, (data[0].split("\n")))), list(map(int, (data[1].split("\n"))))
    print(ranges, ing)

    ranges.sort(key=lambda item: item[0])
    ranges = mergeOverlap(ranges)
    for item in ranges:
        ans += (item[1] - item[0])+1
    print(ranges)

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    data = data.split("\n\n") # split on single new line
    #data = list(map(int, data)) # map all to int


    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    part_1(parse_data())
    # ---------------Part 2------------------- #
    part_2(parse_data())

    return 0

if __name__ == "__main__":
    main()
