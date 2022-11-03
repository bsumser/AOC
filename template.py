import re
import math
import pyperclip
from aocd import get_data  # module for automating advent of code data get


def part_2(data):
    noun = 0
    verb = 0
    for noun in range(0, 100):
        for verb in range(0, 100):
            data_copy = data
            print(noun, verb, sep=" ")
            ans = part_1(noun, verb, data_copy)
            if (ans == 19690720):
                return 100 * noun + verb


def part_1(noun, verb, data):
    data[1] = noun
    data[2] = verb
    count = 0
    for count in range(0, len(data)):
        print(count)
        if (data[count] == 99):
            print(noun, verb, data[count], sep=" ")
            return data[0]
        if (data[count] == 1):
            data[data[count+3]] = data[data[count+2]] + data[data[count+1]]
            count += 4
        if (data[count] == 2):
            data[data[count+3]] = data[data[count+2]] * data[data[count+1]]
            count += 4
    print("done")
    return data[0]

def main():
    input_data = get_data(day=2, year=2019)
    ans = 0

    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [line.strip() for line in input_data.split(",")]  # split into list
    data = [int(line) for line in data]
    print(data)
    print(len(data))

    # ---------------Part 1------------------- #
    # data[1] = 12
    # data[2] = 2
    # count = 0
    # while count <= len(data):
    #     if (data[count] == 99):
    #         break
    #     elif (data[count] == 1):
    #         data[data[count+3]] = data[data[count+2]] + data[data[count+1]]
    #         count += 4
    #     elif (data[count] == 2):
    #         data[data[count+3]] = data[data[count+2]] * data[data[count+1]]
    #         count += 4
    # ans = data[0]

    # ---------------Part 2------------------- #
    noun = 0
    verb = 0
    while noun < 100:
        part_1(12, 2, data)
        noun += 1

    print(ans)
    pyperclip.copy(str(ans))
    return 0

main()
