import time
<<<<<<< HEAD
#import re
##from scanf import scanf #https://pypi.org/project/scanf/
#import math
#import numpy as np
=======
import re
#from scanf import scanf #https://pypi.org/project/scanf/
import math
import numpy as np
>>>>>>> 8c57845 (part 1 done 2 is broken)

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
<<<<<<< HEAD
    
    
    
=======
    for line in data:
        string = line[0]
        nums = line[1].split(",")
        nums = [int(val) for val in nums]
        #print(string, nums)
        stringPoss = []
        string_recurse(string, 0, stringPoss)
        stringPoss = set(stringPoss)
        for poss in stringPoss:
            ans += string_check(poss, nums)

>>>>>>> 8c57845 (part 1 done 2 is broken)
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)

<<<<<<< HEAD
=======
def string_recurse(string, index, stringPoss):
    if (index == len(string)):
        stringPoss.append(string)
    else:
        stringList = list(string)
        if (stringList[index] == '#' or stringList[index] == '.'):
            base_case = ''.join(stringList)
            string_recurse(base_case, index+1, stringPoss)
        elif (stringList[index] == '?'):
            stringList[index] = '#'
            hash_case = ''.join(stringList)
            string_recurse(hash_case, index+1, stringPoss)

            stringList[index] = '.'
            dot_case = ''.join(stringList)
            string_recurse(dot_case, index+1, stringPoss)

def string_check(string, nums):
    answers = string.split('.')
    answers = [line for line in answers if line != '']
    #print(answers)
    if (len(answers) != len(nums)):
        #print("invalid string with %s nums %s" % (string, nums))
        #print("invalid on length")
        return 0
    for i in range(0, len(answers)):
        if (len(answers[i]) != nums[i]):
            #print("invalid string with %s nums %s" % (string, nums))
            #print(len(answers[i]), nums[i])
            return 0
    print("valid string with %s nums %s" % (string, nums))
    return 1
>>>>>>> 8c57845 (part 1 done 2 is broken)

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

<<<<<<< HEAD

def parse_data():
    #open file and count lines
    file_name = "./day12s.txt"
=======
def parse_data():
    #open file and count lines
    file_name = "./day12.txt"
>>>>>>> 8c57845 (part 1 done 2 is broken)
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()


    '''-------------------------------PARSE BLOCK START------------------------------------------'''

    # split on newline
<<<<<<< HEAD
    data = data.split("\n\n")
=======
    data = data.split("\n")
    data = [line.split() for line in data]
>>>>>>> 8c57845 (part 1 done 2 is broken)
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
<<<<<<< HEAD
    for line in data:
        print(line)
        print("\n")
=======
    print(data)
>>>>>>> 8c57845 (part 1 done 2 is broken)
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
<<<<<<< HEAD
    #ans1, part1time = part_1(data1)
=======
    ans1, part1time = part_1(data1)
>>>>>>> 8c57845 (part 1 done 2 is broken)
    # ---------------Part 2------------------- #
    ans2, part2time = part_2(data2)


    #check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
