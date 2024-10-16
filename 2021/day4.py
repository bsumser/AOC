#!/usr/bin/env python3
import time
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    #nums = [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]
    nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

    #check_list = [
    #    [1, 1, 0, 1, 1],
    #    [1,1,0,0,0],
    #    [1,0,1,0,0],
    #    [0,0,0,1,0],
    #    [1,0,0,0,1]
    #]

    #bingo_checker(check_list, check_list, 2)
    
    bin_board_list = []
    test_list = [
        [0, 0, 0, 0, 0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    for i in data:
        bin_board_list.append(test_list)

    print(bin_board_list)
    print(data)
    print(len(bin_board_list), len(data))

    for num in nums:
        for g in range(0, len(data)):
            num_board = data[g]
            bin_board = bin_board_list[g] 
            print("checking num %d--------------- " % (num))
            for i in range(0, len(num_board)):
                print(bin_board[i], num_board[i])
            for i in range(0, 5):
                for j in range(0, 5):
                    if (num_board[i][j] == num):
                        bin_board[i][j] = 1
                        print("num found for board--------------- at %d num = %d (%d,%d)" % (num_board[i][j], num, i, j))
                        for i in range(0, len(num_board)):
                            print(bin_board[i], num_board[i])

                        ans = bingo_checker(bin_board, num_board, num)
                        if (ans != 0):
                            print("score found %d" % ans)
                            print("Part 1 done in %s seconds" % (time.time() - start_time))
                            print("Part 1 answer is: %d\n" % ans)
                            return ans



    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def bingo_checker(list1, list2, num):
    length = len(list1)

    print("\tchecking the score for --------------- at num = %d" % (num))
    for i in range(0, len(list1)):
        print("\t", list1[i], list2[i])

    #print("-------------checking rows")
    # check rows
    for i in range(0, length):
        check_sum = sum(list1[i][0:])
        #print(check_sum)
        
        if (check_sum == 5):
            num_sum = 0 
            # check for unmarked values
            for i in range(0, length):
                for j in range(0, length):
                    if (list1[i][j] == 0):
                        num_sum += list2[i][j]
            print(num_sum, num)
            return num_sum * num


    # check columns
    #print("-------------checking cols")
    for col in range(0, length):
        check_sum = sum([row[col] for row in list1])
        #print(check_sum)
        
        if (check_sum == 5):
            num_sum = 0 
            # check for unmarked values
            for i in range(0, length):
                for j in range(0, length):
                    if (list1[i][j] == 0):
                        num_sum += list2[i][j]
            print(num_sum, num)
            return num_sum * num

    return 0

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0
    
    nums = [69,88,67,56,53,97,46,29,37,51,3,93,92,78,41,22,45,66,13,82,2,7,52,40,18,70,32,95,89,64,84,68,83,26,43,0,61,36,57,34,80,39,6,63,72,98,21,54,23,28,65,16,76,11,20,33,96,4,10,25,30,19,90,24,55,91,15,8,71,99,58,14,60,48,44,17,47,85,74,87,86,27,42,38,81,79,94,73,12,5,77,35,9,62,50,31,49,59,75,1]


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day4s.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n\n")
    data = [line.strip("\n") for line in data]
    data = [line.split("\n") for line in data]
    data = [word.split() for line in data for word in line]
    #data = [line.replace(" ", "") for line in data]
    #data = data.split(",")
    #data = [re.split(r"([A-Z])",line) for line in data]
    #data = [val for sublist in data for val in sublist if val]

    boards = []
    for i in range(0, len(data), 5):
        curBoard = [data[i],data[i+1],data[i+2],data[i+3],data[i+4]]
        # convert to int
        curBoard = [list( map(int,i) ) for i in curBoard]
        boards.append(curBoard)


    print(boards[0])
    print(len(boards))
    return boards


def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    #ans2 = part_2(data2)


    return 0
main()
