list = [56,34,76,3,4,9,2,3,90]
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            tem = list[j]
            list[j] = list[j+1]
            list[j+1] = tem
print(list)
