import pyperclip #module for copying to clipboard
import re
from aocd import get_data #module for automating advent of code data get

inputData = get_data(day=4, year=2020)

data = [str.strip() for str in inputData.split("\n\n")] #split into list
data = [str.replace('\n', ' ') for str in data] #split into list
#data = [str.split(' ') for str in data] #split into list
data = list(filter(bool, data)) #remove empty strings

print("Data Received")
print(data)

#---------------Part 1-------------------#
matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

ans = 0

for line in data:
    if all(match in line for match in matches):
        if re.search("byr:(192[0-9]|19[3-9][0-9]|20[01][0-9]|2020)",line):
            if re.search("iyr:(201[0-9]|2020)",line):
                if re.search("eyr:(202[0-9]|2030)",line):
                    if re.search("hgt:(15[0-9]|1[6-8][0-9]|19[0-3])cm", line) or re.search("hgt:(59|6[0-9]|7[0-6])in", line):
                        if re.search("hcl:#([a-f0-9]{6}|[a-f0-9]{6})", line):
                            if re.search("ecl:amb", line) or re.search("ecl:blu", line) or re.search("ecl:brn", line) or re.search("ecl:gry", line) or re.search("ecl:grn", line) or re.search("ecl:hzl", line) or re.search("ecl:oth", line):
                                if re.search("pid:([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])", line):
                                    print(line)
                                    ans += 1
#---------------Part 2-------------------#

ValidPassports = 0
for passport in data:
    if (re.search(r"byr:19[2-9]\d|byr:200[0-2]", passport) and re.search(r"eyr:202\d|eyr:2030", passport) and
            re.search(r"iyr:201\d|iyr:2020", passport) and re.search(r"hgt:1[5-8]\dcm|hgt:19[0-3]cm|hgt:59in|hgt:6\din|hgt:7[0-6]in", passport) and
    re.search(r"hcl:#[a-z0-9]{6}", passport) and re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) and re.search(r"pid:\d{9}\b", passport)):
        ValidPassports += 1

print(len(data))
print(ValidPassports)
pyperclip.copy(str(ValidPassports))
