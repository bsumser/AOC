#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

#create ppm file header, P3, length and width, color scale max value
def get_header(height, width, f):
    ppm = 'P3\n{} {}\n255\n'.format(width, height)
    f.write(ppm)
    return f

def write_image(grid, height, width, f):
    """Function to write an image file in ppm format

    """

    for row in range(height):
        for col in range(width):
            if (grid[row][col] == 0):
                f.write("255 255 255 ")
            elif (grid[row][col] == 1):
                f.write("255 243 59 ")
            elif (grid[row][col] == 2):
                f.write("243 144 63 ")
            elif (grid[row][col] >= 2):
                f.write("233 62 58 ")
            f.write('\n')

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    grid = [ [0]*1000 for i in range(1000)]

    for line in range(0, len(data)):
        x1 = min(data[line][0], data[line][2])
        x2 = max(data[line][0], data[line][2])
        y1 = min(data[line][1], data[line][3])
        y2 = max(data[line][1], data[line][3])

        print("line is: %d,%d to %d,%d" % (x1, y1, x2, y2))
        
        # x coord is the same
        if (x1 == x2):
            for row in range(y1, y2+1):
                grid[row][x1] += 1
            
        # y coord is the same
        elif (y1 == y2):
            for col in range(x1, x2+1):
                grid[y1][col] += 1

    for line in grid:
        print(*line, sep='')
    print("\n\n")

    ans = sum(val > 1 for line in grid for val in line)

    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0
    
    

    grid = [ [0]*1000 for i in range(1000)]

    for line in range(0, len(data)):
        x1 = data[line][0]
        x2 = data[line][2]
        y1 = data[line][1]
        y2 = data[line][3]

        coords = []

        print("line is: %d,%d to %d,%d" % (x1, y1, x2, y2))

        if (x1 != x2 and y1 != y2):
            if (y1 < y2 and x1 < x2):
                print("top-left bot-right diag")
                y_list = [i for i in range (y1, y2+1)]
                x_list = [i for i in range(x1, x2+1)]
                coords = tuple(zip(x_list, y_list))
                print(coords)
            elif (y1 > y2 and x1 > x2):
                print("top-left bot-right diag")
                y_list = [i for i in range (y2, y1+1)]
                x_list = [i for i in range(x2, x1+1)]
                coords = tuple(zip(x_list, y_list))
                print(coords)

            elif (y1 > y2 and x1 < x2):
                print("bot-left top-right diag")
                y_list = [i for i in range (y1, y2-1, -1)]
                x_list = [i for i in range(x1, x2+1)]
                coords = tuple(zip(x_list, y_list))
                print(coords)

            elif (y1 < y2 and x1 > x2):
                print("bot-left top-right diag")
                y_list = [i for i in range (y1, y2+1)]
                x_list = [i for i in range(x1, x2-1, -1)]
                coords = tuple(zip(x_list, y_list))
                print(coords)
            else:
                print("diag case missed")

        elif (x1 == x2 and y1 < y2):
            y_list = [i for i in range (y1, y2+1)]
            x_list = [x1 for i in range(0, len(y_list))]
            coords = tuple(zip(x_list, y_list))
            print("case 1")
            print(coords)

        elif (x1 == x2 and y1 > y2):
            y_list = [i for i in range (y2, y1+1)]
            x_list = [x1 for i in range (0, len(y_list))]
            coords = tuple(zip(x_list, y_list))
            print("case 2")
            print(coords)

        elif (y1 == y2 and x1 < x2):
            x_list = [i for i in range (x1, x2+1)]
            y_list = [y1 for i in range(0, len(x_list))]
            coords = tuple(zip(x_list, y_list))
            print("case 3")
            print(coords)

        elif (y1 == y2 and x1 > x2):
            x_list = [i for i in range (x2, x1+1)]
            y_list = [y1 for i in range(0, len(x_list))]
            coords = tuple(zip(x_list, y_list))
            print("case 4")
            print(coords)

        for coord in coords:
            grid[coord[1]][coord[0]] += 1

        #name = "frame_" + str(line) + ".ppm"
        #f = open(name, 'w')
        #get_header(1000, 1000, f)
        #write_image(grid, 1000, 1000, f)

    ans = sum(val > 1 for line in grid for val in line)

    #for line in grid:
    #    print(*line, sep='')
    #print("\n\n")



    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day5.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.split("\n")
    #data = data.replace(" ", "")
    #data = data.split(",")
    data = [line.split(",") for line in data]
    data = ([list(map(int, i) ) for i in data])


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
