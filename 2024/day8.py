#!/usr/bin/env python3
import time
import sys
import re
import math
sys.path.append('../')
import saoc
from functools import reduce
import operator
import itertools

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def __repr__(self):
        return f"Node(val='{self.val}', children={self.children})"

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    check_dict = {}

    for row in range(len(data)):
        for col in range(len(data[row])):
            cur = data[row][col]
            if cur == '.':
                continue
            elif cur in check_dict:
                check_dict[cur].append( (row,col) )
            else:
                check_dict[cur] = [(row,col)]

    for key,val in check_dict.items():
        print(key, val)

    dist_dict = {}
    anti_set = set()

    for key in check_dict.keys():
        coords = [val for val in check_dict[key]]
        test_list = list(itertools.combinations(coords, 2))
        print(f"test {test_list}")
        for combo in test_list:
            first = list(combo[0])
            second = list(combo[1])
            antis = check_line(first, second, key, data)
            for anti in antis:
                anti_set.add(anti)

    print(anti_set)
    ans += len(anti_set)

    print("Part 1 answer is: %d\n" % ans)
    return ans

def check_line(first, second, char, data):
    antis = []
    dist = check_dist(first, second) / 2
    slope = second[1] - first[1] / second[0] - first[0]
    rise = (second[1] - first[1])
    run = (second[0] - first[0])
    print(f"    check {char} {first}, {second} slope {slope} {rise}/{run} dist {dist}")
    a_1 = [0,0]
    a_2 = [0,0]

    if first[0] < second[0] and first[1] < second[1]:
        print("first is top left, second bottom right")
        a_1[0], a_1[1] = first[1] - rise, first[0] - run
        a_2[0], a_2[1] = second[1] + rise, second[0] + run
    elif first[0] > second[0] and first[1] < second[1]:
        print("first is bottom left, second top right")
        a_1[0], a_1[1] = first[1] + rise, first[0] - run
        a_2[0], a_2[1] = second[1] - rise, second[0] + run
    
    a_1[1] = first[1] - rise
    a_1[0] = first[0] - run

    a_2[1] = second[1] + rise
    a_2[0] = second[0] + run
    
    print(f"    antis {char} {first}, {second} at {a_1} and {a_2}")

    #check anti 1
    if (0 <= a_1[0] and a_1[0] < len(data) and 0 <= a_1[1] and a_1[1] < len(data[0])):
        antis.append(tuple(a_1))
    if (0 <= a_2[0] and a_2[0] < len(data) and 0 <= a_2[1] and a_2[1] < len(data[0])):
        antis.append(tuple(a_2))
    return antis

def check_dist(first, second):
    dist = abs(first[0] - second[0]) + abs(first[1] - second[1])
    return dist

def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0

    check_dict = {}

    for row in range(len(data)):
        for col in range(len(data[row])):
            cur = data[row][col]
            if cur == '.':
                continue
            elif cur in check_dict:
                check_dict[cur].append( (row,col) )
            else:
                check_dict[cur] = [(row,col)]

    for key,val in check_dict.items():
        print(key, val)

    dist_dict = {}
    anti_set = set()

    for key in check_dict.keys():
        coords = [val for val in check_dict[key]]
        test_list = list(itertools.combinations(coords, 2))
        print(f"test {test_list}")
        for combo in test_list:
            first = list(combo[0])
            second = list(combo[1])
            antis = check_line_gold(first, second, key, data)
            for anti in antis:
                anti_set.add(anti)

    print(anti_set)
    ans += len(anti_set)

    print("Gold answer is: %d\n" % ans)
    return ans

def check_line_gold(first, second, char, data):
    antis = []
    dist = check_dist(first, second) / 2
    slope = second[1] - first[1] / second[0] - first[0]
    rise = (second[1] - first[1])
    run = (second[0] - first[0])
    print(f"    check {char} {first}, {second} slope {slope} {rise}/{run} dist {dist}")
    a_1 = [0,0]
    a_2 = [0,0]
    a_1[1] = first[1] - rise
    a_1[0] = first[0] - run
    antis.append(tuple(a_1))
    
    while (0 <= a_1[0] and a_1[0] < len(data) and 0 <= a_1[1] and a_1[1] < len(data[0])):
        antis.append(tuple(a_1))
        a_1[1] -=  rise
        a_1[0] -=  run
        print(a_1)

    a_2[1] = second[1] + rise
    a_2[0] = second[0] + run
    antis.append(tuple(a_2))
    
    while (0 <= a_2[0] and a_2[0] < len(data) and 0 <= a_2[1] and a_2[1] < len(data[0])):
        antis.append(tuple(a_2))
        a_2[1] += rise
        a_2[0] += run

    print(f"    antis {char} {first}, {second} at {a_1} and {a_2}")

    return antis


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    
    # GET ALL THE NUMBERS IN A LINE
    #data = [re.findall(r'\d+', line) for line in data]

    #REMOVE TRAILING EMPTY LISTS
    data = [list(line) for line in data if line]
    #data = [[int(val) for val in line] for line in data]

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
