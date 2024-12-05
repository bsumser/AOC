#!/usr/bin/env python3
import time
import sys
import regex
from functools import reduce
from operator import add, mul
from aocd import get_data  # module for automating advent of code data
from aocd import submit
import numpy as np

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    rows_checked = set()
    cols_checked = set()
    diags_checked = set()
    anti_diags_checked = set()
    ans = 0

    # Process rows in the outer loop
    for row in range(len(data)):
        # Check the row only once
        cur_row = "".join(data[row])
        matches = regex.findall(r'(?=(XMAS|SAMX))', cur_row, overlapped=True)  # Overlapping matches
        ans += len(matches)
        rows_checked.add(row)

        # Process each column in the row
        for col in range(len(data[row])):
            if data[row][col] == "X":
                # Check the column
                if col not in cols_checked:
                    cur_col = "".join(data[i][col] for i in range(len(data)))
                    matches = regex.findall(r'(?=(XMAS|SAMX))', cur_col, overlapped=True)
                    ans += len(matches)
                    cols_checked.add(col)

                # Check main diagonal (top-left to bottom-right)
                if (row, col) not in diags_checked:
                    diag = []
                    r, c = row, col
                    while r < len(data) and c < len(data[0]):
                        diag.append(data[r][c])
                        diags_checked.add((r, c))
                        r += 1
                        c += 1
                    diag = "".join(diag)
                    matches = regex.findall(r'(?=(XMAS|SAMX))', diag, overlapped=True)
                    ans += len(matches)

                # Check anti-diagonal (top-right to bottom-left)
                if (row, col) not in anti_diags_checked:
                    anti_diag = []
                    r, c = row, col
                    while r < len(data) and c >= 0:
                        anti_diag.append(data[r][c])
                        anti_diags_checked.add((r, c))
                        r += 1
                        c -= 1
                    anti_diag = "".join(anti_diag)
                    matches = regex.findall(r'(?=(XMAS|SAMX))', anti_diag, overlapped=True)
                    ans += len(matches)

    print(f"Total matches: {ans}")


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
    for row in range(1, len(data) - 2):
        for col in range(1, len(data[0]) - 2):
            if (data[row][col] == "A"):
                diag1 = "" + data[row-1][col-1] + data[row][col] + data[row+1][col+1]
    
                diag2 = "" + data[row-1][col+1] + data[row][col] + data[row+1][col-1]

                if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                    ans += 1
    


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
    file_name = "./day4bigboy.txt"
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()
    
    #data = get_data(day=4, year=2024)

    data = data.replace("\n\n", "\n")
    data = data.split("\n")
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]


    # fix ragged array
    print(f"{len(data)} x {len(data[0])}")
    num_cols = 0
    for line in data:
        if len(line) != 15001:
            line.append("F")
    for line in data:
        if len(line) != 15001:
            print("ragged")
    print(f"{len(data)} x {len(data[0])}")


    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def parse_data_2():
    start_time = time.time()

    # open file and read in data
    #file_name = "./day4.txt"
    #print(f"parsing data for {file_name}")
    #my_file = open(file_name, "r")
    #data = my_file.read()
    #my_file.close()
    
    data = get_data(day=4, year=2024)

    data = data.split("\n")
    
    for line in data:
        print(data)

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    ans1 = 0
    ans2 = 0

    # ---------------Part 1------------------- #
    data1 = parse_data()
    #ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    #data2 = parse_data()
    ans2 = part_2(data1)

    return 0

if __name__ == "__main__":
    main()
