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
    dots = list("." * len(data[0]))
    dot_rows = []
    print(dots)
    for i in range(0, len(data)):
        if (len(set(data[i])) == 1):
            print("append dots to %d" % i)
            dot_rows.append(i)
    print(dot_rows)

    ins_count = 0
    for val in dot_rows:
        data.insert(val + ins_count, dots)
        ins_count += 1
    for line in data:
        print(line)

    print("\n\n")

    dots = np.array(dots)
    data = np.array(data)
    num_slice = len(data[:,0])
    dots = np.array(list("." * num_slice))
    dots.shape = (num_slice, 1)
    dot_cols = []
    print(dots)
    print("\n\n")
    for i in range(0, len(data[i])):
        slice = len(set(list(data[:,i])))
        if (slice == 1):
            dot_cols.append(i)
    print(dot_cols)
    
    ins_count = 0
    for val in dot_cols:
        data = np.hstack((data[:,:val+ins_count], dots, data[:,val+ins_count:]))
        ins_count += 1
    data = data.tolist()
    
    for line in data:
        print(*line, sep='')

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
            graph[(i,j)] = connects
    print(galaxies)
    print("\n\n")
    print(graph)
    print("\n\n")

    done = []
    for key in galaxies.keys():
        for key2 in galaxies.keys():
            val = galaxies[key]
            val2 = galaxies[key2]
            if (val == val2):
                continue
            elif ((val,val2) in done or (val2, val) in done):
                continue
            else:
                dist = abs(val[0] - val2[0]) + abs(val[1] - val2[1])
                done.append((val, val2))
                done.append((val2, val))
                #print("shortest path from %s to %s is %d" % (key, key2, dist))
                ans += dist
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
    dots = list("." * len(data[0]))
    dot_rows = []
    print(dots)
    for i in range(0, len(data)):
        if (len(set(data[i])) == 1):
            print("append dots to %d" % i)
            dot_rows.append(i)
    print(dot_rows)

    print("\n\n")

    dots = np.array(dots)
    data = np.array(data)
    num_slice = len(data[:,0])
    dots = np.array(list("." * num_slice))
    dots.shape = (num_slice, 1)
    dot_cols = []
    print(dots)
    print("\n\n")
    for i in range(0, len(data[i])):
        slice = len(set(list(data[:,i])))
        if (slice == 1):
            dot_cols.append(i)
    print(dot_cols)


    print("modifiers at %s rows and %s cols" % (dot_rows, dot_cols))

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
            graph[(i,j)] = connects

    done = []
    offset = 1000000 - 1
    dot_cols.sort()
    dot_rows.sort()
    for key in galaxies.keys():
        for key2 in galaxies.keys():
            val = galaxies[key]
            val2 = galaxies[key2]
            if (val == val2):
                continue
            elif ((val,val2) in done or (val2, val) in done):
                continue
            else:
                min_row, min_col = min(val[0], val2[0]), min(val[1], val2[1])
                max_row, max_col = max(val[0], val2[0]), max(val[1], val2[1])
                extra_rows = len(set(range(min_row, max_row+1)).intersection(dot_rows))
                extra_cols = len(set(range(min_col, max_col+1)).intersection(dot_cols))
                dist = abs((max_row + offset * extra_rows) - min_row) + abs((max_col + offset * extra_cols) - min_col)
                done.append((val, val2))
                done.append((val2, val))
                #print("shortest path from %s to %s is %d" % (key, key2, dist))
                #print("extra rows %d extra cols %d" % (extra_rows, extra_cols))
                ans += dist

    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''

    print("modifiers at %s rows and %s cols" % (dot_rows, dot_cols))
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
    file_name = "./day11.txt"
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
    #ans1, part1time = part_1(data1)
    # ---------------Part 2------------------- #
    ans2, part2time = part_2(data2)


    #check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
