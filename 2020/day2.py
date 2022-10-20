import pyperclip #module for copying to clipboard
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=2, year=2020)
#print(inputData)

data = [str.strip() for str in inputData.splitlines()] #split into list
data = [str.replace(':', '') for str in data] #split into list
data = [str.replace('-', ' ') for str in data] #split into list
data = list(filter(bool, data)) #remove empty strings
data = [txt.split(" ") for txt in data]

print("Data Received")
print(data)


#---------------Part 1-------------------#
total = 0
for item in data:
    count = item[3].count(item[2])
    print(item[0], count, item[1], sep=' ')
    if (count >= int(item[0]) and count <= int(item[1])):
        total += 1

#---------------Part 2-------------------#
total = 0
for item in data:
    if (item[3][int(item[0]) - 1] == item[2] and item[3][int(item[1]) - 1] == item[2]):
        continue
    elif (item[3][int(item[0]) - 1] != item[2] and item[3][int(item[1]) - 1] != item[2]):
        continue
    elif (item[3][int(item[0]) - 1] == item[2] or item[3][int(item[1]) - 1] == item[2]):
        total += 1

pyperclip.copy(str(total))
