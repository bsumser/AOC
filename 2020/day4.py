if __name__ == "__main__":
    my_file = open("day4.txt", "r")
    inputList = my_file.read()
    inputList = inputList.split('\n\n')
    inputList = [x.replace("\n", " ") for x in inputList]
    inputList = [x.split(" ") for x in inputList]
    #inputList = list(tuple(map(int, x.split(', '))))
    inputList = [[c.split(":") for c in row] for row in inputList]

    for i in range(len(inputList)):
        #if ("byr" && "iyr" && "eyr" && "hgt" && "hcl" && "ecl" && "pid") in inputList[i]:
            print(inputList[i])

