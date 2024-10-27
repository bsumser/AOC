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
    check_list = [ [0, -1], [0, 1], [-1, 0], [1, 0]]
    lows = []

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            check = True
            neighbors = []
            for coord in check_list:
                i_1 = i + coord[0]
                j_1 = j + coord[1]
                if ( 0 <= i_1 <= len(data) - 1 and 0 <= j_1 <= len(data[i]) - 1):
                    #print("valid at %d %d" % (i_1, j_1))
                    if (data[i][j] < data[i_1][j_1]):
                        neighbors.append(data[i][j])
                    else:
                        check = False
            if (check):
                #print("low of %d with neighbors %s" % (data[i][j], neighbors))
                lows.append(data[i][j])
    ans = sum(lows) + len(lows)

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
    check_list = [ [0, -1], [0, 1], [-1, 0], [1, 0]]
    lows = []

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            check = True
            neighbors = []
            for coord in check_list:
                i_1 = i + coord[0]
                j_1 = j + coord[1]
                if ( 0 <= i_1 <= len(data) - 1 and 0 <= j_1 <= len(data[i]) - 1):
                    #print("valid at %d %d" % (i_1, j_1))
                    if (data[i][j] < data[i_1][j_1]):
                        neighbors.append(data[i][j])
                    else:
                        check = False
            if (check):
                #print("low of %d with neighbors %s" % (data[i][j], neighbors))
                lows.append([i,j])
    print("low points are:")
    print(lows)

    # every low point is a sink.
    # find how big the network around it is
    # graph algorithms
    G = nx.Graph()
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            check = True
            neighbors = []
            for coord in check_list:
                i_1 = i + coord[0]
                j_1 = j + coord[1]
                if ( ( 0 <= i_1 <= len(data) - 1 and 0 <= j_1 <= len(data[i]) - 1) and ( data[i][j] > data[i_1][j_1]) and data[i_1][j_1] != 9):
                    start = f"{data[i][j]} {i},{j}"
                    end = f"{data[i_1][j_1]} {i_1},{j_1}"
                    G.add_edge(start, end)
    options = {
        'node_color': 'blue',
        'node_size': 300,
        'width': 3,
        'arrowstyle': '-|>',
        'arrowsize': 2,
    }
    nx.draw_networkx(G, arrows=True, **options)
    plt.savefig('plotgraph.png')

    vis = [[ False for i in range(len(data[0]))] for i in range(len(data))]

    basins = []
    for low in lows:
        basins.append(BFS(data, vis, low[0], low[1]))

    basins.sort(reverse=True)
    print(basins)

    ans = (basins[0] * basins[1] * basins[2])

    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 

    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans


def BFS(grid, vis, row, col):
    print("BFS on %d at %d,%d" % (grid[row][col], row, col))
    check_list = [ [0, -1], [0, 1], [-1, 0], [1, 0]]
    basin_count = set()
    q = queue()

    q.append((row, col))
    vis[row][col] = True

    while(len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")

        for coord in check_list:
            adjx = x + coord[0]
            adjy = y + coord[1]
            
            if ( ( 0 <= adjx <= len(grid) - 1 and 0 <= adjy <= len(grid[0]) - 1) and ( grid[x][y] < grid[adjx][adjy]) and (grid[adjx][adjy] != 9)):
                q.append((adjx, adjy))
                basin_count.add( (grid[adjx][adjy], adjx, adjy) )
                vis[adjx][adjy] = True
    print("BFS on %d at %d,%d done count = %d" % (grid[row][col], row, col, len(basin_count)))

    return(len(basin_count) + 1)

    
def parse_data():
    #open file and count lines
    file_name = "./day9s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    for i in range(0, len(data)):
        data[i] = list(data[i])
        for j in range(0, len(data[i])):
            data[i][j] = int(data[i][j])

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