list1 = [10, 20, 30, 40, 50, 60]
list2 = [10, 20, 30, 50, 40, 70]

if len(list1) == len(list2):
    list1.sort()
    list2.sort()

    equal = True
    for a in range(0, len(list1)):
        if list1[a] == list2[a]:
            continue
        else:
            equal = False

    if equal:
        print("Both lists are equal")
    else:
        print("Lists are not equal")

else:
    print("Lists are not equal")
