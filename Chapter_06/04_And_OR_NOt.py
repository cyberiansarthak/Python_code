#lOGICAL OPERETORS IN CONDISIONAL STATEMENT
A=[12,45,78,63,13]
Input0=int(input("enter first number\n"))
Input1=int(input("enter second number\n"))
if(Input0 and Input1 in A):
    print("Yeah buddy both number present in list")
elif(Input0 or Input1 in A):
    print("Only one number is present")    
else:
    print("None of these two present in our list")    
