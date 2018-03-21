import copy
li=[1,2,3]
a=copy.deepcopy(li)
li.append(9)
print(li)
print(a)

"""Deep copy means it will creat a new object in the memory and then copy the previous object in it
so if u change the original object it will not impact to the newily created object"""

"""Shallow copy means it will creat a link to the old object itself that means if make any changes in the old object it
will reflect to the new one also"""