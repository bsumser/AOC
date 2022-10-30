import pyperclip #module for copying to clipboard
import re
from aocd import get_data #module for automating advent of code data get

dp = [[]]
p = []

def getSums(myList,target):
    already_seen = set()
    pairs = []
    for x in myList:
        if (target - x) in already_seen:
            pairs.append((x, target - x))
        already_seen.add(x)
    return pairs

def maxSubArraySum(a, size):

    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def bruteSub(array, value):
    for i in range(len(array)):
        for j in range(i, len(array)):
            sum = 0
            for k in range(i, j):
                sum += array[k]
            if (sum == value):
                print(array[i:j])
                print(min(array[i:j]))
                print(max(array[i:j]))
                return print(min(array[i:j]) + max(array[i:j]))

def main():
    inputData = get_data(day=9, year=2020)

    data = [line.strip() for line in inputData.split("\n")] #split into list
    data = [int(line) for line in data]
    print("Data Received")
    print(data)
    ans = 0
    i = 25


    #---------------Part 1-------------------#
    #res = []
    #print(data[i-25:i])
    #print(data[i])
    #while i < len(data):
    #    mini = data[i-25:i]
    #    if (getSums(mini, data[i]) == []):
    #        print(data[i])
    #        ans = data[i]
    #        pyperclip.copy(str(ans))
    #        #return data[i]
    #    i += 1


    #---------------Part 2-------------------#
    ans = bruteSub(data, 3199139634)

    print(ans)
    pyperclip.copy(str(ans))
    return 0
main()
