#!/usr/bin/env python3
import time
import re
import argparse
from functools import reduce
#import pyperclip
#from aocd import get_data  # module for automating advent of code data get

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()
    
    #--------------------------------SETUP IMAGE VALUES-----------------------------------#
    image_size = 300
    offset = 50
    grid = [ [0]*image_size for i in range(image_size)]
    frame_num = 0
    #-------------------------------SETUP IMAGE VALUES------------------------------------#

    head = "N"
    headNum = 0
    headings = ["N", "E", "S", "W"]

    x = 0
    y = 0

    s = {(0,0)}

    for i in range(0, len(data) - 1, 2):
        turn = 1 if data[i] == "R" else -1
        move = int(data[i+1])
        headNum += turn

        head = headings[headNum % 4]

        for i in range(0, move):
            if head == 'N':
                y += 1
            elif head == 'E':
                x += 1
            elif head == 'S':
                y -= 1
            elif head == 'W':
                x -= 1
            print("turn %s %d move to move %d blocks %s, %d blocks from start" %
                  (data[i], turn, move, head, abs(x) + abs(y)))
            #-------------------------------WRITE IMAGE OF GRID-----------------------------------#
            grid[y+offset][x+offset] += 1
            name = "frame_" + str(frame_num) + ".ppm"
            f = open(name, 'w')
            get_header(image_size, image_size, f)
            write_image(grid, image_size, image_size, f, x+offset, y+offset)
            frame_num += 1
            #------------------------------------------------------------------------------------#

    print(x,y)
    ans = abs(x) + abs(y)


    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    #--------------------------------SETUP IMAGE VALUES-----------------------------------#
    image_size = 300
    offset = 50
    grid = [ [0]*image_size for i in range(image_size)]
    frame_num = 0
    #-------------------------------SETUP IMAGE VALUES------------------------------------#

    head = "N"
    headNum = 0
    headings = ["N", "E", "S", "W"]

    x = 0
    y = 0

    s = {(0,0)}

    for i in range(0, len(data) - 1, 2):
        turn = 1 if data[i] == "R" else -1
        move = int(data[i+1])
        headNum += turn

        head = headings[headNum % 4]


        # you originally only counted the intersections you turned at into the set,
        # instead of every intersection you passed between turns

        for i in range(0, move):
            if head == 'N':
                y += 1
            elif head == 'E':
                x += 1
            elif head == 'S':
                y -= 1
            elif head == 'W':
                x -= 1
            #print("turn %s %d move to move %d blocks %s, %d blocks from start, heading is %c" %
            #      (data[i], turn, move, head, abs(x) + abs(y), head))
            #print("writing image pixel at: %d %d" % (y+offset, x+offset))
            
            #-------------------------------WRITE IMAGE OF GRID-----------------------------------#
            grid[y+offset][x+offset] += 1
            name = "frame_" + str(frame_num) + ".ppm"
            f = open(name, 'w')
            get_header(image_size, image_size, f)
            write_image(grid, image_size, image_size, f, x+offset, y+offset)
            frame_num += 1
            #------------------------------------------------------------------------------------#
            
            if ( (x,y) not in s):
                s.add( (x,y) )
            else:
                break;

    print(x,y)
    ans = abs(x) + abs(y)

    print(s)
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

#create ppm file header, P3, length and width, color scale max value
def get_header(height, width, f):
    ppm = 'P3\n{} {}\n255\n'.format(width, height)
    f.write(ppm)
    return f

def write_image(grid, height, width, f, x, y):
    """Function to write an image file in ppm format

    """

    for row in range(height):
        for col in range(width):
            if (row == y and col == x):
                f.write("0 0 0")
            elif (grid[row][col] == 0):
                f.write("255 255 255")
            elif (grid[row][col] == 1):
                f.write("128 128 128")
            else:
                f.write("128 128 128")
            f.write('\n')

def parse_data():
    #open file and count lines
    file_name = "./day1.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()

    #parse data
    data = data.strip("\n")
    data = data.replace(" ", "")
    data = data.split(",")
    data = [re.split(r"([A-Z])",line) for line in data]
    data = [val for sublist in data for val in sublist if val]

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
    #ans2 = part_2(data2)


    #pyperclip.copy(ans2)
    return 0
main()
