list = [2,3,4,5,4,3,23,24,6,18,72,9,135,7,150,49]

unique_element = set()
for i in list:
    unique_element.add(i)
special_element = set()
print(unique_element)

max_elemet = max(list)
print(max_elemet)

for value in unique_element:
    count = 2
    element = value
    while element<=max_elemet:
        element = value *count
        if element in unique_element:
            special_element.add(element)
        count+=1

print(special_element)
