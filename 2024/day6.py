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

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    pos = set()
    start_row = 0
    start_col = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '^':
                start_row = row
                start_col = col
                print(f"pos is ({row}, {col})")

    dirs = ["U", "R", "D", "L"]
    dir = 0

    while (0 <= start_row < len(data) and 0 <= start_col < len(data[0])):
        if dir == "U":
            next_row, next_col = start_row - 1, start_col + 1
            if (data[next_row][next_col] == "."):
                start_row, start_col = next_row, next_col
            else
            

    
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

    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    data = [list(line) for line in data if line]

    print(data)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    part_1(parse_data())
    # ---------------Part 2------------------- #
    #part_2(parse_data())

    return 0

if __name__ == "__main__":
    main()
