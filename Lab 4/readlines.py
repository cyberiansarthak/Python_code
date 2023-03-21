file = open("Lab 4/demofile.txt", 'r')
Lines = file.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
