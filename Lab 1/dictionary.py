# Create a new dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Access an item in the dictionary
print(my_dict['name'])

# Get a list of all keys in the dictionary
print(list(my_dict.keys()))

# Get a list of all values in the dictionary
print(list(my_dict.values()))

# Get a list of all key-value pairs in the dictionary
print(list(my_dict.items()))

# Check if a key is in the dictionary
print('age' in my_dict)

# Add a new key-value pair to the dictionary
my_dict['occupation'] = 'Engineer'
print(my_dict)

# Update the value of an existing key in the dictionary
my_dict['age'] = 35
print(my_dict)

# Remove a key-value pair from the dictionary
del my_dict['city']
print(my_dict)

# Remove all key-value pairs from the dictionary
my_dict.clear()
print(my_dict)

# Get the length of the dictionary
print(len(my_dict))

# Check the data type of the dictionary
print(type(my_dict))
