#!/usr/bin/env python3
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque as queue
#import re
#import argparse
#from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    flow_rates = {}
    adj_list = {}
    for line in data:
        cur = line[0]
        flow = int(line[1])
        edges = line[2:]
        flow_rates[cur] = flow
        adj_list[cur] = set(edges)
        print(f"{cur} has flow {flow} to edges {edges}")
    
    #sort flowrates to find greedy choice
    flow_rates = dict(sorted(flow_rates.items(), key=lambda item: item[1], reverse=True))
    print(flow_rates)
    print(adj_list)

    countdown = 30

    # find valve with most flow, move to that and open valves along the way
    #continue to next highest until countdown is over
    #while(countdown > 0):

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 1

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 

    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    file_name = "./day16s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()
    data = data.split("\n")
    my_file.close()
    
    data = list(map(lambda line: line.replace("Valve ", ""), data))
    data = list(map(lambda line: line.replace("has flow rate=", ""), data))
    data = list(map(lambda line: line.replace(";", ""), data))
    data = list(map(lambda line: line.replace("tunnels lead to valves ", ""), data))
    data = list(map(lambda line: line.replace("tunnel leads to valve ", ""), data))

    data = [line.split(" ") for line in data]
    data = [line for line in data if line != ['']]
    print(data)

    return data

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()


    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()