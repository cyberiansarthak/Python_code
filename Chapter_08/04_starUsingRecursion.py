#STAR PATTERN USING RECURSION
inp =int(input("enter number of rows:\n"))   
#FUNCTION FOR Upper triangle
def printfun(n):
    if( n==0 ):
        return 
    else:
        printfun(n-1)
        print(" * "*n)

printfun(inp) 

#FUNCTION FOR LOWER TRIANGLE
def printfun(n):
    if( n==0 ):
        return 
    else:
         print(" * "*n)
    printfun(n-1)
       

printfun(inp)

