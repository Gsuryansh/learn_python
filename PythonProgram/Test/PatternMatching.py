st="abbcaabc"
temp=''
for value in st:
    if value in temp:
        print(temp)
        temp = value
    else:
        temp=temp+value
print(temp)