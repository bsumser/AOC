import time
import re
from scanf import scanf #https://pypi.org/project/scanf/

# module for automating advent of code data get
# https://github.com/wimglenn/advent-of-code-data
from aocd import submit
#from aocd import get_data

#https://aocpercenter.marcolussetti.com/

def part_1(data):
    '''Function that takes data and performs part 1'''
    print("part 1 starting----reading %d lines of data" % len(data))
    print("printing first line of data:\n")
    ans = 1 + 6
    start_time = time.time()
    cards = [data[0]]
    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''
    while(cards):
        card = cards.pop()
        card_num, nums, wins = card[0], card[2], card[1]
        card_num = int(card_num[0])
        nums = nums.split()
        nums = [int(num) for num in nums]
        wins = wins.split()
        wins = [int(win) for win in wins]
        print("process card %d" % card_num)
        print(card_num, wins, nums)

        points = set(nums).intersection(set(wins))
        print(points, len(points))

        print("won cards %d to %d" % (card_num+1, card_num + len(points)))

        for i in range(card_num, card_num + len(points) + 1):
            ans += 1
            cards.append(data[i-1])
        print(cards)
        print("len of cards is %d " % ans)
        choice = input("continue? (y/n)")
        if (choice == 'y'):
            continue



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


    '''-------------------------------PART 1 CODE GOES HERE--------------------------------------'''






    '''-------------------------------PART 1 CODE ENDS HERE--------------------------------------'''


    print("Part 2 done in %s seconds" % (time.time() - start_time))
    print("Part 2 answer is: %d\n" % ans)
    return ans

def parse_data():
    #open file and count lines
    file_name = "./day4s.txt"
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
    data = [line.split("|") for line in data]
    
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
    ans1 = part_1(data1)
    # ---------------Part 2------------------- #
    ans2 = part_2(data2)


    check_answer(ans1)
    return 0
main()
