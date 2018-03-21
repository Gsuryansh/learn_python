def RemoveSpaces(string):
    temp=""
    for char in string:
        if char==" ":
            continue
        temp=temp+char
    return temp
string="Suryansh Gupta"
print(RemoveSpaces(string))