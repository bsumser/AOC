import re

if __name__ == "__main__":
    my_file = open("day3.txt", "r")
    inputList = my_file.readlines()

    right = 0
    treeCount = 0
    
    i = 0
    for i in range(len(inputList) - 1):
        right += 3
        if (right - 11 > 0):
            right -= 11
        #print("checking tree at row " + str(i) + " index " + str(right))
        print(inputList[i + 1][right])
        if (inputList[i + 1][right] == "#"):
            #print("tree")
            treeCount += 1
    print(treeCount)
