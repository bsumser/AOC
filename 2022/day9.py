import re
import time
import math
from itertools import groupby
import pyperclip
import numpy as np
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    start_time = time.time()
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited = set([Point(0, 0)])
    ans = 0

    for line in data:

        move = int(line[1])
        print(line)
        if line[0] == "R":
            print("move right %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[0] += 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "L":
            print("move left %d" % (move))
            for x


in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[0] -= 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "U":
            print("move up %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[1] += 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "D":
            print("move down %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[1] -= 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)

    ans = len(visited)

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def update_tail(head_pos, head_pos_old, tail_pos, visited):
    if (abs(tail_pos[0] - head_pos[0]) == 2) and (tail_pos[1] != head_pos[1]):
        tail_pos = head_pos_old
    if (abs(tail_pos[1] - head_pos[1]) == 2) and (tail_pos[0] != head_pos[0]):
        tail_pos = head_pos_old
    elif (head_pos[0] - tail_pos[0]) > 1:
        print("move one right")
        tail_pos[0] += 1
    elif (tail_pos[0] - head_pos[0]) > 1:
        print("move one left")
        tail_pos[0] -= 1
    elif (head_pos[1] - tail_pos[1]) > 1:
        print("move one up")
        tail_pos[1] += 1
    elif (tail_pos[1] - head_pos[1]) > 1:
        print("move one down")
        tail_pos[1] -= 1

    tempPoint = Point(tail_pos[0], tail_pos[1])
    visited.add(tempPoint)
    print(head_pos)
    print(tail_pos)

    return (head_pos, tail_pos, visited)

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 1 starting")
    start_time = time.time()
    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_nodes = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    visited = set([Point(0, 0)])
    visited9 = set([Point(0, 0)])
    ans = 0

    for line in data:

        move = int(line[1])
        print(line)
        if line[0] == "R":
            print("move right %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[0] += 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "L":
            print("move left %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[0] -= 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "U":
            print("move up %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[1] += 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)
        if line[0] == "D":
            print("move down %d" % (move))
            for x in range(0, move, 1):
                head_pos_old = head_pos[:]
                head_pos[1] -= 1
                head_pos, tail_pos, visited = update_tail(head_pos, head_pos_old, tail_pos, visited)

    ans = len(visited)

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def update_tail_2(head_pos, head_pos_old, tail_pos, visited):
    if (abs(tail_pos[0] - head_pos[0]) == 2) and (tail_pos[1] != head_pos[1]):
        tail_pos = head_pos_old
    if (abs(tail_pos[1] - head_pos[1]) == 2) and (tail_pos[0] != head_pos[0]):
        tail_pos = head_pos_old
    elif (head_pos[0] - tail_pos[0]) > 1:
        print("move one right")
        tail_pos[0] += 1
    elif (tail_pos[0] - head_pos[0]) > 1:
        print("move one left")
        tail_pos[0] -= 1
    elif (head_pos[1] - tail_pos[1]) > 1:
        print("move one up")
        tail_pos[1] += 1
    elif (tail_pos[1] - head_pos[1]) > 1:
        print("move one down")
        tail_pos[1] -= 1

    tempPoint = Point(tail_pos[-1][0], tail_pos[-1][1])
    visited.add(tempPoint)
    print(head_pos)
    print(tail_pos)

    return (head_pos, tail_pos, visited)

def parse_data():
    #data = get_data(day=9, year=2022)
    my_file = open("input2.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    data = [line.split() for line in data]
    data = [line for line in data if line != []]
    my_file.close()
    print(data)



    #my_file = open("maze.txt", "r")
    #data = my_file.read()
    #data = data.split("\n")
    #data = [list(line) for line in data]
    #my_file.close()

    return data

def main():
    ans = 0
    data1 = parse_data()
    data2 = parse_data()

    for line in data1:
        print(line)

    # ---------------Part 1------------------- #
    ans = part_1(data1)
    # ---------------Part 2------------------- #

    print(ans)
    pyperclip.copy(str(ans))
    return ans

main()
