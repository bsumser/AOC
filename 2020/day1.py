import pyperclip #module for copying to clipboard
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=1, year=2020)
print(inputData)

data = [str.strip() for str in inputData.splitlines()] #split into list
data = list(filter(bool, data)) #remove empty strings

data = [int(i) for i in data]

print("tester")

#---------------Part 1-------------------#
for i in data:
    for j in data:
        if (i+j == 2020):
            ans = i*j

#---------------Part 2-------------------#
for i in data:
    for j in data:
        for k in data:
            if (i+j+k == 2020):
                ans = i*j*k

pyperclip.copy(str(ans))
