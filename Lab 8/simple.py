a, b, c, i, j = [0, 4, 5, 9, 12, 22, 23], [1, 2, 7, 10, 11, 21, 34, 35], [], 0, 0

for x in range(0, len(a) + len(b)):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

    if i == len(a) or j == len(b):
        break

while i < len(a):
    c.append(a[i])
    i += 1
    
while j < len(b):
    c.append(b[j])
    j += 1
    
