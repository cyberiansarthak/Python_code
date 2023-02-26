#IN WHILE LOOP FIRST CHECK CONDITION IF CONDITION IS TRUE THEN CODE INSIDE WHILE LOOP IS EXECUTED,OTHERWISE NOT
i = 0
while i<10:   # so in the first step it check condition (in this case it is true)
    print("yes " +str(i)) # then execute the print statement
    i=i+1                 # it help to not form a infinte while loop()


#Note: if the condition is always true then it will create infinte loop
# in the above case if we not increase the value of i then it always less then 10.