#Greeting function
def greet(name):
    print("good morning "+name)
greet("Sarthak")    #Function calling

#deafult parameter in function calling
def greet_02(name ="sarthak"):
    print("Good moring "+ name)
greet_02() # IF WE ARE NOT PASSING ANY PARAMETER THEN IT TAKE DEFAULT PARAMETER
greet_02("Shrashti")    