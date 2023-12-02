#!/usr/bin/env python3
import time
import re
from scanf import scanf #https://pypi.org/project/scanf/

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
    red = 12
    green = 13
    blue = 14

    check_dict = {"red":12, "green":13, "blue":14}

    delims = [",", " "]

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    for i in range(0, len(data)):
        line = data[i]
        id = i+1
        check = True
        for string in line:
            for delim in delims:
                string = " ".join(string.split(delim))
            string = string.split()
            print(string)
            for i in range(0, len(string), 2):
                num = int(string[i])
                color = string[i+1]
                if(num > check_dict[color]):
                    check = False
        if (check == True):
            ans += id

    
    

    
    

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
    red = 12
    green = 13
    blue = 14

    check_dict = {"red":12, "green":13, "blue":14}

    delims = [",", " "]
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    for i in range(0, len(data)):
        line = data[i]
        id = i+1
        check = True
        freq_dict = {"red":0, "green":0, "blue":0}
        for string in line:
            for delim in delims:
                string = " ".join(string.split(delim))
            string = string.split()
            print(string)
            for i in range(0, len(string), 2):
                num = int(string[i])
                color = string[i+1]
                if (freq_dict[color] < num):
                    update = {color:num}
                    print(update)
                    freq_dict.update(update)
        ans += (freq_dict["red"] * freq_dict["blue"] * freq_dict["green"])
    


    

   
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day2.txt"
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
    data = [line.split(";") for line in data]

    for line in data:
        for item in line:
            item.split(",")

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
            print(submit(answer))
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