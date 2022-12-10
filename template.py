import re
import time
import math
from itertools import groupby
import pyperclip
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions
from collections import namedtuple



def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    ans = 0
    ins_queue = []
    ins_cycle = []
    com_ins = []
    cycle_pop = []
    reg = 1
    com_ins.append(reg)
    check_set = set()
    check_set = {20, 60, 100, 140, 180, 220}
    cycle = 0

    for x in range(0, len(data), 1):
        cycle += 1
        if ins_cycle != [] and ins_cycle[0] != 0:
            x -= 1
            continue
        print (data[x])
        print("reg is %d at cycle %d" % (reg, cycle))
        print(ins_queue)
        print(ins_cycle)
        if (cycle % 20 == 0 and cycle < 221 and cycle in check_set):
            print("CYCLE 20 hit")
            print("COMP INS")
            print(com_ins)
            print("%d * %d" % (cycle, reg))
            signal = (cycle * reg)
            cycle_pop.append(signal)
        if (data[x][0] == "addx"):
            print("adding %d to ins_queue" % (int(data[x][1])))
            ins_queue.append(int(data[x][1]))
            ins_cycle.append(2)
        if ins_cycle:
            ins_cycle[0] -= 1
            x -= 1
        if (ins_cycle and ins_cycle[0] == 0):
            print("poping instruction")
            com_ins.append(ins_queue[0])
            reg += ins_queue.pop(0)
            ins_cycle.pop(0)
        print("reg is %d after cycle %d" % (reg, cycle))
        print(ins_queue)
        print(ins_cycle)

    ans = sum(cycle_pop)
    print(cycle_pop)
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 1 starting")
    start_time = time.time()
    ans = 0

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans


def parse_data():
    #data = get_data(day=10, year=2022)
    my_file = open("input.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    data = [line.split() for line in data]
    data = [line for line in data if line != []]
    my_file.close()
    print(data)

    return data

def main():
    ans = 0
    data1 = parse_data()
    #data2 = parse_data()

    # ---------------Part 1------------------- #
    ans = part_1(data1)
    # ---------------Part 2------------------- #

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
