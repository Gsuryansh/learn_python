number=1234567
reverse_number=0
while number>0:
    temp=number%10
    number=number/10
    reverse_number=reverse_number*10+temp
print(reverse_number)