# main.py
import sys

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    my_file = open(sys.argv[1], "r")
    content_list = my_file.readlines()
    content_list = list(map(int, content_list))

    count = 0

    while i < len(content_list):
        if (sum(content_list[i:i+3]) < sum(content_list[i+1:i+4])):
            count+=1
        i += 1
    print(count)