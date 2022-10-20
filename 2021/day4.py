if __name__ == "__main__":
    my_file = open("day4.txt", "r")
    inputList = my_file.read()
    inputList = inputList.split('\n\n')
    inputList = [x.replace("\n", " ") for x in inputList]

    for i in range(len(inputList)):
        print(inputList[i])