#READLINE
f = open("sample.txt","r")        # it take to parameter file name and mode

#READ FIRST LINE
data = f.readline()                  
print(data)  

# READ SECOND LINE
data = f.readline()                  
print(data) 

#READ THIRD LINE
data = f.readline()                  
print(data)                     
f.close()                         # after reading close the FILE 