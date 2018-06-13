list = [1,2,3,4,6,7,9,9,9,8,8,8]
i = 0
while i< len(list)-1:
    j = i+1
    if list[i]%2 != 0 and list[j]%2 == 0:
        list[i],list[j] = list[j],list[i]
        i = j+1

    elif list[i]%2 == 0 and list[j]%2 != 0:
        i = j + 1

    elif list[i]%2 == 0 and list[j]%2 == 0:
        for k in range(j+1,len(list)):
            if list[k]%2 != 0:
                list[j],list[k] = list[k],list[j]
                i = j+1
                break
    else:
        for k in range(j + 1, len(list)):
            if list[k]%2 == 0:
                list[i],list[k] = list[k],list[i]
                i = j+1
                break

print(list)