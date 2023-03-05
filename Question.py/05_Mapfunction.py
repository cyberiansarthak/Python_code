#MAP FUNCTION
num = int(input("Enter the number to which you want squares from 1\n"))
#Square function
def Sq(a):
    return a*a
List=[] 
for i in range(1,num+1):
   List.append(i)
print(List)
result = map(Sq,List)
print(list(result))
