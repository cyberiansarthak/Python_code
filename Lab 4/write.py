f = open("Lab 4/demofile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

f = open("Lab 4/demofile.txt", "r")
print(f.read())
