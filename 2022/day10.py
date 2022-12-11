import re
import time
import math
from itertools import groupby
import pyperclip
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions
from collections import namedtuple

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    ans = 0
    ins_queue = []
    ins_cycle = []
    cycle = 0
    reg = 1
    com_ins = []
    cycle_pop = []
    com_ins.append(reg)
    check_set = set()
    check_set = {20, 60, 100, 140, 180, 220}

    for line in data:
        ins_queue.append(line)
        ins_cycle.append(2)

    while ins_queue and cycle < 221:
        cycle += 1
        print("ins %s at cycle %d" % (ins_queue[0], cycle))
        if (ins_queue[0][0] == "noop"):
            print("noop")
            ins_queue.pop(0)
            ins_cycle.pop(0)
            if (cycle % 20 == 0 and cycle < 221 and cycle in check_set):
                print("CYCLE 20 hit")
                print("COMP INS")
                print(com_ins)
                print("%d * %d" % (cycle, reg))
                signal = (cycle * reg)
                cycle_pop.append(signal)
            continue
        ins_cycle[0] -= 1
        print("reg is %d at cycle %d" % (reg, cycle))
        if (cycle % 20 == 0 and cycle < 221 and cycle in check_set):
            print("CYCLE 20 hit")
            print("COMP INS")
            print(com_ins)
            print("%d * %d" % (cycle, reg))
            signal = (cycle * reg)
            cycle_pop.append(signal)
        if (ins_cycle and ins_cycle[0] == 0):
            ins = ins_queue.pop(0)
            print("poping instruction %s" % (ins))
            ins_cycle.pop(0)
            if ins != "noop":
                com_ins.append(ins[1])
                reg += int(ins[1])
        print("reg is %d after cycle %d" % (reg, cycle))

    print(cycle_pop)
    ans = sum(cycle_pop)

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0
    ins_queue = []
    ins_cycle = []
    cycle = 0
    reg = 1
    com_ins = []
    cycle_pop = []
    com_ins.append(reg)
    check_set = set()
    scan_line = 0
    read_out = [ ["."]*40 for i in range(6)]
    #read_out = ["." for i in range(6*40)]
    check_set = {20, 60, 100, 140, 180, 220}
    cycle_set = {40, 80, 120, 160, 200, 240}

    for line in data:
        ins_queue.append(line)
        ins_cycle.append(2)

    while ins_queue and cycle < 221:
        cycle += 1
        cycle_low = (cycle % 40) - 1
        cycle_hi = (cycle % 40) + 1
        pos = cycle % 40 - 1
        if cycle in cycle_set: scan_line += 1
        #print("ins %s at cycle %d" % (ins_queue[0], cycle))
        print("reg val %d in range (%d,%d) at cycle %d" % (reg, cycle_low, cycle_hi, cycle))
        if (pos in (reg - 1, reg, reg + 1)):
            print("CRT draws pixel in position %d" % (reg))
            read_out[scan_line][pos] = "#"
        if (ins_queue[0][0] == "noop"):
            #print("noop")
            ins_queue.pop(0)
            ins_cycle.pop(0)
            if (cycle % 20 == 0 and cycle < 221 and cycle in check_set):
                #print("CYCLE 20 hit")
                #print("COMP INS")
                #print(com_ins)
                #print("%d * %d" % (cycle, reg))
                signal = (cycle * reg)
                cycle_pop.append(signal)
            continue
        ins_cycle[0] -= 1
        #print("reg is %d at cycle %d" % (reg, cycle))
        if (cycle % 20 == 0 and cycle < 221 and cycle in check_set):
            #print("CYCLE 20 hit")
            #print("COMP INS")
            #print(com_ins)
            #print("%d * %d" % (cycle, reg))
            signal = (cycle * reg)
            cycle_pop.append(signal)
        if (ins_cycle and ins_cycle[0] == 0):
            ins = ins_queue.pop(0)
            #print("poping instruction %s" % (ins))
            ins_cycle.pop(0)
            if ins != "noop":
                com_ins.append(ins[1])
                reg += int(ins[1])
        #print("reg is %d after cycle %d" % (reg, cycle))

    print(cycle_pop)
    ans = sum(cycle_pop)

    print(read_out)
    for row in read_out:
        print(*row, sep='')
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
    data2 = parse_data()

    # ---------------Part 1------------------- #
    #ans = part_1(data1)
    # ---------------Part 2------------------- #
    ans = part_2(data2)

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
