"""This program to find wheather a string is rotational palindrom or not"""


def IsPalindrom(string):
    l=0
    h=len(string)-1
    while l<h:
        if string[l]!=string[h]:
            return False
        l+=1
        h-=1
    return  True
def IsRotationalPalindrom(string):
    if IsPalindrom(string):
        return True
    for i in range(len(string)-1):
        string1=string[i+1:len(string)]+string[0:i+1]
        print(string1)
        if IsPalindrom(string1):
            return True
    return False
string2="madami"
if IsRotationalPalindrom(string2):
    print("String is rotational palindrome")

else:
    print("String is not rotational palindrome")