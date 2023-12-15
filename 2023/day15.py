import time
import re
from scanf import scanf #https://pypi.org/project/scanf/
import math
import numpy as np

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
from aocd import submit
from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    for line in data:
        cur = 0
        for char in line:
            cur += (ord(char))
            cur *= 17
            cur %= 256
        print(cur)
        ans += cur


    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    boxes = [[] for i in range(255)]
    print(len(boxes))
    print(boxes)
    for line in data:
        box_idx = 0
        if ('=' in line):
            hash_val, num = line.split("=")
        elif ('-' in line):
            hash_val = line.strip("-")
        for char in hash_val:
            box_idx += (ord(char))
            box_idx *= 17
            box_idx %= 256
        cur_box = boxes[box_idx]
        if (len(line) == 4):
            ins, val = hash_val, int(num)
            print("add %s val %d idx %d" % (ins, val, box_idx))
            if (cur_box == []):
                cur_box.append((ins,val))
            elif (bool([lens for lens in cur_box if lens[0] == ins])):
                for i in range(0, len(cur_box)):
                    if (cur_box[i][0] == ins):
                        cur_box[i] = (ins, val)
            else:
                cur_box.append((ins, val))
        elif (len(line) == 3):
            ins = hash_val
            print("remove %s idx %s" % (ins, box_idx))
            print("\t%s" % cur_box)
            if (cur_box == []):
                continue
            else:
                for i in range(0, len(cur_box)):
                    if (cur_box[i][0] == ins):
                        cur_box.pop(i)
                        break
            print("\t%s" % cur_box)
        boxes[box_idx] = cur_box
        print("\n\n")
        for i in range(0, len(boxes)):
            if (boxes[i] != []):
                print(boxes[i], i)
        
    for i in range(0, len(boxes)):
        if (boxes[i] != []):
            for j in range(0, len(boxes[i])):
                ans += ((i+1) * (j+1) * boxes[i][j][1])
                    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''

    end_time = time.time() - start_time
    print("Part 2 done in %s seconds" % (end_time))
    print("Part 2 answer is: %d\n" % ans)
    assert ans == 247933
    return (ans, end_time)

def parse_data():
    #open file and count lines
    file_name = "./day15.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()


    '''-------------------------------PARSE BLOCK START------------------------------------------'''

    # split on newline
    data = data.split(",")
    
    #for i in range(0, len(data)):
    #    data[i] = list(map(int, data[i]))
    
    # convert to 2d array on every char
    #data = [list(line) for line in data]

    #filter out letters and leave only numbers
    # data = [''.join(filter(str.isdigit, val)) for val in data]

    # split on comma
    #data = data.split(",")

    # scanf for specific pattern
    #pattern = 'Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d'
    #data = [scanf(pattern, line) for line in data]

    # remove spaces
    #data = data.replace(" ", "")

    # regex
    #data = [re.split(r"([A-Z])",line) for line in data]

    # double list comp
    #data = [val for sublist in data for val in sublist if val]
    '''-------------------------------PARSE BLOCK END--------------------------------------------'''

    # print check
    for line in data:
        print(line)
    return data

def check_answer(answer):
    choice = input("ANSWER IS %d; DO YOU WISH TO SUBMIT (y/n)?\n" % (answer))

    if (choice == 'y'):
        try:
            print(submit(answer))
            print("submitted")
        except:
            print("answer is wrong")
        return 0
    else:
        return 0

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data()

    # ---------------Part 1------------------- #
    ans1, part1time = part_1(data1)
    # ---------------Part 2------------------- #
    ans2, part2time = part_2(data2)


    #check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
