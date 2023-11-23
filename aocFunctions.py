#!/usr/bin/env python3

def char_val(char, offset):
    # function that returns a value for a char based on its ascii code
    # offset of 96 will return a = 1, b = 2, etc
    # offset of 38 will return A = 27, B = 28, etc
    # this could be extended for any ascii char and offset
    ans += ord(char) - offset
    print(char + " " + str(ord(char) - offset))
    return ans

def string_split(string, split):
    # function to split a string into however many parts
    # returns a list of strings
    firsthalf, secondhalf = line[:len(line)//2], line[len(line)//2:]

    stringList += firsthalf
    stringList += secondhalf


def intersect(input_list):
    # function to find intersection of all words in a list
    # takes a list as parameter and returns a string
    intersect = ''
    for word in input_list:
        intersect = set(word).intersection(intersect)
        print(intersect)
    return intersect


def print_2dlist_no_sep(input_list):
    """Function to print a 2d list without seperators.
    Useful for displaying grids as ascii map

    [[file:~/AOC/2021/day5.py][Used in AOC 2022 day 5]]
    """
    for line in input_list:
        print(*line, sep='')
    print("\n\n")

def plot_to_grid(grid, point1, point2):
    """function that accepts a grid as a 2dlist and plots lines on it
    from point1 to point2

    [[file:2021/day5.py][used in AOC 2022 day 5]]
    """

    x1 = point1[0]
    x2 = point1[1]
    y1 = point2[0]
    y2 = point2[1]

    coords = []

    print("line is: %d,%d to %d,%d" % (x1, y1, x2, y2))

    if (x1 != x2 and y1 != y2):
        if (y1 < y2 and x1 < x2):
            print("top-left bot-right diag")
            y_list = [i for i in range (y1, y2+1)]
            x_list = [i for i in range(x1, x2+1)]
            coords = tuple(zip(x_list, y_list))
            print(coords)
        elif (y1 > y2 and x1 > x2):
            print("top-left bot-right diag")
            y_list = [i for i in range (y2, y1+1)]
            x_list = [i for i in range(x2, x1+1)]
            coords = tuple(zip(x_list, y_list))
            print(coords)

        elif (y1 > y2 and x1 < x2):
            print("bot-left top-right diag")
            y_list = [i for i in range (y1, y2-1, -1)]
            x_list = [i for i in range(x1, x2+1)]
            coords = tuple(zip(x_list, y_list))
            print(coords)

        elif (y1 < y2 and x1 > x2):
            print("bot-left top-right diag")
            y_list = [i for i in range (y1, y2+1)]
            x_list = [i for i in range(x1, x2-1, -1)]
            coords = tuple(zip(x_list, y_list))
            print(coords)
        else:
            print("diag case missed")

    elif (x1 == x2 and y1 < y2):
        y_list = [i for i in range (y1, y2+1)]
        x_list = [x1 for i in range(0, len(y_list))]
        coords = tuple(zip(x_list, y_list))
        print("case 1")
        print(coords)

    elif (x1 == x2 and y1 > y2):
        y_list = [i for i in range (y2, y1+1)]
        x_list = [x1 for i in range (0, len(y_list))]
        coords = tuple(zip(x_list, y_list))
        print("case 2")
        print(coords)

    elif (y1 == y2 and x1 < x2):
        x_list = [i for i in range (x1, x2+1)]
        y_list = [y1 for i in range(0, len(x_list))]
        coords = tuple(zip(x_list, y_list))
        print("case 3")
        print(coords)

    elif (y1 == y2 and x1 > x2):
        x_list = [i for i in range (x2, x1+1)]
        y_list = [y1 for i in range(0, len(x_list))]
        coords = tuple(zip(x_list, y_list))
        print("case 4")
        print(coords)

    for coord in coords:
        grid[coord[1]][coord[0]] += 1
