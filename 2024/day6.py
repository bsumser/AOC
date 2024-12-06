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

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0

    data[start_row][start_col] = '.'
    while (0 <= start_row < len(data) and 0 <= start_col < len(data[0])):
        next_row, next_col = start_row + dirs[dir % 4][0], start_col + dirs[dir%4][1]

        if not (0 <= next_row < len(data) and 0 <= next_col < len(data[0])):
            break
        
        if data[next_row][next_col] == '.':
            start_row, start_col = next_row, next_col
            pos.add( (start_row, start_col) )
        elif data[next_row][next_col] == '#':
                dir += 1
    ans = len(pos)
    
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans, pos


def part_2(data, pos):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    start_row = 0
    start_col = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == '^':
                start_row, init_row = row, row
                start_col, init_col = col, col
                print(f"pos is ({row}, {col})")

    copy = [row[:] for row in data]
    for loc in pos:
        copy[loc[0]][loc[1]] = '#'
        if cycle_detect(copy, init_row, init_col):
            ans += 1
        copy[loc[0]][loc[1]] = '.'

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def cycle_detect(data, start_row, start_col):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = 0

    cycle_count = {}
    cycle_thresh = 4

    data[start_row][start_col] = '.'
    while (0 <= start_row < len(data) and 0 <= start_col < len(data[0])):
        next_row, next_col = start_row + dirs[dir % 4][0], start_col + dirs[dir%4][1]

        if not (0 <= next_row < len(data) and 0 <= next_col < len(data[0])):
            break
        
        if data[next_row][next_col] == '.':
            start_row, start_col = next_row, next_col
        elif data[next_row][next_col] == '#':
                dir += 1
        if (start_row, start_col) in cycle_count:
            cycle_count[ (start_row, start_col)] += 1
            if cycle_count[ (start_row, start_col)] > cycle_thresh:
                return True
        elif (start_row, start_col) not in cycle_count:
            cycle_count[ (start_row, start_col)] = 1
    return False

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    data = [list(line) for line in data if line]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    ans, pos = part_1(parse_data())
    # ---------------Part 2------------------- #
    part_2(parse_data(), pos)

    return 0

if __name__ == "__main__":
    main()
