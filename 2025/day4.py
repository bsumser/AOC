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
    for point in data:
        print(data[point])
        count = 0
        if (data[point] == "."):
            continue
        for d in (1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j):
            if point + d in data and (data[point+d] == "@" or data[point + d] == "X"):
                count += 1
        if count < 4:
            ans += 1
            data[point] = "X"
    
    height = 10
    width = 10
    for y in range(height):
        row = []
        for x in range(width):
            v = data.get(x + y*1j)
            row.append(v)
        print("".join(row))

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
    years = 50
    for i in range(0, years):
        old_data = data.copy()
        data, ans = update(data, ans)
        if old_data == data:
            break
        else:
            old_data = data
    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def update(maze, ans):
    newMaze = maze.copy()
    for point in newMaze:
        count = 0
        if (newMaze[point] == "."):
            continue
        for d in (1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j):
            if point + d in newMaze and (newMaze[point+d] == "@"):
                count += 1
        if count < 4:
            ans += 1
            newMaze[point] = "."
    height = 10
    width = 10
    for y in range(height):
        row = []
        for x in range(width):
            v = newMaze.get(x + y*1j)
            row.append(v)
        print("".join(row))
    print("\n")
    return newMaze, ans


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    #data = data.split("\n") # split on single new line
    #data = list(map(int, data)) # map all to int

    # parse into grid
    #data = data.split("\n") # split on single new line
    #data = [list(line) for line in data]
    #data = [list(line) for line in data]

    #data = data.split("\n\n") # split on double newline
    #data = [line.split("\n") for line in data]
    maze = {}
    for r, row in enumerate(data.splitlines()):
        for c, char in enumerate(row):
            maze[r * 1j + c] = char

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return maze

def main():
    # ---------------Part 1------------------- #
    part_1(parse_data())
    # ---------------Part 2------------------- #
    part_2(parse_data())

    return 0

if __name__ == "__main__":
    main()
