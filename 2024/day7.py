#!/usr/bin/env python3
import time
import sys
import re
sys.path.append('../')
import saoc
from functools import reduce
import operator
from itertools import product

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
    def __repr__(self):
        return f"Node(val='{self.val}', children={self.children})"

def part_1(data):
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    for line in data:
        cur = line[1:]
        cur_sum = sum(cur)
        cur_prod = reduce(operator.mul, cur)
        if cur_sum == line[0] or cur_prod == line[0]:
            ans += line[0]
        else:
            if calibrate(line):
                ans += line[0]

    print("Part 1 answer is: %d\n" % ans)
    return ans

def silver(data):
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    #1. Create a graph of all possible combination of operators. 
    #2. DFS through the graph and test each combination until we get the sum. 
    #Part 2 was exactly the same except with one extra operator.
    #for line in data:
    #    create_graph(line[1:])
    
    root = create_graph([1,2,3])
    print_tree(root)

    print("Part 1 answer is: %d\n" % ans)
    return ans

def create_graph(line):
    #create graph for all combinations of operators
    
    def build_tree(node, index):
        if index >= len(line):
            return
        next_val = line[index]

        add_node = Node(node.val + next_val)
        node.children.append(add_node)
            
        mul_node = Node(node.val * next_val)
        node.children.append(mul_node)

        build_tree(add_node, index+1)
        build_tree(mul_node, index+1)

    root = Node(line[0])

    build_tree(root, 1)

    print(f"graph for{root}")
    return root

def print_tree(root):
    if root:
        print(root.val)
        for child in root.children:
            print_tree(child)

def calibrate(line):
    print(f"checking {line}")
    length = len(line) - 1
    ops = ['+', '*']
    combs = [''.join(x) for x in product(ops, repeat = length)]
   
    
    for comb in combs:
        cur_op = 1
        init_val = line[1]
        while(cur_op < len(line) - 1):
            if (comb[cur_op] == '+'):
                init_val += line[cur_op+1]
            elif (comb[cur_op] == '*'):
                init_val *= line[cur_op+1]
            cur_op += 1
        if (init_val == line[0]):
            print(f"win comb is {comb}")
            print(init_val)
            return True
    return False
    

def part_2(data):
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    for line in data:
        cur = line[1:]
        cur_sum = sum(cur)
        cur_prod = reduce(operator.mul, cur)
        if cur_sum == line[0] or cur_prod == line[0]:
            ans += line[0]
        else:
            if calibrate_2(line):
                ans += line[0]
    print("Part 2 answer is: %d\n" % ans)
    return ans

def calibrate_2(line):
    length = len(line) - 1
    ops = ['+', '*', '|']
    combs = [''.join(x) for x in product(ops, repeat = length)]
   
    for comb in combs:
        cur_op = 1
        init_val = line[1]
        while(cur_op < len(line) - 1):
            if (comb[cur_op] == '+'):
                init_val += line[cur_op+1]
            elif (comb[cur_op] == '*'):
                init_val *= line[cur_op+1]
            elif (comb[cur_op] == '|'):
                init_val = int(str(init_val) + str(line[cur_op+1]))
            cur_op += 1
        if (init_val == line[0]):
            print(init_val)
            return True
    return False

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n")
    data = [re.findall(r'\d+', line) for line in data]
    data = [line for line in data if line]
    data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    silver(parse_data())
    # ---------------Part 2------------------- #
    part_2(parse_data())

    return 0

if __name__ == "__main__":
    main()
