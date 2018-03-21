a={'ab':12,'z':23,'e':65}
b={'cd':34}
z=a.copy()#It will copy the content of a in the new dictonary z
z.update(b)#It will udate the content of z with b's content
print(z)
del z['e']#this will delet the mention value from the dictionary
print(z)
#z.clear()#it will clear all the value from the dictionary
#print(z)
#del z#it will delet the dictionary itself
#print(z)
"""You can not have more then one key in the dictionary"""
"""Dictionary keys are immutable"""
