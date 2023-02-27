#STAR PATTERN USING RECURSION
#FUNCTION FOR ROWS
def printfun(n):
    if( n==0 ):
        return 
    else:
        printfun(n-1)
        print(" * "*n)
inp =int(input("enter number of rows:\n"))     
printfun(inp)

