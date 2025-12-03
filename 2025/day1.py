#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()
    combo = []
    init = 50
    for num in range(0, 100):
        combo.append(num)
    print(combo)


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    for line in data:
        dir = line[0]
        nums = int(line[1:])
        if dir == "L": 
            nums *= -1
        init += nums
        init %= 100
        if init == 0: 
            ans += 1

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0
    init = 50

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    for line in data:
        dir = line[0]
        nums = int(line[1:])
        if dir == "L": 
            nums *= -1
        for i in range(0, abs(nums)):
            init += 1 if nums >= 0 else -1
            init %= 100
            if init == 0: 
                ans += 1

    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    data = data.split("\n") # split on single new line
    #data = list(map(int, data)) # map all to int

    #data = data.split("\n\n") # split on double newline
    #data = [line.split("\n") for line in data]

    print(data)
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
