import re
import math
import pyperclip
import aocFunctions
from aocd import get_data  # module for automating advent of code data get
from itertools import groupby

def part_1(data):
    print("part 2")
    ans = 0
    for i in range(0, len(data) - 3, 4):
        x = set(range(data[i],data[i+1] + 1))
        y = set(range(data[i+2],data[i+3] + 1))
        if (x.issubset(y)):
            ans += 1
        elif (y.issubset(x)):
            ans += 1

    return ans

def part_2(data):
    print("part 2")
    ans = 0
    for i in range(0, len(data) - 3, 4):
        x = set(range(data[i],data[i+1] + 1))
        y = set(range(data[i+2],data[i+3] + 1))
        setans = x.intersection(y)
        #print(xs)
        if (len(setans)):
            print(setans)
            ans += 1
    return ans

def main():
    input_data = get_data(day=4, year=2022)
    ans = 0
    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [line.split(",") for line in data]
    data = [val.split("-") for sublist in data for val in sublist]
    data = [int(val) for sublist in data for val in sublist]
    print(data)
    print(len(data))

    # ---------------Part 1------------------- #
    ans = part_1(data)
    # ---------------Part 2------------------- #
    #ans = part_2(newData)

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
