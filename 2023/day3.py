#!/usr/bin/env python3
import time
import re
#from scanf import scanf #https://pypi.org/project/scanf/

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
#from aocd import submit
#from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()
    coords = [[-1, 1], [0, 1], [1, 1], [-1, 0], [0, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''

    for i in range(0, len(data)):
        check_set = []
        for j in range(0, len(data[i])):
            char = data[i][j]
            if (char.isnumeric() == False and char != '.'):
                print(char)
                check_set = []
                for coord in coords:
                    i_2 = i + coord[0]
                    j_2 = j + coord[1]
                    cur = [i_2, j_2]
                    if (data[i_2][j_2] and data[i_2][j_2].isnumeric()):
                        print("num found %d" % int(data[i_2][j_2]))
                        num = []
                        if (cur not in check_set):
                            num.append(data[i_2][j_2])
                        head = [i_2, j_2-1]
                        tail = [i_2, j_2+1]

                        while(head[1] >= 0 and data[head[0]][head[1]].isnumeric()):
                            if (data[head[0]][head[1]].isnumeric()):
                                num.insert(0, data[head[0]][head[1]])
                            head[1] -= 1
                        while(tail[1] < len(data[i]) and data[tail[0]][tail[1]].isnumeric()):
                            if (data[tail[0]][tail[1]].isnumeric()):
                                num.append(data[tail[0]][tail[1]])
                                check_set.append(tail)
                            tail[1] += 1
                        num_int = int("".join(num))
                        if (num_int not in check_set):
                            print("adding %d" % num_int)
                            ans += num_int
                            check_set.append(num_int)



    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0


    coords = [[-1, 1], [0, 1], [1, 1], [-1, 0], [0, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''

    for i in range(0, len(data)):
        check_set = []
        for j in range(0, len(data[i])):
            char = data[i][j]
            if (char.isnumeric() == False and char != '.' and char == '*'):
                gear_set = []
                print(char)
                check_set = []
                for coord in coords:
                    i_2 = i + coord[0]
                    j_2 = j + coord[1]
                    cur = [i_2, j_2]
                    if (data[i_2][j_2] and data[i_2][j_2].isnumeric()):
                        print("num found %d" % int(data[i_2][j_2]))
                        num = []
                        if (cur not in check_set):
                            num.append(data[i_2][j_2])
                        head = [i_2, j_2-1]
                        tail = [i_2, j_2+1]

                        while(head[1] >= 0 and data[head[0]][head[1]].isnumeric()):
                            if (data[head[0]][head[1]].isnumeric()):
                                num.insert(0, data[head[0]][head[1]])
                            head[1] -= 1
                        while(tail[1] < len(data[i]) and data[tail[0]][tail[1]].isnumeric()):
                            if (data[tail[0]][tail[1]].isnumeric()):
                                num.append(data[tail[0]][tail[1]])
                                check_set.append(tail)
                            tail[1] += 1
                        num_int = int("".join(num))
                        if (num_int not in check_set):
                            print("adding gear %d" % num_int)
                            gear_set.append(num_int)
                            check_set.append(num_int)
                if (len(gear_set) == 2):
                    res = 1
                    for gear in gear_set:
                        res = res * gear
                    ans += res





    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day3.txt"
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
    print(data)
    return data

def check_answer(answer):
    choice = input("ANSWER IS %d; DO YOU WISH TO SUBMIT (y/n)?\n" % (answer))

    if (choice == 'y'):
        try:
            #print(submit(answer))
            print("submit")
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
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    check_answer(ans2)
    return 0
main()
