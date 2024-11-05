#!/usr/bin/env python3
import time
import re
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
    adj_list = {}
    ready_list = {}
    node_set = set()

    #init edges to adjacency list
    for edge in data:
        node_set.add(edge[0])
        node_set.add(edge[1])
        adj_list[edge[0]] = []
        ready_list[edge[1]] = []
    
    #add edges to adjacency list
    for edge in data:
        adj_list[edge[0]].append(edge[1])
        ready_list[edge[1]].append(edge[0])

    # find nodes with no incoming edges
    for key, value in adj_list.items():
        for entry in value:
            if (entry in node_set):
                node_set.remove(entry)
    #print(adj_list)
    #print(ready_list)

    #breadth first search
    starts = list(node_set)
    starts.sort(reverse=True)
    visited = set()
    order = []

    while(starts):
        cur = starts.pop()
        #print(f"cur is {cur}")
        visited.add(cur)
        order.append(cur)

        if (cur in adj_list):
            for val in adj_list[cur]:
                if (set(ready_list[val]).issubset(visited)):
                    starts.append(val)
        starts.sort(reverse=True)


    ans = "".join(order)

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %s\n" % ans)
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    adj_list = {}
    ready_list = {}
    node_set = set()

    #init edges to adjacency list
    for edge in data:
        node_set.add(edge[0])
        node_set.add(edge[1])
        adj_list[edge[0]] = []
        ready_list[edge[1]] = []
    
    #dictionary for all work times
    time_set = {}
    for node in node_set:
        time_set[node] = (ord(node) - 64)
    
    #add edges to adjacency list
    for edge in data:
        adj_list[edge[0]].append(edge[1])
        ready_list[edge[1]].append(edge[0])

    # find nodes with no incoming edges
    for key, value in adj_list.items():
        for entry in value:
            if (entry in node_set):
                node_set.remove(entry)

    #breadth first search kinda
    starts = list(node_set)
    starts.sort(reverse=True)
    print(f"starts {starts}")
    visited = set()
    order = []
    workers = [0, 0]
    print(time_set)

    # while nodes need to be procssed
    while(starts):

        # while there are ready nodes and open workers
        # assign all open workers
        while(starts and 0 in workers):
            if (starts[-1] not in ready_list.keys() or set(ready_list[starts[-1]]).issubset(visited)):
                for i in range(0, len(workers)):
                    if workers[i] == 0:
                        print(f"{starts[-1]} ready")
                        cur = starts.pop()
                        workers[i] = time_set[cur]
                        print(f"workers are {workers}")
                        visited.add(cur)
                        order.append(cur)

            # decrease worker time until job done
            while(0 not in workers):
                workers = [worker - 1 for worker in workers]
            print(workers)

            if (cur in adj_list):
                for val in adj_list[cur]:
                    if (set(ready_list[val]).issubset(visited)):
                        starts.append(val)
                        print(f"{val} {ready_list[val]} ready")
            starts.sort(reverse=True)
            return "done"

    print(f"order {order}")

    ans = "".join(order)
    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %s\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    file_name = "./day7s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    #print(data)
    data = data.split("\n")
    data = [line for line in data if line]
    for i in range(0, len(data)):
        cur = str(data[i])
        #print(len(cur))
        data[i] = [cur[5], cur[36]]
    #print(data)
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
