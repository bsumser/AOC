import time
import re
from scanf import scanf #https://pypi.org/project/scanf/
import math

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
from aocd import submit
from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    #print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    input = "LRRLRRRLLRRLRRLRRRLRLRRLRRLRRRLRRRLRRLRLLRRLRLRRLRRLRLRLRRLRRLRRRLLRLLRRLRLRRRLRRRLLRRRLRRLRLLRRLRRRLRLLRLRLLRRRLRLRRRLLRRRLRRRLRRLLRLRLLRRLRRLLRRRLLRLLRRLRRRLRLRRRLRLRRLRLRLRRLRRLRRLLLRRRLRLRLLLRRRLLRLRRLRRRLRRLRRLRRRLRRRLRRLLRLLRRLRRRLLRRRLRLRLRRRLRRRLRRLRRLRLLRLRRLLRRLLRRRR"
    #input = "RL"
    input = list(input)
    steps = 0
    print(input)
    transitions = {}

    for i in range(0, len(data)):
        cur = data[i]
        transitions[cur[0]] = {"L":cur[1], "R":cur[2]}
    print(transitions)

    state = "AAA"
    accepting = "ZZZ"
    i = 0

    while(state != accepting):
        dir = input[i]
        old_state = state
        state = transitions[state][dir]
        print("%s to %s on %s" % (old_state, state, dir))
        steps += 1
        if (state == accepting):
            break
        i += 1
        if (i == len(input)):
            i = 0
    print(state)
    ans = steps


    
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
    input = "LRRLRRRLLRRLRRLRRRLRLRRLRRLRRRLRRRLRRLRLLRRLRLRRLRRLRLRLRRLRRLRRRLLRLLRRLRLRRRLRRRLLRRRLRRLRLLRRLRRRLRLLRLRLLRRRLRLRRRLLRRRLRRRLRRLLRLRLLRRLRRLLRRRLLRLLRRLRRRLRLRRRLRLRRLRLRLRRLRRLRRLLLRRRLRLRLLLRRRLLRLRRLRRRLRRLRRLRRRLRRRLRRLLRLLRRLRRRLLRRRLRLRLRRRLRRRLRRLRRLRLLRLRRLLRRLLRRRR"
    #input = "LR"
    input = list(input)
    print(input)
    transitions = {}
    starts = []
    end_states = []
    ans = []

    for i in range(0, len(data)):
        cur = data[i]
        transitions[cur[0]] = {"L":cur[1], "R":cur[2]}
    print(transitions)

    for line in data:
        cur = line[0]
        if (cur[2] == 'A'):
            starts.append(cur)
    
    print(starts)

    for state in starts:
        steps = 0
        i = 0
        while(state[2] != "Z"):
            dir = input[i]
            old_state = state
            state = transitions[state][dir]
            print("%s to %s on %s" % (old_state, state, dir))
            steps += 1
            if (state[2] == "Z"):
                end_states.append(state)
                break
            i += 1
            if (i == len(input)):
                i = 0
         
        ans.append(steps)
    print(end_states)
    print(ans)
    ans = math.lcm(*ans)
    print(ans)

    assert ans == 19185263738117

    
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''


    end_time = time.time() - start_time
    print("Part 2 done in %s seconds" % (end_time))
    print("Part 2 answer is: %d\n" % ans)
    return (ans, end_time)

def state_check(states):
    for state in states:
        if state[2] != "Z":
            return False
    return True


def parse_data():
    #open file and count lines
    file_name = "./day8.txt"
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
    data = [line.split(",") for line in data]
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
    #print(data)
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


    check_answer(ans1)
    #return (ans1, part1time, ans2, part2time)
    return 0
main()
