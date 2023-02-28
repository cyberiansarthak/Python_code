#A FILE IS A DATA STORED IN A STORAGE DEVICE ,
#A PYTHON PROGRAM CAN TALK TO THE FILE BY READING CONTENT FROM IT AND WRITING CONTENT TO IT

#TYPES OF FILE
#1. TEXT FILE (.TXT,.C,.PY)
#2. BINARY FILE(.JPG,.DAT)


#OPENING FUNCTION
f = open("sample.txt","r")        # it take to parameter file name and mode
data = f.read()                   # use read method to read the file content
print(data)                       # print the content
f.close()                         # after reading close the 

#Note: by default the mode is read