import re
import pyperclip
from itertools import combinations
from aocd import get_data  # module for automating advent of code data get


def main():
    input_data = get_data(day=10, year=2020)

    data = [line.strip() for line in input_data.split("\n")]  # split into list
    data = [int(line) for line in data]
    # data = [16,10,15,5,1,11,7,19,6,12,4]
    maxJolt = 3 + max(data)
    data.insert(0, 0)
    data.append(maxJolt)
    data.sort()
    print("data Received")
    print(data)
    ans = 0
    oneJolt= 0
    threeJolt = 1
    currentAdapter = 0

    # ---------------Part 1------------------- #
    #for i in range(0, len(data)):
    #    if (data[i] - currentAdapter == 1):
    #        oneJolt += 1
    #    elif (data[i] - currentAdapter == 3):
    #        threeJolt += 1
    #    currentAdapter = data[i]

    #ans = oneJolt * threeJolt
    # ---------------Part 2------------------- #
    adj_matrix = [[0] * 5] * 5

    #initialize adjacency matrix to 0
    #loop and fill adjacency matrix
    #find all paths from 0 to maxJolt

    for i in range(0, 5):
        for j in range(0, 5):
            print(data[j], "-", data[i], "=", data[j] - data[i], sep=" ")
            if 0 < (data[j] - data[i]) <= 3:
                adj_matrix[i][j] = 1
            else:
                adj_matrix[i][j] = 0

    print(len(data))
    print('My list:', *adj_matrix, sep='\n- ')
    print(adj_matrix)
    print(ans)
    pyperclip.copy(str(ans))
    return 0


main()
