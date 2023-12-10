import time
import re
#from scanf import scanf #https://pypi.org/project/scanf/
import math

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

    start = (69, 88)

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    graph = {}
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            connects = check_coord_neighbors( [i, j], data)
            print(connects)
            graph[(i,j)] = connects
            if (data[i][j] == 'S'):
                print("start at %d,%d" % (i,j))

    for line in graph:
        print(line)

    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)

def check_coord(i, j, char):

    #| is a vertical pipe connecting north and south.
    #- is a horizontal pipe connecting east and west.
    #L is a 90-degree bend connecting north and east.
    #J is a 90-degree bend connecting north and west.
    #7 is a 90-degree bend connecting south and west.
    #F is a 90-degree bend connecting south and east.
    #. is ground; there is no pipe in this tile.
    #S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    pipe_dict = {"|":"north and south",
        "-":"east and west",
        "L":"north and east",
        "J":"north and west",
        "7":"south and west",
        "F":"south and east",
        ".":"east and west",
        "S":"starting",
    }

def check_coord_neighbors(input_coord, data):
    """Function to check all neighbors of an input coordinate

    """
    coords = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    dirs = ["W", "N", "S", "E"]
    connects = {
        (0, 1):"- J 7",
        (-1, 0):"| 7 F",
        (1, 0):"| L J",
        (0, -1):"- L F"}

    length = len(data[0]) - 1
    height = len(data) - 1
    
    connections = []
    for k in range(0, len(coords)):
        coord = coords[k]
        cur_dir = dirs[k]
        i = input_coord[0] + coord[0]
        j = input_coord[1] + coord[1]
        if (0 <= i <= length and 0 <= j <= height):
            symbol = data[i][j]
            print("coord is %s, neighbor is %s val is %c" % (input_coord, [i,j], symbol))
            if (symbol in connects[coord]):
                print("\tvalid connection on %c" % symbol)
                connections.append((i,j))
    return connections


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

def recur_helper(data, ret):
    check = True
    for val in data:
        if (val != 0):
            check = False
    if (check == True):
        print(data)
        return ret
    cur = []
    for j in range(0, len(data) - 1):
        cur.append(data[j+1] - data[j])
    ret.append(cur)

    recur_helper(cur, ret)

def parse_data():
    #open file and count lines
    file_name = "./day10s.txt"
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
