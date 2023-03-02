#CLASS 
#A CLASS IS A BLUEPRINT FOR CREATING OBJECTS
#syntax
class PascalConvention_name:     #class creation
     name ="sarthak"             #class variable
     def isPrint(self):                  #class method(use camel convention)
        return print(self.name),print(self.branch)


#OBJECT
#AN OBEJCT IS A INSTANTIATION OF A CLASS .WHEN CLASS IS DEFINED, 
# A TEMPLATE(INFO) IS DEFINED MEMORY IS ALLOCATED ONLY AFTER OBJECT CREATE.
#syntax
Student = PascalConvention_name() #object creation 
Student.name="Dev"                #instance variable
Student.branch="icb"              #instance variable
Student.isPrint()


#MODELLING A PROBLEM IN OOPS
#class -->Employee(noun)
#Attributes --> name,age,salary(adjective)
#methods --->Salary()(verb)
class Employee:                                  #Class
    name ="Sarthak"
    age =18                                      #Attributes
    Salary =50000
    def Salary(self):                            #Methods
        print("Salary of employee :",self.Salary)

     

