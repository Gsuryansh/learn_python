li = [1,2,3,4,5,6,5,4,3,6,5,1,1,9,8,7,8,9]
value = 0
while value < len(li)-1:
    j = value+1
    while j < len(li):
        if li[value] == li[j]:
            li.pop(j)
            continue
        j+=1
    value+=1
print(li)

