# def insertion_sort(list):
#     for i in range(1,len(list)):
#         key = list[i]
#         j = i-1
#
#         while j>=0 and key < list[j]:
#             list[j+1] = list[j]
#             j-=1
#
#         list[j+1] = key
#     return list
#
# list = insertion_sort([18,25,23,12,11,9,7,45,6])
# print(list)
#


def insertion_sort(list):
    for i in range (1,len(list)):
        key = list[i]
        j = i-1

        while key < list[j] and j>=0:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = key
    return list
list = [1,8,5,8,49,99,45,67,34,34]


print(insertion_sort(list))























