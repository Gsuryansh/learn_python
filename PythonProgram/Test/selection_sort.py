""" """

list = [ -634 ,-524 ,-5, 4 ,42, 2643, 23, -9520, 1852 ,3, -510, -510, 3, 3, 3, 15]
print("printing length of unsorted list {}".format(len(list)))

for i in range(len(list)-1):
    min_index = i
    for j in range(i+1 , len(list)):
        if list[min_index]>list[j]:
            min_index = j

    list[i],list[min_index]=list[min_index],list[i]

print("Printing length of sorted list {}".format(len(list)))
print(list)
