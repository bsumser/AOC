#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
import saoc

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    ans = 0
    start_time = time.time()

    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    nums, groups, rule_set = data[0], data[1], set()

    for i in range(len(nums)):
        rule_set.add( (nums[i][0], nums[i][1]))
    
    passes = list(filter(lambda group: group_checker(group, rule_set), groups))
    ans = sum(group[len(group)//2] for group in passes)
    
    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    print("Part 1 done in %s seconds" % (time.time() - start_time))
    print("Part 1 answer is: %d\n" % ans)
    #big boy assertion
    #assert ans == 14346279
    return ans

def group_checker(group, rule_set):
    for i in range(0, len(group)):
        cur_val, end_slice, start_slice = group[i], group[i+1:], group[0:i]
        
        for val in start_slice:
            if (cur_val, val) in rule_set:
                return False

        for val in end_slice:
            if (val, cur_val) in rule_set:
                return False
    return True


def part_2(data):
    '''Function that takes data and performs part 2'''
    print("part 2 starting----reading %d lines of data" % len(data))
    start_time = time.time()
    ans = 0

    '''-------------------------------PART 2 CODE GOES HERE--------------------------------------'''
    nums, groups, rule_set, post_rules = data[0], data[1], set(), {}

    for i in range(len(nums)):
        rule_set.add( (nums[i][0], nums[i][1]))
        if nums[i][0] not in post_rules:
            post_rules[nums[i][0]] = [nums[i][1]]
        elif nums[i][0] in post_rules:
            post_rules[nums[i][0]].append(nums[i][1])
    
    fails = list((filter(lambda group: not group_checker(group, rule_set), groups)))
    for fail in fails:
        i = 0
        while i < len(fail) - 1:
            # bubble sort up according to post idx rule
            if fail[i+1] not in post_rules[fail[i]]:
                fail[i], fail[i+1] = fail[i+1], fail[i]
                i = -1
            i += 1
    ans = sum(group[len(group)//2] for group in fails)

    '''-------------------------------PART 2 CODE ENDS HERE--------------------------------------''' 
    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    #big boy assertion
    #assert ans == 14357204
    return ans

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().split("\n\n")
    nums = [[int(val) for val in rule.split('|') if val ] for rule in data[0].split("\n") if rule]
    groups = [[int(val) for val in group.split(',') if val ] for group in data[1].split("\n") if group]
    data = [nums, groups]

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
