import time
import re
from scanf import scanf #https://pypi.org/project/scanf/
import math

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
from aocd import submit
#from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 0
    start_time = time.time()
    seeds = "79 14 55 13"
    #seeds = "3127166940 109160474 3265086325 86449584 1581539098 205205726 3646327835 184743451 2671979893 17148151 305618297 40401857 2462071712 203075200 358806266 131147346 1802185716 538526744 635790399 705979250"
    seeds = list(map(int, seeds.split()))
    #print("seeds: %s" % str(seeds))
    cats = ["seed to soil", "soil to fert", "fert to water", "water to light", "light to temp", "temp to humid", "humid to loca"]
    seed_loci = []
    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''

    for seed in range(0, len(seeds)):
        categories = [
            [data[0][i:i+3] for i in range(0, len(data[0]), 3)],
            [data[1][i:i+3] for i in range(0, len(data[1]), 3)],
            [data[2][i:i+3] for i in range(0, len(data[2]), 3)],
            [data[3][i:i+3] for i in range(0, len(data[3]), 3)],
            [data[4][i:i+3] for i in range(0, len(data[4]), 3)],
            [data[5][i:i+3] for i in range(0, len(data[5]), 3)],
            [data[6][i:i+3] for i in range(0, len(data[6]), 3)]]
        print(categories)
        cur_seed = seeds[seed]
        print(cur_seed)
        for i in range(0, len(categories)):
            cur_loci = []
            category = categories[i]
            print("cur seed is %d category is %s %s" % (cur_seed, cats[i], str(category)))
            cur_seed = seed_mapper(cur_seed, category)
            cur_loci.append(cur_seed)
        seed_loci.append(cur_seed)
        print("ended with cur seed %d" % cur_seed)
        if (305618297 <= cur_seed <= 3831071286):
            ans = cur_seed
            break


    #print(seed_loci)
    #ans = min(seed_loci)
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    return ans

def seed_mapper(seed, category):
    for entry in category:
        source = entry[1]
        dest = entry[0]
        rang = entry[2]-1
        
        # part 1
        offset = dest - source
        
        print("\tsource range %d to %d\n\tdest range %d to %d\n\toffset is %d" % (source, source+rang, dest, dest+rang, offset))
        if (source <= seed <= source+rang):
            print("\t\tseed hit")
            print("\t\tmapping seed %d to dest %d" % (seed, seed+offset))
            seed += offset
            return seed
    print("\t\tseed mapping not found")
    print("\t\tmapping seed %d to dest %d" % (seed, seed))
    return seed

def seed_mapper_2(seed, category):
    for entry in category:
        source = entry[1]
        dest = entry[0]
        rang = entry[2]-1
        
        # part 2
        offset = source - dest
        #print("\tsource range %d to %d\n\tdest range %d to %d\n\toffset is %d" % (source, source+rang, dest, dest+rang, offset))
        if (dest <= seed <= dest+rang):
            #print("\t\tseed hit")
            #print("\t\tmapping seed %d to dest %d" % (seed, seed+offset))
            seed += offset
            return seed
    #print("\t\tseed mapping not found")
    #print("\t\tmapping seed %d to dest %d" % (seed, seed))
    return seed

def multi_loop(seed, seeds, data):
    categories = [
        [data[0][i:i+3] for i in range(0, len(data[0]), 3)],
        [data[1][i:i+3] for i in range(0, len(data[1]), 3)],
        [data[2][i:i+3] for i in range(0, len(data[2]), 3)],
        [data[3][i:i+3] for i in range(0, len(data[3]), 3)],
        [data[4][i:i+3] for i in range(0, len(data[4]), 3)],
        [data[5][i:i+3] for i in range(0, len(data[5]), 3)],
        [data[6][i:i+3] for i in range(0, len(data[6]), 3)]]
    trans_seed = seed
    loca_seed = seed
    #print(categories)
    #print(trans_seed)
    for i in range(len(categories)-1, -1, -1):
        category = categories[i]
        #print("cur seed is %d category is %s %s" % (trans_seed, cats[i], str(category)))
        trans_seed = seed_mapper_2(trans_seed, category)
    #map_str = "final mapping %d to %d" % (loca_seed, trans_seed)

    for val in range(0, len(seeds), 2):
        first = seeds[val]
        last = seeds[val] + seeds[val+1]
        #print("seed range is %d to %d trans_seed is %d" % (first, last - 1, trans_seed))
        if (trans_seed in range(first, last)):
            print("map loca_seed %d from trans_seed %d" % (loca_seed, trans_seed))
            ans = loca_seed
            print("Part 2 done in %s seconds" % (time.time() - start_time))
            print("Part 2 answer is: %d\n" % ans)
            return ans


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    start_time = time.time()
    ans = 0


    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    #seeds = "79 14 55 13"
    seeds = "3127166940 109160474 3265086325 86449584 1581539098 205205726 3646327835 184743451 2671979893 17148151 305618297 40401857 2462071712 203075200 358806266 131147346 1802185716 538526744 635790399 705979250"
    # 305618297  - 3831071286
    seeds = list(map(int, seeds.split()))
    ##print("seeds: %s" % str(seeds))
    cats = ["seed to soil", "soil to fert", "fert to water", "water to light", "light to temp", "temp to humid", "humid to loca"]
    seed_loci = []

    intervals = []

    for i in range(0, len(seeds), 2):
        cur = [seeds[i], seeds[i] + seeds[i+1]]
        intervals.append(cur)
    intervals.sort()
    print(intervals, len(intervals))
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    print(stack, len(stack))

    for seed in range(0, 3831071286):
        categories = [
            [data[0][i:i+3] for i in range(0, len(data[0]), 3)],
            [data[1][i:i+3] for i in range(0, len(data[1]), 3)],
            [data[2][i:i+3] for i in range(0, len(data[2]), 3)],
            [data[3][i:i+3] for i in range(0, len(data[3]), 3)],
            [data[4][i:i+3] for i in range(0, len(data[4]), 3)],
            [data[5][i:i+3] for i in range(0, len(data[5]), 3)],
            [data[6][i:i+3] for i in range(0, len(data[6]), 3)]]
        trans_seed = seed
        loca_seed = seed
        #print(categories)
        #print(trans_seed)
        for i in range(len(categories)-1, -1, -1):
            category = categories[i]
            #print("cur seed is %d category is %s %s" % (trans_seed, cats[i], str(category)))
            trans_seed = seed_mapper_2(trans_seed, category)
        #map_str = "final mapping %d to %d" % (loca_seed, trans_seed)

        for val in range(0, len(seeds), 2):
            first = seeds[val]
            last = seeds[val] + seeds[val+1]
            #print("seed range is %d to %d trans_seed is %d" % (first, last - 1, trans_seed))
            if (trans_seed in range(first, last)):
                print("map loca_seed %d from trans_seed %d" % (loca_seed, trans_seed))
                ans = loca_seed
                print("Part 2 done in %s seconds" % (time.time() - start_time))
                print("Part 2 answer is: %d\n" % ans)
                return ans
                
    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------'''


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day5.txt"
    lines = open(file_name, 'r').readlines()
    num_lines = len(lines)
    print("parsing data for ----reading %d lines of data\n" % num_lines)

    #open file and read in data
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()


    '''-------------------------------PARSE BLOCK START------------------------------------------'''

    # split on newline
    data = data.split("\n\n")
    data = [line.split() for line in data]
    for i in range(0, len(data)):
        data[i] = list(map(int, data[i]))
    
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
    print(data)
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
    #ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    check_answer(ans2)
    return 0
main()
