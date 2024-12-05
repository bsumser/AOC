#!/usr/bin/env python3
import time
import sys
import regex
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    data = [[1,2,3], [4,5,6], [7,8,9]]

    board = saoc.AOC_GRID(data)
    print(board)
    
    #for i in range(3):
    #    print(board.get_row(i))
    #    print(board.get_col(i))

    print(board.get_anti_diag(1,1))
    
    
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    #assert ans == 2358

    #big boy assertion
    #assert ans == 7025140
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
    #assert ans == 1737

    #big boy assertion
    #assert ans == 879274
    return ans

def parse_data():
    start_time = time.time()

    # open file and read in data
    file_name = sys.argv[1]
    print(f"parsing data for {file_name}")
    data = open(file_name, "r").read()
    data = data.split("\n")
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    print(data)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def parse_data_2():
    start_time = time.time()

    # open file and read in data
    file_name = sys.argv[1]
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()
    
    data = data.split("\n")
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    ans1 = 0
    ans2 = 0

    # ---------------Part 1------------------- #
    data = parse_data()
    ans1 = part_1(data)
    # ---------------Part 2------------------- #
    #data2 = parse_data_2()
    ans2 = part_2(data)

    return 0

if __name__ == "__main__":
    main()
