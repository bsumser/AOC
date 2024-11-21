#!/usr/bin/env python3
import time
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
        node_set.add(data[i][0])
        node_set.add(data[i][1])
    for node in node_set:
        print(node)

    #init edges to adjacency list
    adj_list = {}
    for edge in node_set:
        adj_list[edge] = []
    
    #add edges to adjacency list
    for edge in data:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    print(adj_list)

    dfs(adj_list, 'start', 'end')
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
   
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def dfs_rec(adj, u, d, visited, path):
    visited[u] = True
    path.append(u)

    if u == d:
        print(path)
    else:
        for i in adj[u]:
            if visited[i] == False:
                dfs_rec(adj, i, d, visited, path)
    path.pop()
    visited[u]= False

def dfs(adj, s, d):
    visited = {}
    for i in adj:
        visited[i] = False

    path = []

    print(visited)

    dfs_rec(adj, s, d, visited, path)

def parse_data():
    #open file and count lines
    file_name = "./day12s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    data = [line.split("-") for line in data]
    data = data[0:len(data)-1]

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
