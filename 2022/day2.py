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
    input_data = get_data(day=2, year=2022)
    ans = 0

    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [line.split(" ") for line in data]

    # need to make this work
    ansDict = {
        "A": {'X':1 + 3, 'Y':2+6, 'Z':3+0},
        "B": {'X':1 + 0, 'Y':2+3, 'Z':3+6},
        "C": {'X':1 + 6, 'Y':2+0, 'Z':3+3}
    }

    score = 0

    for line in data:
        score += ansDict[line[1][line[2]]]
    ans = score

    print(data)
    score = 0

    # ---------------Part 1------------------- #
    for line in data:
        if line[0] is "A":
            if line[1] is "X":
                score += 1 + 3
            elif line[1] is "Y":
                score += 2 + 6
            elif line[1] is "Z":
                score += 3 + 0

        elif line[0] is "B":
            if line[1] is "X":
                score += 1 + 0
            elif line[1] is "Y":
                score += 2 + 3
            elif line[1] is "Z":
                score += 3 + 6

        elif line[0] is "C":
            if line[1] is "X":
                score += 1 + 6
            elif line[1] is "Y":
                score += 2 + 0
            elif line[1] is "Z":
                score += 3 + 3
    ans = score
    # ---------------Part 2------------------- #
    score = 0
    for line in data:
        if line[0] is "A":
            if line[1] is "X":
                score += 3 + 0
            elif line[1] is "Y":
                score += 1 + 3
            elif line[1] is "Z":
                score += 2 + 6

        elif line[0] is "B":
            if line[1] is "X":
                score += 1 + 0
            elif line[1] is "Y":
                score += 2 + 3
            elif line[1] is "Z":
                score += 3 + 6

        elif line[0] is "C":
            if line[1] is "X":
                score += 2 + 0
            elif line[1] is "Y":
                score += 3 + 3
            elif line[1] is "Z":
                score += 1 + 6
    ans = score

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
