#METHODS OF DICTIONARY
Dict__02={
    "Name":"sarthak khare",
    "Scholar number":31978,
    "Marks":{
        "Maths":50,
        "English":75,
        "Science":48
    }

}

#PRINTING THE  KEYS & VALUES IN LIST OF A DICTIONARY
print(list(Dict__02.keys()))# print of list of keys
print(list(Dict__02.values()))#print the list of values

#PRINTING THE VALUES & KEYS (ALTERNATE METHOD)
print(Dict__02.values())
print(Dict__02.keys())

#PRINTING (Key,value) BY (ITEMS KEYWORD)
print(Dict__02.items())

#UPDATE DICTIONARY
updatedictionary={
    "Age":18,
    "Marks":{
        "Maths":77# remove english and science marks and update only maths marks

    }
}
Dict__02.update(updatedictionary)
print(Dict__02)

#GET METHOD
print(Dict__02["Name"])
print(Dict__02.get('Name')) # it's seems like to be same as normal print method 
print(Dict__02["name"]) # but the normal through an error when the key is not present
print(Dict__02.get('name'))# and get method does not get any error
