# main.py
import sys
def convertList(list):
    list = my_file.readlines()
    list = map(lambda split_str: split_str.split(" "), list)
    list = map(lambda strip_str: strip_str.strip, list)
    #list = map(lambda split_str: split_str.split(" "), list[0])

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    my_file = open(sys.argv[1], "r")
    
    horizontal = 0
    depth = 0
    aim = 0
    i = 0

    List = my_file.readlines()
    List = map(lambda split_list: split_list.strip("\n").split(" "), List)

    newList = list(List)
    
    print(newList)
    
    while i < len(newList):
        if (str(newList[i][0]) == "forward"):
            horizontal += int(newList[i][1])
            depth += (aim * int(newList[i][1]))
        if (str(newList[i][0]) == "down"):
            aim += int(newList[i][1])
            #depth += int(newList[i][1])
        if (str(newList[i][0]) == "up"):
            #depth -= int(newList[i][1])
            aim -= int(newList[i][1])
        i+= 1
    print(horizontal)
    print(depth)
    print(depth * horizontal)
