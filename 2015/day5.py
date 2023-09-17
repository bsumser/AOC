#!/usr/bin/env python3
import time
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get
#import aocFunctions

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    print(data)
    start_time = time.time()

    no_string = ['ab', 'cd', 'pq', 'xy']
    vowels = 'aeiou'

    for i in range(0, len(data)):
        print(data[i])
        vowel_count = 0
        double_flag = -1
        duo_flag = 1
        for j in range(0, len(data[i])):
            if data[i][j] in vowels:
                vowel_count += 1
            if (j+1 < len(data[i])) and data[i][j] == data[i][j+1]:
                print("%s double in string %s" % (data[i][j], data[i]))
                double_flag = 1
        for duo in no_string:
            if duo in data[i]:
                print("%s contains duo %s" % (data[i], duo))
                duo_flag = -1
                break
        if duo_flag == 1 and vowel_count >= 3 and double_flag == 1:
            ans += 1



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d" % ans)
    return ans

def parse_data():
    my_file = open("./day5.txt", "r")
    data = my_file.read()
    my_file.close()
    data = data.strip("\n\n")
    data = data.split("\n")
    #data = [x.split("x") for x in data]
    #data = [int(num) for row in data for num in row]


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


    print(ans1)
    print(ans2)
    #pyperclip.copy(ans2)
    return 0
main()
