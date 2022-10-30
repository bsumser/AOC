import pyperclip #module for copying to clipboard
import math
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=5, year=2020)

data = [str.strip() for str in inputData.split("\n")] #split into list
data = list(filter(bool, data)) #remove empty strings

print("Data Received")
print(data)

#---------------Part 1-------------------#
#maxID = 0
#for line in data:
#    rowMin = 0
#    rowMax = 127
#    colMin = 0
#    colMax = 7
#    for char in range(0, len(line)):
#        if (line[char] == 'F'):
#            rowMax -= math.ceil((rowMax - rowMin) / 2)
#            print(line[char], "row range is", rowMin, rowMax, sep=" ")
#        if (line[char] == 'B'):
#            rowMin += math.ceil((rowMax - rowMin) / 2)
#            print(line[char], "row range is", rowMin, rowMax, sep=" ")
#        if (line[char] == 'R'):
#            colMin += math.ceil((colMax - colMin) / 2)
#            print(line[char], "col range is", colMin, colMax, sep=" ")
#        if (line[char] == 'L'):
#            colMax -= math.ceil((colMax - colMin) / 2)
#            print(line[char], "col range is", colMin, colMax, sep=" ")
#    if(maxID < ((rowMax * 8) + colMax)):
#        maxID = ((rowMax * 8) + colMax)
#---------------Part 2-------------------#
maxID = 0
plane = []
for line in data:
    rowMin = 0
    rowMax = 127
    colMin = 0
    colMax = 7
    for char in range(0, len(line)):
        if (line[char] == 'F'):
            rowMax -= math.ceil((rowMax - rowMin) / 2)
            #print(line[char], "row range is", rowMin, rowMax, sep=" ")
        if (line[char] == 'B'):
            rowMin += math.ceil((rowMax - rowMin) / 2)
            #print(line[char], "row range is", rowMin, rowMax, sep=" ")
        if (line[char] == 'R'):
            colMin += math.ceil((colMax - colMin) / 2)
            #print(line[char], "col range is", colMin, colMax, sep=" ")
        if (line[char] == 'L'):
            colMax -= math.ceil((colMax - colMin) / 2)
            #print(line[char], "col range is", colMin, colMax, sep=" ")
    plane.append((rowMax * 8) + colMax)
    plane.sort()
    if(maxID < ((rowMax * 8) + colMax)):
        maxID = ((rowMax * 8) + colMax)
for i in range(0, len(plane) - 1):
    if (plane[i + 1] == plane[i] + 2):
        print(plane[i] + 1)
print(len(data))
print(plane)
pyperclip.copy(str(maxID))
