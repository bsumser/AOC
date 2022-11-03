import re
import math
import pyperclip
from aocd import get_data  # module for automating advent of code data get


def fuel_calc(value, total):
    if (value <= 0):
        return total
    fuel = 0
    fuel = (math.floor(value / 3) - 2)
    if fuel > 0:
        total += fuel
        print(fuel)
    return fuel_calc(fuel, total)


def main():
    input_data = get_data(day=1, year=2019)
    ans = 0

    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [int(line) for line in data]

    # ---------------Part 1------------------- #
    #ans = 0
    #for val in data:
    #    ans += (math.floor(val / 3) - 2)


    # ---------------Part 2------------------- #
    for val in data:
        ans += fuel_calc(val, 0)


    print(data)
    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
