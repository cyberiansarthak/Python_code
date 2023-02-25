#WE MUST BE ABLE ABLE TO EXECUTE INSTRUCTIONS ON A CONDITIONS BEING SET THIS IS WHAT CONDITIONAL ARE FOR!
#IF ,ELSE AND ELIF
Age = 18
inpt = int(input("Enter your age\n"))
#This all condition are executed one after another 
if(inpt<Age):
    print("You are not eligible for voting")
elif(inpt==Age):
    print("You are eligible for voting ,now you can registerd for voting card")     
else:
    print("You are eligible for voting")        
