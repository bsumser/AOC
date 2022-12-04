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


def intersect(list):
    # function to find intersection of all words in a list
    # takes a list as parameter and returns a string
    intersect = ''
    for word in list:
        intersect = set(word).intersection(intersect)
        print(intersect)
    return intersect
