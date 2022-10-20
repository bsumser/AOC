def endLoop():
    raise StopIteration

if __name__ == "__main__":
    my_file = open("input.txt", "r")
    inputList = my_file.readlines()
    inputList = [x.strip("\n") for x in inputList]

    print(len(inputList[0]))

    length = len(inputList) - 1

    one = [0,0,0,0,0,0,0,0,0,0,0,0]
    zero = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(inputList) - 1):
        for j in range(0,12):
            if (inputList[i][j] == "1"):
                one[j] += 1
            if (inputList[i][j] == "0"):
                zero[j] += 1
    print(one)
    print(zero)

    output = 0

    for i in range(0,12):
        if (one[i] < zero[i]):
            inputList = list(filter(lambda x: x[i] == '1', inputList))
        #elif (zero[i] > one[i]):
        #    inputList = list(filter(lambda x: x[i] == '0', inputList))


    #output = 0b100011100101 * 0b011100011010
    output = int(0b100011100101) * int(0b011101011110)
    print(output)
    for i in range(0,len(inputList)):
        print(inputList[i])