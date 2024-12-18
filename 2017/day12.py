#!/usr/bin/env python3
import time
import random
from collections import deque
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
    node_set = set()
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            node_set.add(data[i][j])

    #init edges to adjacency list
    adj = {}
    for edge in node_set:
        adj[edge] = []
    
    #add edges to adjacency list
    for edge in data:
        for j in range(1, len(edge)):
            adj[edge[0]].append(edge[j])
            adj[edge[j]].append(edge[0])

    ans = bfs(adj, '0')

    assert ans == 288
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def bfs(adj, s):
    q = deque()

    visited = {}
    for i in adj:
        visited[i] = False

    visited[s] = True
    q.append(s)

    while(q):
        curr = q.popleft()

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    ret = sum(visited.values())
    print(ret)

    return ret


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    node_set = set()
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            node_set.add(data[i][j])

    #init edges to adjacency list
    adj = {}
    for edge in node_set:
        adj[edge] = []
    
    #add edges to adjacency list
    for edge in data:
        for j in range(1, len(edge)):
            adj[edge[0]].append(edge[j])
            adj[edge[j]].append(edge[0])

    while(node_set):
        start = random.choice(list(node_set))

        ret_set = bfs_color(adj, start, node_set)

        node_set -= ret_set

        ans += 1

    # off by one error
    ans -= 1
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    #assertion to check that answer is right
    assert ans == 211
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def bfs_color(adj, s, remain_set):
    q = deque()

    visited = {}
    visited_set = set()
    for i in adj:
        visited[i] = False

    visited[s] = True
    visited_set.add(s)
    q.append(s)

    while(q):
        curr = q.popleft()

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                visited_set.add(x)
                q.append(x)

    return visited_set

def parse_data():
    #open file and count lines
    file_name = "./day12.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    data = data[0:len(data) - 1]

    for i in range(0, len(data)):
        data[i] = data[i].replace(" ", "")
        data[i] = data[i].replace("<->", ",")
        data[i] = data[i].split(",")

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
