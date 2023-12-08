import time
import re
#from scanf import scanf #https://pypi.org/project/scanf/
import math

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
    hands = []
    values = {"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":10,"J":0,"Q":12,"K":13,"A":14}
    for line in data:
        print(line)
        hand = line[0]
        bid = int(line[1])
        cur = []
        cur.append(hand)
        cur.append(bid)
        jack_level = 0

        for char in hand:
            if char == 'J':
                jack_level += 1
        
        res = {}
        for keys in hand:
            res[keys] = res.get(keys, 0) + 1
        res = dict(sorted(res.items(), key=lambda item:item[1], reverse=True))
        print("hand is %s bid is %d" % (hand, bid))
        print(res)
        res = [(k, v) for k, v in res.items()]
        print(res)

        strength = -1

        if (len(res) == 1):
            strength = 7
            print("five of a kind\n")
        elif (len(res) == 2 and res[0][1] == 4):
            if (jack_level == 1):
                strength = 7
            else:
                strength = 6
            print("four of a kind\n")
        elif (len(res) == 2 and res[0][1] == 3 and res[1][1] == 2):
            if (jack_level == 2):
                strength = 7
            elif (jack_level == 3):
                strength = 7
            else:
                strength = 5
            print("full house\n")
        elif (len(res) == 3 and res[0][1] == 3 and res[1][1] == 1):
            if (jack_level == 1):
                strength = 6
            elif (jack_level == 3):
                strength = 6
            else:
                strength = 4
            print("three of a kind\n")
        elif (len(res) == 3 and res[0][1] == 2 and res[1][1] == 2):
            if (jack_level == 1):
                strength = 5
            elif (jack_level == 2):
                strength = 6
            else:
                strength = 3
            print("two pair\n")
        elif (len(res) == 4 and res[0][1] == 2):
            if (jack_level == 1):
                strength = 4
            else:
                strength = 1
            print("one pair\n")
        elif (len(res) == 5):
            if (jack_level == 1):
                strength = 1
            else:
                strength = 0
            print("high card\n")
        if (strength == -1):
            print("strength for hand error")
            break
        cur.append(strength)

        for char in hand:
            cur.append(values[char])

        print("\n")
        hands.append(cur)
    hands = sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))
    for hand in hands:
        print(hand)

    for i in range(0, len(hands)):
        rank = i + 1
        print(hands[i][1], rank)
        ans += (int(hands[i][1]) * rank)


    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''
    end_time = time.time() - start_time
    print("Part 1 done in %s seconds" % (end_time))
    print("Part 1 answer is: %d\n" % ans)

    return (ans, end_time)



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



def parse_data():
    #open file and count lines
    file_name = "./day7.txt"
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
    data = [line.split() for line in data]
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
    ans1, part1time = part_1(data1)
    # ---------------Part 2------------------- #
    ans2, part2time = part_2(data2)


    #check_answer(ans1)
    return (ans1, part1time, ans2, part2time)
main()
