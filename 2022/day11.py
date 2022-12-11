import re
import time
import math
from itertools import groupby
import pyperclip
from collections import defaultdict
from aocd import get_data  # module for automating advent of code data get
import aocFunctions
from collections import namedtuple

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting")
    print(data)
    print(len(data))
    start_time = time.time()
    ans = 0
    i = 0
    monkeys = [[],[],[],[],[],[],[],[],]
    monk_inspect = [0, 0, 0, 0, 0, 0, 0, 0]
    #monkeys = [[],[],[],[]]
    #monk_inspect = [0, 0, 0, 0]

    op = {'+': lambda x, y: x + y,
          '*': lambda x, y: x * y,
          '-': lambda x, y: x - y,
          '/': lambda x, y: x / y}

    superMod = 19 * 5 * 11 * 17 * 7 * 13 * 3 * 2

    for start_index in range(1, len(data), 6):
        for val in data[start_index]:
            monkey_val = int(data[start_index - 1][0])
            print(val)
            monkeys[monkey_val].append(int(val))
    for line in monkeys:
        print(line)


    for monk_round in range(1, 10001, 1):
        for i in range(0, len(data), 6):
            monkey = int(data[i][0])
            cur_monk = monkeys[monkey]
            ops_index = data[i+2]
            test_index = int(data[i+3][0])
            true_index = int(data[i+4][0])
            false_index = int(data[i+5][0])
            cur_monk_copy = cur_monk[:]
            for val in cur_monk_copy:
                #print("MONKEY %d ITEM %d" % (monkey, val))
                monk_inspect[monkey] += 1
                if (ops_index[-1] == "old"):
                    #print("Worry level is %c by %d to %d." % (ops_index[1], val, val))
                    result = op[ops_index[1]](val, val)
                    result = result % superMod
                    if (result % test_index == 0):
                        monkeys[true_index].append(result)
                        cur_monk.remove(val)
                    elif (result % test_index != 0):
                        monkeys[false_index].append(result)
                        cur_monk.remove(val)
                elif (ops_index[-1] != "old"):
                    #print("Worry level is %c by %d to %s." % (ops_index[1], val, int(ops_index[2])))
                    result = op[ops_index[1]](val, int(ops_index[2]))
                    result = result % superMod
                    if (result % test_index == 0):
                        monkeys[true_index].append(result)
                        cur_monk.remove(val)
                    elif (result % test_index != 0):
                        monkeys[false_index].append(result)
                        cur_monk.remove(val)
        #print("ROUND %d END" % (monk_round))
        #print(monkeys)

    monk_inspect.sort(reverse=True)
    print(monk_inspect)
    ans = monk_inspect[0] * monk_inspect[1]
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting")
    start_time = time.time()
    ans = 0



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def parse_data():
    data = get_data(day=11, year=2022)
    #my_file = open("sample.txt", "r")
    #data = my_file.read()
    data = data.split("\n\n")
    #my_file.close()
    data = list(map(lambda line: line.replace("Monkey ", ""), data))
    data = list(map(lambda line: line.replace("  ", " "), data))
    data = list(map(lambda line: line.replace("Starting items", ""), data))
    data = list(map(lambda line: line.replace("Operation: new =", ""), data))
    data = list(map(lambda line: line.replace("Test: divisible by", ""), data))
    data = list(map(lambda line: line.replace("If true: throw to monkey", ""), data))
    data = list(map(lambda line: line.replace("If false: throw to monkey", ""), data))
    data = list(map(lambda line: line.replace(",", ""), data))
    data = list(map(lambda line: line.replace(":", ""), data))
    data = list(map(lambda line: line.replace("  ", " "), data))

    data = [line.split("\n") for line in data]
    data = [val.strip() for line in data for val in line]
    data = [line.split(" ") for line in data]


    for line in data:
        print(line)

    return data

def parse_sample_data():
    #data = get_data(day=11, year=2022)
    with open('sample.txt') as f:
        data = f.readlines()
    f.close()
    data = list(map(lambda line: line.replace("Monkey ", ""), data))
    data = list(map(lambda line: line.replace("  ", " "), data))
    data = list(map(lambda line: line.replace("Starting items", ""), data))
    data = list(map(lambda line: line.replace("Operation: new =", ""), data))
    data = list(map(lambda line: line.replace("Test: divisible by", ""), data))
    data = list(map(lambda line: line.replace("If true: throw to monkey", ""), data))
    data = list(map(lambda line: line.replace("If false: throw to monkey", ""), data))
    data = list(map(lambda line: line.replace(",", ""), data))
    data = list(map(lambda line: line.replace(":", ""), data))
    data = list(map(lambda line: line.replace("  ", " "), data))

    data = [line.split("\n") for line in data]
    data = [val.strip() for line in data for val in line]
    data = [line.split(" ") for line in data]
    data = [ele for ele in data if ele != ['']]
    print(data)

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
