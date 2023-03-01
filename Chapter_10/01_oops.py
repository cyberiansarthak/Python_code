#OBJECT ORIENTED PROGRAM
#SOLVING A PROBLEM BY CREATING OBJECTS IS ONE OF THE MOST POPULAR APPROCHES IN PROGRAMMING.
#THE CONCEPT FOCUS ON DRY PRINCIPLE

#CLASS 
#A CLASS IS A BLUEPRINT FOR CREATING OBJECTS
#Write the program to add two numbers

#Procedural method
a=12
b=45
print(a+b)



#Object-oriented method
class Number:
    def sum(self):
        return self.a +self.b
    
num = Number()
num.a =12
num.b=13
s=num.sum()
print(s)    