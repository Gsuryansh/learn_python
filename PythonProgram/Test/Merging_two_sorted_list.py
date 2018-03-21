a = [1,4,6,8,10,12,13,78]
b= [1,2,3,4,5,12,23,33,34]
c = []


while a and b:
    if a[0]<b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))

print(c+a+b)



#list.append() only append one element
#list.extend() will append a list in another list list
# li = [1,2,3,4]
# li1 = [5,6]
# li.extend(li1)
# print(li)