prime_no=[]
number=2
while number<=100:
    temp=2
    while temp<=(number/2):
        if number%temp==0:
            break
        temp=temp+1
    if temp>(number/2):
        prime_no.append(number)
    number=number+1
print(prime_no)
