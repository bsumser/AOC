#!/usr/bin/env python3
import time
import sys
import re
sys.path.append('../')
sys.set_int_max_str_digits(10000)
sys.setrecursionlimit(1500)
from saoc import coord_check_grid

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    for group in data:
        a = [group[0], group[1]]
        b = [group[2], group[3]]
        prize = [group[4], group[5]]
        print(a, b, prize)

        cur = claw_sack(a, b, prize[0], prize[1], 0)
        print(f"{group} answer is {cur}")
        if (cur < 100000):
            ans += cur


    print("silver answer is: %d\n" % ans)
    return ans


def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0

    
    print("Gold answer is: %d\n" % ans)
    return ans

def claw_sack(a, b, prize_x, prize_y, coins, memo=None):
    if memo is None:
        memo = {}

    if (prize_x, prize_y) in memo:
        return memo[(prize_x, prize_y)]

    if prize_x == 0 and prize_y == 0:
        return 0
    
    elif prize_x < 0 or prize_y < 0:
        return 100000000
    
    else:
        res =  min(
            claw_sack(a, b, prize_x-a[0], prize_y-a[1], coins, memo) + 3,
            claw_sack(a, b, prize_x-b[0], prize_y-b[1], coins, memo) + 1
        )
    memo[(prize_x, prize_y)] = res
    return res


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n\n")
    
    # ALL numbers to 2d list
    #data = [line.split("\n") for line in data]
    data = [re.findall(r'\d+', line) for line in data]
    #data = [list(line) for line in data]
    data = [[int(val) for val in line] for line in data]

    #split on every char 
    #data = list(data)
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
