def bubble_sort(list):
    for index,value in enumerate(list):
        try:
            if list[index+1]<value:
                temp = value
                list[index] = list[index+1]
                list[index+1] = temp
                bubble_sort(list)
        except IndexError:
            pass
    return list

sorted_list=bubble_sort([1,8,4,7,56,83,23,89,34,54])
print(sorted_list)

# def bubble_sort(listt):
#     for i, num in enumerate(listt):
#         try:
#             if listt[i + 1] < num:
#                 listt[i] = listt[i + 1]
#                 listt[i + 1] = num
#                 bubble_sort(listt)
#         except IndexError:
#             pass
#     return listt


# listt = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(listt)