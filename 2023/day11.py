import time
import re
#from scanf import scanf #https://pypi.org/project/scanf/
import math
import sys
sys.setrecursionlimit(20000)

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
    graph = {}
    galaxies = {}
    galaxy_num = 1
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if (data[i][j] == '#'):
                galaxies[galaxy_num] = (i,j)
                galaxy_num += 1
            check_coord_neighbors((i,j), data, graph)
            connects = check_coord_neighbors( [i, j], data, graph)
            print("coord checker prints")
            print(connects)
            graph[(i,j)] = connects
    print(galaxies)
    print(graph)

    dist = abs(galaxies[5][0] - galaxies[9][0]) + abs(galaxies[5][1] - galaxies[9][1])
    print(dist)

    for val in galaxies.values():
        for val2 in galaxies.values():
            if (val == val2):
                continue
            else:
                print(val, val2)
                ans += abs(val[0] - val2[0]) + abs(val[1] - val2[1])
            print(val, val2)
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)


def part_2(data):
    '''Function that takes data and performs part 2'''
    #print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0


    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''

    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''

    end_time = time.time() - start_time
    print("Part 2 done in %s seconds" % (end_time))
    print("Part 2 answer is: %d\n" % ans)
    return (ans, end_time)

def check_coord_neighbors(input_coord, data, graph):
    """Function to check all neighbors of an input coordinate

    """
    coords = [(0, 1), (-1, 0), (1, 0), (0, -1)]

    num_rows = len(data) - 1
    num_cols = len(data[0]) - 1
    
    connections = []
    for k in range(0, len(coords)):
        coord = coords[k]
        row = input_coord[0] + coord[0]
        col = input_coord[1] + coord[1]
        if (0 <= row <= num_rows and 0 <= col <= num_cols):
            print("coord is %s, neighbor is %s" % (input_coord, [row, col]))
            connections.append((row, col))
            print(connections)
    return connections

def parse_data():
    #open file and count lines
    file_name = "./day11s.txt"
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
    #ans2, part2time = part_2(data2)


    #check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
