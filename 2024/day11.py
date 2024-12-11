#!/usr/bin/env python3
import time
import sys
sys.path.append('../')
from saoc import coord_check_grid

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0
    iter = 25
    while(iter):
        for i in range(0, len(data)):
            cur = data[i]
            if cur == 0:
                print(f"0 on {cur}")
                data[i] = 1
            elif len(str(cur)) % 2 == 0:
                print(f"even on {cur}")
                cur = str(cur)
                size = len(cur) // 2
                first = int(cur[0:size])
                second = int(cur[size:])
                print(f"{first}, {second}")
                data[i] = first
                print(data)
                data.insert(i+1, second)
                print(data)
                i += 3
            else:
                print(f"other on {cur}")
                data[i] *= 2024 
        iter -= 1
        print(data)
        time.sleep(2)
    ans = len(data)



    print("silver answer is: %d\n" % ans)
    return ans

def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0


    
    print("Gold answer is: %d\n" % ans)
    return ans

def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().strip("\n")
    
    # ALL numbers to 2d list
    #data = [re.findall(r'\d+', line) for line in data]
    data = data.split(" ")
    data = [int(val) for val in data]

    #split on every char 
    data = list(data)
    #data = [int(val) for val in data]

    print(data)
    print("Parsing done in %s seconds" % (time.time() - start_time))
    return data

def main():
    # ---------------Part 1------------------- #
    silver(parse_data())
    # ---------------Part 2------------------- #
    gold(parse_data())

    return 0

if __name__ == "__main__":
    main()
