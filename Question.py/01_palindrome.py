# function which return reverse of a string
#with the help of slicing
def isPalindrome(s):
	return s == s[::-1]
#with the help of for loop
def isPalindrome_01(s):
    for 

#Take input from user
s = input("enter the string\n")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
