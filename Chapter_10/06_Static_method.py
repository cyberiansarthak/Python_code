#SOMETIMES WE DONT'T WANT TO PASS (SELF) INSIDE OUR CLASS METHOD PARAMETER THEN WE USE STATIC METHOD

class StaticClass:
    @staticmethod               #this annotation is used to represents static method
    def isStatic_method():
        print("I am static method")


    @staticmethod                    # we can not use self parameter in static method
    def Static_method(self):                #this line throw an error
        print("I am static method")


StaticClass.isStatic_method()      # now we can use this method without passing any parameter
StaticClass.Static_method()    #this line throw an error

