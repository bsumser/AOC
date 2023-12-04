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

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------''' 
    for line in data:
        ans += (int(line[0]) * 10) + int(line[-1])
    
    
    
    
    

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
    #nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------''' 
    for line in data:
        left = 0
        right = 0
        length = len(line)
        print(line)
        for i in range(0, length):
            for char in range (0, 3):
                cur_slice = line[i+char:i+5]
                back_slice = line[length-(char-3):length]
                print("\t %s - %s" % (cur_slice, back_slice))


   
   
   
   
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

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


    '''-------------------------------PARSE BLOCK START------------------------------------------''' 

    # split on newline
    data = data.split("\n")

    data = [''.join(filter(str.isdigit, val)) for val in data]
    
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

def parse_data_2():
    #open file and count lines
    file_name = "./day1s.txt"
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

    # list of replacements
    #nums = {1:["one","on1e"], 2:["two","tw2o"], 3:["three","thre3e"], 4:["four","fou4r"], 5:["five","fiv5e"], 
    #6:["six","si6x"], 7:["seven","seve7n"], 8:["eight","eigh8t"], 9:["nine","nin9e"]}

    ## loop through and replace instances
    #for i in range(0, len(data)):
    #    for j in range(1, len(nums)+1):
    #        data[i] = data[i].replace(nums[j][0], nums[j][1])
    #data = [''.join(filter(str.isdigit, val)) for val in data]
    
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
            print("exception has occurred")
        return 0
    else:
        return 0

def main():
    ans1 = 0
    ans2 = 0
    data1 = parse_data()
    data2 = parse_data_2()

    # ---------------Part 1------------------- #
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    check_answer(ans1)
    return 0
main()