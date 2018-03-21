li=[1,2,3,4,5,6,17,53,78,79,81,23,101]
prime=[]
for value in li:
    temp=2
    if value<=1:
        continue
    else:
        while temp<=(value/2):
            if value%temp==0:
                break
            temp+=1
        if temp>(value/2):
            prime.append(value)
print(prime)
