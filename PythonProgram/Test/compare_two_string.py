string = "#suryansh ursyansh#"
string1 = string.split(" ")[0]
string2 = string.split(" ")[1]

dict1 = {}
dict2 = {}

if len(string1) != len(string2):
    print("String are not same")
    exit(1)

for i,j in zip(string1,string2):
    dict1[i] = dict1.get(i,0)+1
    dict2[j] = dict2.get(j,0)+1

if cmp(dict1,dict2) == 0:
    print("String are same")
else:
    print("String are not same")
