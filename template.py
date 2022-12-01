import re
import math
import pyperclip
from aocd import get_data  # module for automating advent of code data get
from itertools import groupby


def part_1(data):
    print("part 2")
    ans = 0

    return ans

def part_2(data):
    print("part 2")
    ans = 0

    return ans

def main():
    input_data = get_data(day=1, year=2022)
    ans = 0

    myList = [line.strip() for line in input_data.split("\n")]  # split into list
    result = [[]]
    for i in myList:
        if not i:
            result.append([])
        else:
            result[-1].append(i)
    print(result)
    temp = 0
    maxVal1 = 0
    maxVal2 = 0
    maxVal3 = 0

    # ---------------Part 1------------------- #
    for subList in result:
        temp = 0
        for val in subList:
            temp += int(val)
        if temp >= maxVal1:
            maxVal3 = maxVal2
            maxVal2 = maxVal1
            maxVal1 = temp
        elif temp >= maxVal2:
            maxVal3 = maxVal2
            maxVal2 = temp
        elif temp >= maxVal3:
            maxVal3 = temp
    ans = maxVal1 + maxVal2 + maxVal3

    # ---------------Part 2------------------- #

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
