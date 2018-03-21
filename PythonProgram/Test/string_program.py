st="aaaaaaaabbbbcccchhhgggdddtttaaabbbcccd"
output=""
count=0
temp=""

for value in st:
    if count == 0:
        temp = value
        count=count+1
    else:
        if value in temp:
            count=count+1
        else:
            output=output+str(count)+temp
            temp=value
            count=1
output=output+str(count)+value
print(output)