""" it will arrange the element of the list according to there index if element is not present for the respective index then it will be mark as
  -1 """
list = [2,5,7,9,0,1,45,56,67,10,8,3]

unique_element = set()
for i in list:
    unique_element.add(i)


for value in range(len(list)):
    if value in unique_element:
        list[value] = value
    else:
        list[value] = -1


print(list)


