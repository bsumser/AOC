#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
sys.set_int_max_str_digits(10000)
from saoc import coord_check_grid

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0
    iter = 0
    while(iter < 24):
        i = 0
        while(i < len(data)):
            cur = data[i]
            if cur == 0:
                data[i] = 1
            elif len(str(cur)) % 2 == 0:
                cur = str(cur)
                size = len(cur) // 2
                first = int(cur[0:size])
                second = int(cur[size:])
                data[i] = first
                data.insert(i+1, second)
                i += 1
            else:
                data[i] *= 2024
            i += 1
        iter += 1
        if (i == len(data)):
            i = 0
    ans = len(data)



    print("silver answer is: %d\n" % ans)
    return ans

def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0

    for iter in (0, 75): #parts 1 and 2
        print(sum(solve_stone(int(stone), iter) for stone in open("day11.txt").read().split()))

    
    print("Gold answer is: %d\n" % ans)
    return ans


def solve_stone(stone, iter):
    if iter == 0:
        return 1 
    elif stone == 0:
        return solve_stone(1, iter-1)
    elif len(str(stone)) % 2:
        return solve_stone(stone * 2024, iter-1)
    cur = str(stone)
    size = len(cur) // 2
    first = int(cur[0:size])
    second = int(cur[size:])
    return solve_stone(first, iter-1) + solve_stone(second, iter-1)

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().strip("\n")
    
    # ALL numbers to 2d list
    #data = [re.findall(r'\d+', line) for line in data]
    data = data.split(" ")
    data = [int(val) for val in data]

    #split on every char 
    data = list(data)
    #data = [int(val) for val in data]

    print(data)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    silver(parse_data())
    # ---------------Part 2------------------- #
    gold(parse_data())

    return 0

if __name__ == "__main__":
    main()
