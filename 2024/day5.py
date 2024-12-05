#!/usr/bin/env python3
import time
import sys
import regex
import itertools
import functools

rule_set = set()

sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    nums = data[0].split("\n")
    groups = data[1].split("\n")

    post_rules = {}
    pre_rules = {}
    rule_set = set()

    for i in range(len(nums)):
        nums[i] = nums[i].split("|")
        nums[i] = [int(val) for val in nums[i]]
        rule_set.add( (nums[i][0], nums[i][1]))
        if (nums[i][0] not in post_rules):
            post_rules[nums[i][0]] = [nums[i][1]]
        else:
            post_rules[nums[i][0]].append(nums[i][1])
        if (nums[i][1] not in pre_rules):
            pre_rules[nums[i][1]] = [nums[i][0]]
        else:
            pre_rules[nums[i][1]].append(nums[i][0])
    
    for i in range(len(groups)):
        groups[i] = groups[i].split(",")
        groups[i] = [int(val) for val in groups[i]]
    #print(groups)

    passes = []
    for group in groups:
        if (group_checker(group, pre_rules, post_rules, rule_set)):
            passes.append(group)
    for group in passes:
        ans += group[len(group)//2]

                

    
    
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    assert ans > 111

    #big boy assertion
    #assert ans == 7025140
    return ans

def group_checker(group, pre_rules, post_rules, rule_set):
    for i in range(0, len(group)):
        cur_val = group[i]
        end_slice = set(group[i+1:])
        start_slice = set(group[0:i])
        
        for val in start_slice:
            if (cur_val, val) in rule_set:
                return False

            if (val, cur_val) in rule_set:
                cur_key = pre_rules[cur_val]
                if val in cur_key:
                    pass
        for val in end_slice:
            if (val, cur_val) in rule_set:
                return False
            if (cur_val, val) in rule_set:
                cur_key = post_rules[cur_val]
                if val not in cur_key:
                    return False
    return True


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    nums = data[0].split("\n")
    groups = data[1].split("\n")

    post_rules = {}
    pre_rules = {}
    rule_set = set()

    for i in range(len(nums)):
        nums[i] = nums[i].split("|")
        nums[i] = [int(val) for val in nums[i]]
        rule_set.add( (nums[i][0], nums[i][1]))
        if (nums[i][0] not in post_rules):
            post_rules[nums[i][0]] = [nums[i][1]]
        else:
            post_rules[nums[i][0]].append(nums[i][1])
        if (nums[i][1] not in pre_rules):
            pre_rules[nums[i][1]] = [nums[i][0]]
        else:
            pre_rules[nums[i][1]].append(nums[i][0])
    
    for i in range(len(groups)):
        groups[i] = groups[i].split(",")
        groups[i] = [int(val) for val in groups[i]]
    #print(groups)

    fails = []
    re_pass = []
    for group in groups:
        if not (group_checker(group, pre_rules, post_rules, rule_set)):
            fails.append(group)
    for fail in fails:
        i = 0
        while i < len(fail) - 1:
            # bubble sort up according to post idx rule
            if fail[i+1] not in post_rules[fail[i]]:
                fail[i], fail[i+1] = fail[i+1], fail[i]
                i = -1
            i += 1
    for group in fails:
        ans += group[len(group)//2]


    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    #assert ans == 1737

    #big boy assertion
    #assert ans == 879274
    return ans

def compare(a, b):
    if (a,b) not in rule_set:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def parse_data():
    start_time = time.time()

    # open file and read in data
    file_name = sys.argv[1]
    print(f"parsing data for {file_name}")
    data = open(file_name, "r").read()
    data = data.split("\n\n")
    #data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def parse_data_2():
    start_time = time.time()

    # open file and read in data
    file_name = sys.argv[1]
    print(f"parsing data for {file_name}")
    my_file = open(file_name, "r")
    data = my_file.read()
    my_file.close()
    
    data = data.split("\n")
    data = [list(line) for line in data]
    #data = [[int(val) for val in line] for line in data]

    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    ans1 = 0
    ans2 = 0

    # ---------------Part 1------------------- #
    data = parse_data()
    ans1 = part_1(data)
    # ---------------Part 2------------------- #
    #data2 = parse_data_2()
    ans2 = part_2(data)

    return 0

if __name__ == "__main__":
    main()
