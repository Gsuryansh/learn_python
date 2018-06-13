string = "ABCab[c^&^%$#(dZ"
newstring  = ""
for value in string:

    if ord(value)<ord("a") and ord(value)>=ord("A") and ord(value) not in range(91,97):
        newstring += chr(ord(value)+32)

    elif ord(value)>=ord("a") and ord(value)<=ord("z"):
        newstring += chr(ord(value)-32)

    else:
        newstring += value

print(newstring)