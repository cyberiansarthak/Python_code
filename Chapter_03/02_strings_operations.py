#CONCATING TWO STRINGS
a = "hello"
b = " i am sarthak"
c = a+b
print(c)

#SLICING
name = "my name is sarthak khare"
print(name[1:2]) #first index is the starting index second is for ending
print(name[:6])#if we blanked first index then it's auto take 0
print(name[0:])#if we blanked second index then it auto take it from the last of the string
print(name[0::2])#third index is for skiping any charcter of the string

#LENGTH
name = "my name is sarthak khare"
print(len(name))

#STRING ENDS WITH
name = "my name is sarthak khare"
print(name.endswith("khare"))

#STRING COUNT
name = "my name is sarthak khare"
print(name.count("a"))

#STRING CAPITALIZE
name = "my name is sarthak khare"
print(name.capitalize())

#STRING FIND CHARACTERS 
name = "my name is sarthak khare"
print(name.find("is"))

#STRING REPLACE
name = "my name is sarthak khare"
print(name.replace("my name is","i am"))




