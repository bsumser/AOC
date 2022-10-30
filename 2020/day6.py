import pyperclip #module for copying to clipboard
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=6, year=2020)

data = [str.strip() for str in inputData.split("\n\n")] #split into list
data = [str.replace('\n', ' ') for str in data] #split into list
data = list(filter(bool, data)) #remove empty strings

print("Data Received")
print(data)
ans = 0

#---------------Part 1-------------------#
#for line in data:
#    s = set(line.replace(" ", ""))
#    print(line, len(s), sep=" ")
#    ans += len(s)

#---------------Part 2-------------------#
for line in data:
    newLine = line.split(" ")
    #print(newLine)
    a = set(newLine[0])
    for string in newLine:
        a &= set(string)
    print(len(a))
    ans += len(a)

print(ans)
pyperclip.copy(str(ans))
