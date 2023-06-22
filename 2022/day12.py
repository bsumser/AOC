import re
import time
import math
import pyperclip
from aocd import get_data  # module for automating advent of code data get
import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    print(data)
    print(len(data))
    start_time = time.time()
    ans = 0
    start_i, start_j = 0,0
    cur_i, cur_j = 0,0
    end_i, end_j = 0,0
    open_list = []
    closed_list = []

    for i in range(0, len(data) - 1, 1):
        for j in range(0, len(data[0]) - 1, 1):
            if data[i][j] == "S":
                start_i = i
                start_j = j
            elif data[i][j] == "E":
                end_i = i
                end_j = j
    open_list.append([start_i, start_j])
    print(open_list)
    while (open_list):
        cur_i, cur_j = open_list[0][0], open_list[0][1]
        closed_list.append(open_list.pop())
        if (cur_i == end_i and cur_j == end_j):
            break
        neighbor_nodes = get_nodes(cur_i, cur_j, data)

        for node in neighbor_nodes:
            # check node is within range
            if (node[1] > len(data) - 1 or node[1] < 0 or node[1] > len(data[0]) - 1 or node[1] < 0):
                continue
            for sub_node in closed_list:
                if node == sub_node:
                    continue
            i, j = sub_node[0], sub_node[1]
            node_g = cost_function(data[i][j])
            node_h = abs(end_i-i) + abs(end_j-j)
            node_f = node_g + node_h

            if node in open_list:
                open_g = cost_function(data[node[0]][node[1]])
                if node_g > open_g:
                    continue
            open_list.append(node)

    print(start_i)
    print(start_j)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans


def cost_function(char):
    cost = ord(char) - 96
    return cost

def get_nodes(cur_i, cur_j, data):
    neighbor_nodes = []

    i = cur_i
    j = cur_j

    neighbor_nodes.append([i,j+1])
    neighbor_nodes.append([i,j-1])
    neighbor_nodes.append([i+1,j])
    neighbor_nodes.append([i-1,j])
    return neighbor_nodes

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def parse_data():
    #data = get_data(day=11, year=2022)
    my_file = open("sample.txt", "r")
    data = my_file.read()
    data = data.split("\n")
    my_file.close()

    #data = [line.split("\n") for line in data]
    #data = [val.strip() for line in data for val in line]
    data = [[*line] for line in data]
    data = [line for line in data if line != []]


    for line in data:
        print(line)

    return data

def main():
    ans = 0
    data1 = parse_data()
    #data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    #ans2 = part_2(data2)

    #total_ans = str(ans1) + str(ans2)

    print(ans)
    pyperclip.copy(ans1)
    return 0
main()
