def DecimalToBinary(number):
    binary=0
    temp=1
    while number>0:
        binary=binary+(number%2)*temp
        number=number/2
        temp=temp*10
    return binary
value=DecimalToBinary(15)
st=str(value)
strev=st[::-1]
if st==strev:
    print("Number is binary palindrome")

else:
    print("Number is not binary palindrome")

