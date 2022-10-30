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
#pos = 0
#trees = 0
#edge = len(data[0]) - 1
#print(edge)
#string = ""
#for line in range(1, len(data)):
#    string = "Miss at"
#    pos += 3
#    if (pos > edge):
#        pos = (pos % edge) - 1
#    if (data[line][pos] == '#'):
#        trees += 1
#        string = "Hit at"
#    print(string, pos, data[line], sep=" ")
#---------------Part 2-------------------#

pos = 0
trees = 0
edge = len(data[0]) - 1
print(edge)
string = ""

#for line in range(2, len(data)):
line = 2
while (line < len(data)):
    string = "Miss at"
    pos += 1
    if (pos > edge):
        pos = (pos % edge) - 1
    if (data[line][pos] == '#'):
        trees += 1
        string = "Hit at"
    print(string, pos, data[line], sep=" ")
    line+=2


ans = 64 * 65 * 259 * 59 * 35
print(ans)
pyperclip.copy(str(ans))
