my_tuple = [1, 2, 3, 4, 5]

my_list = list(my_tuple)

my_list.remove(3)
print(my_list)

my_list.append(6)
print(my_list)

print(len(my_list))

popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list.insert(2, 3)
print(my_list)

my_list.clear()
print(my_list)

print(type(my_list))

my_tuple = tuple(my_list)
print(my_tuple)