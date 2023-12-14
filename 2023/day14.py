import time
import re
#from scanf import scanf #https://pypi.org/project/scanf/
import math
import numpy as np

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
#from aocd import submit
#from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    #print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    data = rotate_matrix(data)
    for line in data:
        for i in range(len(line)-2, -1, -1):
            if (line[i] == '#' or line[i] == '.'):
                continue
            j = i
            while((j+1 < len(line))):
                if (line[j+1] == 'O'):
                    break
                elif (line[j+1] == '#'):
                    break
                line[j] = '.'
                line[j+1] = 'O'
                j += 1
    # print check
    for line in data:
        print(line)

    print("\n\n")

    data = list(zip(*data))[::-1]
    data = [list(elem) for elem in data]
    for line in data:
        print(line)

    row = len(data) + 1
    for line in data:
        count = 0
        row -= 1
        for char in line:
            if (char == 'O'):
                count += 1
        print("row %d * %d count" % (row, count))
        ans += row * count

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    assert ans == 90982

    return (ans, end_time)

def rotate_matrix(data):
    '''Function that rotates a 2d array clockwise'''
    data = list(zip(*data[::-1]))
    data = [list(elem) for elem in data]

    return data

def part_2(data):
    '''Function that takes data and performs part 2'''
    #print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    cycles = 4 * 1000
    dirs = ["N", "W", "S", "E"]
    score_dict = {}
    for c in range(0, cycles):
        cur_dir = dirs[c % 4]
        #print("at cycle %d rolling %s" % (c, cur_dir))
        cur = 0
        data = rotate_matrix(data)
        for line in data:
            for i in range(len(line)-2, -1, -1):
                if (line[i] == '#' or line[i] == '.'):
                    continue
                j = i
                while((j+1 < len(line))):
                    if (line[j+1] == 'O'):
                        break
                    elif (line[j+1] == '#'):
                        break
                    line[j] = '.'
                    line[j+1] = 'O'
                    j += 1
        row = len(data) + 1
        for line in data:
            count = 0
            row -= 1
            for char in line:
                if (char == 'O'):
                    count += 1
            #print("row %d * %d count" % (row, count))
            cur += row * count
        tup_data = tuple(map(tuple, data))
        if (tup_data in score_dict.keys()):
            print("repeat found at %d last dir %s val is %d" % (c, cur_dir, cur))
            print(score_dict[tup_data])
        else:
            score_dict[tup_data] = c
        ans = cur
        #for line in data:
        #    print(*line, sep='')
        #print("\n\n")
    
    #for line in data:
    #    print(*line, sep='')
    #print("\n\n")
    
    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''

    end_time = time.time() - start_time
    print("Part 2 done in %s seconds" % (end_time))
    print("Part 2 answer is: %d\n" % ans)
    return (ans, end_time)

def parse_data():
    #open file and count lines
    file_name = "./day14.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()


    '''-------------------------------PARSE BLOCK START------------------------------------------'''

    # split on newline
    data = data.split("\n")
    data = [list(line) for line in data]
    
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
