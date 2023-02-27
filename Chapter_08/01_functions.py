#FUNCTION IS SET OF SOME STATEMENT FOR PERFORMING SOME TASK
#PERCENTAGE  OF MARKS OF STUDENTS

#METHOD 1
marks_01 =[45,78,96,56]
marks_02 =[78,36,45,91]
percentage_01 =(marks_01[0]+marks_01[1]+marks_01[2]+marks_01[3])/4
percentage_02 =(marks_02[0]+marks_02[1]+marks_02[2]+marks_02[3])/4
print(percentage_01,percentage_02)
#Note: if there are n numbers of marks list then from above we are not calculate percentage easily

#METHOD 2
#USING FUNCTIONS
def percentage(marks): #WE CREATE THIS FUNCTION TO SOLVE ABOVE PROBLEM OF REPEATATION
    return sum(marks)/4 # SUM IS ALSO A IN BUILT FUNCTION
Girls_marks =[78,87,98,89]
Boys_marks =[45,54,65,56]
percentage_girls =percentage(Girls_marks)# THIS IS FUNCTION CALLING
percentage_boys = percentage(Boys_marks)# THIS IS FUNCTION CALLING
print(percentage_boys,percentage_girls)

