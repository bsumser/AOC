#!/usr/bin/env python3
import math
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

class Node:
    def __init__(self, code):
        self.code = code
        self.root = True
        self.children = []
    def __repr__(self):
        return f"Node(code='{self.code}', children={self.children})"

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    orbit_graph = {}
    for left, right in data:
        if left not in orbit_graph:
            orbit_graph[left] = Node(left)
        if right not in orbit_graph:
            orbit_graph[right] = Node(right)
        orbit_graph[right].root = False
        orbit_graph[left].children.append(orbit_graph[right])
        orbit_graph[right].children.append(orbit_graph[left])

    for node in orbit_graph:
        print(repr(orbit_graph[node]))

    ans = counter(orbit_graph)

    #assert ans == 288
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def counter(graph):
    seen = set()

    def _traverse(node, depth=0):
        if node.code in seen:
            return 0
        seen.add(node.code)
        return depth + sum(_traverse(child, depth+1) for child in node.children)
    return sum(_traverse(node) for node in graph.values() if node.root)

def dfs_rec(orbit_graph, u, d, visited, count):
    visited.add(u)
    count += 1

    print(f"added {u}, visited is {visited}, count is {count}")

    if u == d:
        print(count)
        return count
    else:
        for i in orbit_graph[u].children:
            for child in orbit_graph[u].children:
                print(child.code)
            if i.code not in visited:
                print(f"recur on {i.code}")
                return dfs_rec(orbit_graph, i.code, d, visited, count)

def bfs(orbit_graph, s, d):
    q = deque()

    dist = {}
    par = []
    dist[s] = 0
    for i in orbit_graph:
        dist[i.code] = math.inf
        par[i.code] = None

    q.append(s)
    
    while(q):
        curr = q.popleft()
        print(f"curr is {curr} que is {q}, visited is {visited}, count is {count}")

        for x in orbit_graph[curr].children:
            if dist[x.code] == math.inf:
                par[x.code] = curr
                dist[x.code] = dist[x.code]
                q.append(x.code)

    return -1

def dfs(orbit_graph, s, d):
    visited = set()
    return dfs_rec(orbit_graph, s, d, visited, 0)

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
    orbit_graph = {}
    for left, right in data:
        if left not in orbit_graph:
            orbit_graph[left] = Node(left)
        if right not in orbit_graph:
            orbit_graph[right] = Node(right)
        orbit_graph[right].root = False
        orbit_graph[left].children.append(orbit_graph[right])
        orbit_graph[right].children.append(orbit_graph[left])

    for node in orbit_graph:
        print(repr(node))

    ans = bfs(orbit_graph, 'YOU', 'SAN')
    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    #assertion to check that answer is right
    #assert ans == 211
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def parse_data():
    #open file and count lines
    file_name = "./day6s2.txt"
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
