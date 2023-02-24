#ADD ELEMENT TO SET
Set =set() # empty set
Set.add(4)
Set.add(5)
Set.add(5)# it can not add to set again because set is non repeating
Set.add(6)
Set.add(7)
print(Set)


#REMOVE ELEMENT FROM SET
Set.remove(4)
print(Set)

#POP FROM SET
print(Set.pop())# it remove one elemnt from set and return the value
print(Set)

#LENGTH
print(len(Set))

#UNION
Set_01=Set.union({1,2,4,5})
print(Set_01)

#INTERSECTION
print(Set_01.intersection(Set))

#CLEAR
Set.clear()
print(Set)