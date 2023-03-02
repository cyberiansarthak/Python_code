#ABSTRACTION
#OBJECT OF A GIVEN CLASS CAN INVOKE THE METHOD OF IT WITHOUT KNOWING THE IMLPLENTATION .

class Student:          #create a class student which have nothing inside it.
    pass


if(Student.marks()):   #in this line we call a method of Student class name as (marks()),
    print(marks)       # but you clearly see there is no method present in our Student class
                       # This is known as abstraction we don't want to know about the class methods just call it.


