#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
sys.set_int_max_str_digits(10000)
from saoc import coord_check_grid

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0
    check_set = set()
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            if (row, col) not in check_set:
                peri = peri_calc(data, data[row][col], row, col, 0, 0, check_set)
                print(f"final peri is {peri} for {data[row][col]}")
                ans += peri


    print("silver answer is: %d\n" % ans)
    return ans

def peri_calc(data, letter, row, col, peri, area, check_set):
    check_set.add( (row, col))
    neighbors = coord_check_grid([row, col], len(data), len(data[0]), False)
    neighbors = [val for val in neighbors if data[val[0]][val[1]] == letter and (val[0], val[1]) not in check_set]
    print(f"{letter} has {neighbors}")
    peri += 4-len(neighbors)

    for neighbor in neighbors:
        peri += peri_calc(data, letter, neighbor[0], neighbor[1], 0, 0, check_set)
    return peri


def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0

    
    print("Gold answer is: %d\n" % ans)
    return ans


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    
    # ALL numbers to 2d list
    #data = [re.findall(r'\d+', line) for line in data]
    data = [list(line) for line in data]

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
