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
    nums = [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]
    #nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    orig_board = data.copy()
    for num in nums:
        print(num)
        for b in range(0, len(data)):
            original = orig_board[b]
            for i in range(0, len(data[b])):
                for j in range(0, len(data[b][i])):
                    if (data[b][i][j] == num and data[b][i][j] > 0):
                        data[b][i][j] = data[b][i][j] * -1
                    elif (data[b][i][j] == num and data[b][i][j] == 0):
                        data[b][i][j] = -69420
                    if (data[b][i][j] == 69420):
                        print("error")
                        print(num)
                        return -1
                    check = check_answer(data[b], original, num)
                    if (check):
                        ans = check
                        print("Part 1 done in %s seconds" % (time.time() - start_time))
                        print("Part 1 answer is: %d\n" % ans)
                        assert ans < 21240
                        return ans

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------''' 
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def check_answer(board, orig_board, num):
    #check rows
    for i in range(0, len(board)):
        if (board[i][0] < 0 and board[i][1] < 0 and board[i][2] < 0 and board[i][3] < 0 and board[i][4] < 0):
            print("row win")
            for row in board:
                print(row)
            sum_list = [val for row in board for val in row if val > 0 and val % 69420 != 0]
            print(sum(sum_list))
            return sum(sum_list) * num


    #check cols
    for j in range(0, len(board)):
        if (board[0][j] < 0 and board[1][j] < 0 and board[2][j] < 0 and board[3][j] < 0 and board[4][j] < 0):
            print("col win")
            for row in board:
                print(row)
            sum_list = [val for row in board for val in row if val > 0 and val % 69420 != 0]
            print(sum(sum_list))
            return sum(sum_list) * num

    #check diag
    #if (board[0][0] < 0 and board[1][1] < 0 and board[2][2] < 0 and board[3][3] < 0 and board[4][4] < 0):
    #    print("diag win LR")
    #    for row in board:
    #        print(row)
    #    sum_list = [val for row in board for val in row if val > 0 and val % 69420 != 0]
    #    print(sum(sum_list))
    #    return sum(sum_list) * num
    #if (board[0][4] < 0 and board[1][3] < 0 and board[2][2] < 0 and board[3][1] < 0 and board[4][0] < 0):
    #    print("diag win RL")
    #    for row in board:
    #        print(row)
    #    sum_list = [val for row in board for val in row if val > 0 and val % 69420 != 0]
    #    print(sum(sum_list), num)
    #    return sum(sum_list) * num

    return 0

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

def parse_data():
    #open file and count lines
    file_name = "./day4.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n\n")

    for i in range(0, len(data)):
        data[i] = data[i].split("\n")
    
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            data[i][j] = data[i][j].strip()
            data[i][j] = data[i][j].replace("  ", " ")
            data[i][j] = data[i][j].split(" ")
    
    for b in range(0, len(data)):
        for i in range(0, len(data[b])):
            for j in range(0, len(data[b][i])):
                data[b][i][j] = int(data[b][i][j])
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