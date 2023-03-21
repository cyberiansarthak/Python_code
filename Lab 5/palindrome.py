s = input("Enter a string ")
ans = s[::-1]

if ans:
	print("Yes")
else:
	print("No")

#METHOD 2
str = input("Enter a string ")

palin = True
for i in range(0, int(len(str)/2)):
    if str[i] != str[len(str)-i-1]:
        palin = False
    else:
        continue

if palin:
	print("Yes")
else:
	print("No")
