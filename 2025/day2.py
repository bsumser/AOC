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
    invs = []
    for line in data:
        id1, id2 = line.split("-")
        ids = [id1, id2]
        for id in range(int(id1), int(id2)+1):
            id = str(id)
            if id[0] == "0":
                ans += int(id)
                continue
            if len(id) % 2 == 0:
                first = id[:(len(id) // 2)]
                second = id[(len(id) // 2):]
                if first == second:
                    ans += int(id)
                    continue



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
        id1, id2 = line.split("-")
        ids = [id1, id2]
        for id in range(int(id1), int(id2)+1):
            s = str(id)
            for i in range(1, len(s)):
                out = set(split_str(s, i, False))
                if len(out) == 1:
                    ans += int(s)
                    break
    

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read()

    #data = data.split("\n") # split on single new line
    #data = list(map(int, data)) # map all to int

    # parse into grid
    data = data.split(",") # split on single new line
    #data = [list(line) for line in data]
    data = [line.strip("\n") for line in data]

    #data = data.split("\n\n") # split on double newline
    #data = [line.split("\n") for line in data]

    print(data)
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
