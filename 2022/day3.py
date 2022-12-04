import re
import math
import pyperclip
from aocd import get_data  # module for automating advent of code data get
from itertools import groupby

def part_1(data):
    print("part 2")
    ans = 0
    for line in data:
        temp = []
        firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]
        print(firsthalf, secondhalf)

        set1 = set(firsthalf)
        set2 = set(secondhalf)

        common = ''.join(sorted(set1.intersection(set2)))
        commonList.append(common)

        for char in common:
            if char.isupper() is False:
                ans += ord(char) - 96
                print(char + " " + str(ord(char) - 96))
            elif char.isupper() is True:
                ans += ord(char) - 38
                print(char + " " + str(ord(char) - 38))

    return ans

def part_2(data):
    print("part 2")
    ans = 0
    for x in range(0, len(data) - 5, 6):
        set1 = set(data[x])
        set2 = set(data[x + 1])
        set3 = set(data[x + 2])
        set4 = set(data[x + 3])
        set5 = set(data[x + 4])
        set6 = set(data[x + 5])
        common = set1.intersection(set2)
        common = set3.intersection(common)
        common2 = set4.intersection(set5)
        common2 = set6.intersection(common2)
        print(str(common) + " " + str(common2))
        for char in common:
            if char.isupper() is False:
                ans += ord(char) - 96
                print(char + " " + str(ord(char) - 96))
            elif char.isupper() is True:
                ans += ord(char) - 38
                print(char + " " + str(ord(char) - 38))
        for char in common2:
            if char.isupper() is False:
                ans += ord(char) - 96
                print(char + " " + str(ord(char) - 96))
            elif char.isupper() is True:
                ans += ord(char) - 38
                print(char + " " + str(ord(char) - 38))

    return ans

def main():
    input_data = get_data(day=3, year=2022)
    ans = 0

    commonList = []

    data = [line.strip() for line in input_data.split("\n")]  # split into list
    print(len(data))

    # ---------------Part 1------------------- #
    ans = part_1(data)
    # ---------------Part 2------------------- #
    ans = part_2(data)

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
