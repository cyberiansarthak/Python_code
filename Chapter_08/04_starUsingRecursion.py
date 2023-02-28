#STAR PATTERN USING RECURSION
inp =int(input("enter number of rows:\n"))   
#FUNCTION FOR Upper right triangle
def printfun(n):
    if( n==0 ):
        return 
    else:
        printfun(n-1)
        print(" * "*n)

printfun(inp) 
print("\n")
#FUNCTION FOR LOWER right TRIANGLE
def printfun(n):
    if( n==0 ):
        return 
    else:
         print(" * "*n)
    printfun(n-1)
       

printfun(inp)
#FUNCTION FOR LEFT SIDE RIGHT TRIANGLE
def printfun(n):
    if( n==0 ):
        return 
    else:
         print(" "*n-1)
         print(" * "*n)
    printfun(n-1)
       

printfun(inp)
