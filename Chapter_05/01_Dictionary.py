# DICTIONARY IS THE SET OF KEY-VALUE PAIR
#CHARCTERISTICS
#MUTABLE
#CAN NOT CONTAIN DUPLICATE KEYS
#INDEXED
#UNORDERED

#CREATION
Dict ={
    "Name":"sarthak khare",
    "Age":18,
    "Blood group":"0 +ve "
}

#PRINTING
print(Dict["Name"]) #by key
print(Dict) #by dICtionary name


#LIST INSIDE A DICTIONARY
Dict_01 ={
    "Name":"sarthak khare",
    "Scholar number":31978,
    "Marks":[45,65,78,98,12]
}

#PRINTING
print(Dict_01) #by name
print(Dict_01["Marks"])# by key
print(Dict_01["Marks"][0])# print the list element


#DICTIONARY INSIDE A DICTIONARY
Dict__02={
    "Name":"sarthak khare",
    "Scholar number":31978,
    "Marks":{
        "Maths":50,
        "English":75,
        "Science":48
    }

}

#PRINTING
print(Dict__02)#by name
print(Dict__02["Marks"])# by key
print(Dict__02["Marks"]["Maths"])# by key of inside dictionary


