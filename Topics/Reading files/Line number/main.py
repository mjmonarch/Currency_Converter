# read sample.txt and print the number of lines
with open('sample.txt', 'r') as file:
    print(len(file.readlines()))
