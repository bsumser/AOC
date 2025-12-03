#!/usr/bin/env python3
import time
import sys
sys.setrecursionlimit(1500)
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    for i in range(0, len(data)):
        local_max = 0
        local_second = 0
        local_idx = 0
        for j in range(0, len(data[0])-1):
            if data[i][j] > local_max:
                local_max = data[i][j]
                local_idx = j
        for j in range(local_idx+1, len(data[0])):
            if data[i][j] > local_second:
                local_second = data[i][j]
        print(local_max, local_second)
        ans += (local_max * 10) + local_second 



    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    for line in data:
        stack = []
        to_remove = len(line) - 12

        for char in line:
            while stack and to_remove > 0 and stack[-1] < char:
                stack.pop()
                to_remove -= 1
            stack.append(char)
        print(stack[:12])
        s = map(str, stack[:12])
        s = ''.join(s)
        s = int(s)
        ans += s

    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def helper(s, remaining):
    local_max = 0
    for i in range(0, len(s)):
        if s[i] > local_max and s[i+1:] >= remaining:
            local_max = s[i]
    return local_max


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    data = data.split("\n") # split on single new line
    #data = list(map(int, data)) # map all to int

    # parse into grid
    #data = data.split(",") # split on single new line
    #data = [list(line) for line in data]
    data = [list(map(int, line)) for line in data]

    #data = data.split("\n\n") # split on double newline
    #data = [line.split("\n") for line in data]

    #print(data)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    part_1(parse_data())
    # ---------------Part 2------------------- #
    part_2(parse_data())

    return 0

if __name__ == "__main__":
    main()
