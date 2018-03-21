a="abcde"

b='abcdt'


if len(a)!= len(b):
    print("String not equal")
    exit(0)
start =0
for value in a:
    if value == b[start]:
        start +=1
        continue
    else:
        break
if start < len(b):
    print("String are not same")

else:
    print("String are the same")


