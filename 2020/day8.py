import pyperclip #module for copying to clipboard
import re
from aocd import get_data #module for automating advent of code data get

def main():
    inputData = get_data(day=8, year=2020)

    data = [line.strip() for line in inputData.split("\n")] #split into list
    data = [re.split(" |([\+])|([\-])", line) for line in data] #split into list
    data[i] = list(filter(lambda item: item ==  None, data[i]))
    data[i] = list(filter(lambda item: item != "", data[i]))
    print("Data Received")
    print(data)
    ans = 0

    #---------------Part 1-------------------#
    insCount = [0] * len(data)
    print(insCount)

    i = 0
    lastIns = 0
    while (i < len(data)):
        if (i > len(data)):
            break
        if (insCount[i] == 1):
            print("loop detected at index", lastIns, "for instruction", data[lastIns],sep=" ")
            if (data[lastIns][0] == "nop"):
                data[lastIns][0] = "jmp"
                insCount[lastIns] = 0
                i = lastIns
                return 0
            if (data[lastIns][0] == "jmp"):
                data[lastIns][0] = "nop"
                insCount[lastIns] = 0
                i = lastIns
                return 0
            print(i,data[i][1],data[i][2], sep=" ")
        if (data[i][0] == "acc" and data[i][1] == "+"):
            ans += int(data[i][2])
            insCount[i] = 1
            lastIns = i
            i += 1
        elif (data[i][0] == "acc" and data[i][1] == "-"):
            ans -= int(data[i][2])
            insCount[i] = 1
            lastIns = i
            i += 1
        elif (data[i][0] == "jmp" and data[i][1] == "+"):
            insCount[i] = 1
            lastIns = i
            i += int(data[i][2])
        elif (data[i][0] == "jmp" and data[i][1] == "-"):
            insCount[i] = 1
            lastIns = i
            i -= int(data[i][2])
        elif (data[i][0] == "nop"):
            insCount[i] = 1
            print("nop")
            lastIns = i
            i += 1

        #---------------Part 2-------------------#

        print(insCount)
        print(ans)
        pyperclip.copy(str(ans))
        return 0
if __name__ == "__main__":
    main()
