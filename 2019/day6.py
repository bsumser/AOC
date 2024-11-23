#!/usr/bin/env python3
import time
import random
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
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

    #init edges to adjacency list
    adj = {}
    for edge in node_set:
        adj[edge] = []
    
    #add edges to adjacency list
    for edge in data:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    print(adj)
    node_list = list(node_set)
    print(node_list)

    for i in range(0, len(node_list)):
        if (node_list[i] == 'COM'):
            print("COMMY")
            continue
        print(f"hop from {node_list[i]} to 'COM'")
        hop = dfs(adj, node_list[i], 'COM')

        if (hop):
            ans += hop - 1

    #assert ans == 288
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def dfs_rec(adj, u, d, visited, count):
    visited[u] = True
    count += 1

    if u == d:
        print(count)
        return count
    else:
        for i in adj[u]:
            if visited[i] == False:
                return dfs_rec(adj, i, d, visited, count)

def dfs(adj, s, d):
    visited = {}
    for i in adj:
        visited[i] = False

    return dfs_rec(adj, s, d, visited, 0)

def draw_graph(adj):
    G = nx.Graph()
    for node, neighbors in adj.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    #assertion to check that answer is right
    #assert ans == 211
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    file_name = "./day6s.txt"
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
        data[i] = data[i].split(")")

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
