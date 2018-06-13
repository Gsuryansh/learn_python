"""list = [99,35,3,4,5,5,5,5,53,2,4,5,6,7]
b = set()
ans = 0
for value in list:
    b.add(value) # here we are adding the unique value to the set b

for i in range(len(list)):

    if (list[i]-1) not in b: # here we are finding the starting of the sequence i.e if list[i]-1 is not in list that means this is the starting
                             # of the sequence
        j = list[i]
        while j in b:
            j+=1
        ans = max(ans,j-list[i])

print(ans)"""

"""Another way for the same program"""

list = [99,35,3,4,5,5,5,5,53,2,4,5,6,7]

list.sort()

length = 1

i = 0

while i < len(list)-1:

  print(i)
