#take input string from user
s = input("enter the string\n")
#take lenth of string using len function
length = len(s)

rev = -1
for x in range(length):
   if(s[x]==s[rev]):
     x+=1
     rev -=1
   else:
    print(s,"is not a palindrome")
    break
else:
    print(s, "is a palindrome")    



