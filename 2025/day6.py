#!/usr/bin/env python3
import time
import sys
from functools import reduce
sys.setrecursionlimit(1500)
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    data = [line.split() for line in data]
    for i in range(0, len(data[0])):
        nums = list(map(int, [data[0][i], data[1][i], data[2][i], data[3][i]]))
        op = data[4][i]
        if op == "+":
            ans += sum(nums)
        elif op == "*":
            ans += reduce((lambda x, y: x * y), nums)
        print(nums)

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
    codes = [[], [], [], [], []]
    for i in range(0, len(data[0])):
        codes[0].append(data[0][i])
        codes[1].append(data[1][i])
        codes[2].append(data[2][i])
        codes[3].append(data[3][i])
        codes[4].append(data[4][i])
        print(codes)
        if codes[0][-1] == " " and codes[1][-1] == " " and codes[2][-1] and codes[3][-1] == " " and codes[4][-1] == " ":
            print("nums done")
            ans += handle_codes(codes)
            codes = [[], [], [], [], []]

    ans += handle_codes(codes)
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def handle_codes(codes):
    ans = 0
    print("handling codes")
    list_len = [len(i) for i in codes]
    print(max(list_len))
    op = codes[4][0]
    print(op)
    if op == "+":
        offset = 0
    elif op == "*":
        offset = 1
    nums = []
    for i in range(0, len(codes[0])):
        cur_num = codes[0][i] + codes[1][i] + codes[2][i] + codes[3][i]
        if cur_num != "    ":
            nums.append(int(cur_num))

    for num in nums:
        print(num)
    if op == "+":
        ans = sum(nums)
    elif op == "*":
        ans = reduce((lambda x, y: x * y), nums)
    print(f"sum/prod is {ans}")
    return ans


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    data = data.split("\n") # split on single new line

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
