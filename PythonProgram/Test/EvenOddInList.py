l=[1,2,3,4,5,6,7,8,9]
for i in range(len(l)):
    if l[i]%2 == 0:
        temp = l.pop(i)
        l.append(temp)

print(l)