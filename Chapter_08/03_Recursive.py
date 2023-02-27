#Factorial 
# n!= 1*2*3*4.......*n
# n! = {1*2*3*4....n-1}*n
# n1 = n-1! *n
# IN RECURSIVE FUNCTION WE RECALL THE FUNCTION INSIDE THE FUNCTION
def Factorial_recursive(n):
    if (n==0 or n==1): # BASE CONDITION
        return 1
    return n*Factorial_recursive(n-1)
INPUT= int(input("ENTER THE NUMBER\n"))
print(Factorial_recursive(INPUT))