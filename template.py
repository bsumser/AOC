import pyperclip #module for copying to clipboard
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=3, year=2020)
#print(inputData)

data = [str.strip() for str in inputData.splitlines()] #split into list
#data = [str.replace(':', '') for str in data] #split into list
#data = [str.replace('-', ' ') for str in data] #split into list
data = list(filter(bool, data)) #remove empty strings
#data = [txt.split(" ") for txt in data]

print("Data Received")
print(data)

#---------------Part 1-------------------#
pos = 0
trees = 0
for line in range(1, len(data)):
    pos += 2
    if (pos > 10):
        pos = (pos % 10) - 1
    print(pos, data[line], sep=" ")
    if (data[line][pos] == '#'):
        trees += 1

#---------------Part 2-------------------#

pyperclip.copy(str(trees))
