#!/usr/bin/env python3
import time
import sys
import re
import math
sys.path.append('../')
import saoc
from functools import reduce
import operator
import itertools

def silver(data):
    print("silver starting----reading %d lines of data" % len(data))
    ans = 0

    files = []
    file_id = 0
    total_files = 0
    for idx in range(0, len(data), 2):
        file_count = data[idx]
        while file_count > 0:
          files.append(str(file_id))
          total_files += 1
          file_count -= 1

        if idx + 1 < len(data) - 1:
          space_count = data[idx+1] 
          while space_count > 0:
            files.append(".")
            space_count -= 1
        file_id += 1
    print(total_files)

    ptr = 0
    for i in range(len(files) - 1, 0, -1):
        cur_file = files[i]
        if cur_file != '.':
          while(files[ptr] != "."):
            ptr += 1
          files[i], files[ptr] = files[ptr], files[i]
        if len(set(files[total_files:-1])) == 1:
           break
    print("".join(files))

    for i in range(0, total_files):
       ans += i * int(files[i])
    print("silver answer is: %d\n" % ans)
    return ans

def gold(data):
    print("gold starting----reading %d lines of data" % len(data))
    ans = 0
    files = []
    D = [(None if i%2 else i//2, int(d)) for i,d in enumerate(open('day9s.txt').read())]
    print(D)

    for i in range(len(D), 0, -1):
      for j in range(0, len(D)):
        i_data, i_size = D[i]
        j_data, j_size = D[j]

        #swap blocks
    
    print("Gold answer is: %d\n" % ans)
    return ans

def check_sum(files):
  ans = 0
  for i in range(0, len(files)):
    if files[i] != '.':
      ans += i * int(files[i])
  return ans 

def find_space(files, size, chunk, chunk_s, chunk_e):
  space = ['.' for _ in range(size)]
  for i in range(0, len(files)):
    if files[i:i+size] == space and i < chunk_e:
      return (space, i, i+size)
  return ([], -1, -1)

def find_chunk(files, size, chunk):
  for i in range(len(files), 0, -1):
    cur = files[i-size+1:i+1]
    if cur == chunk:
      return (i-size+1, i+1)

def update_file(files, chunk):
  swap = ['.' for _ in range(len(chunk))]
  for i in range(len(files), 0, -1):
    cur = files[i-len(chunk):i]
    if cur == chunk:
      files[i-len(chunk):i] = swap
      return files


def find_chunks(files):
  chunks = []
  cur_chunk = [files[0]]
  chunk_dict = {}
  for i in range(1, len(files)):
    if (files[i] == files[i-1]):
       cur_chunk.append(files[i])
    else:
      chunks.append(cur_chunk)
      cur_chunk = [files[i]]
  chunks.append(cur_chunk)
  return chunks


def parse_data():
    start_time = time.time()
    # open file and read in data
    print(f"parsing data for {sys.argv[1]}")
    data = open(sys.argv[1], "r").read().strip("\n")
    
    # ALL numbers to 2d list
    #data = [re.findall(r'\d+', line) for line in data]
    #data = [list(line) for line in data if line]
    #data = [[int(val) for val in line] for line in data]

    #split on every char 
    data = list(data)
    data = [int(val) for val in data]

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
