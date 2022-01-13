with open("test.txt", "r") as reader:
    for line in reader.readlines():
        print(line[0])
