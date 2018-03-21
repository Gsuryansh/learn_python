"""This will count the number of times a digit present in the given number"""
# value=10000222333
# numlist=[]
# dic={}
# while value>0:
#     if (value%10) not in dic:
#         dic[value%10]=1
#     else:
#         dic[value%10]=dic[value%10]+1
#     value=value/10
# print(numlist)
# for num in numlist:
#     if num not in dic:
#         dic[num]=1
#     else:
#         dic[num]=dic[num]+1
# for val in dic:
#     print("number %d present %d times" %(val,dic[val]) )
############################################################################################################################
"""Here we have a dictionary with city and country here city is key and country is value
 so we will convert this in a dictionary whose key will be country and values will be list contains
 the city in that country"""

# from collections import defaultdict
# dictionary={'bangalore':'India','delhi':'India','Pune':'India','San Francisco':'US','LA':'US','Seoul':'Korea'}
# d1=defaultdict(list)
# for k,v in dictionary.items():
#     d1[v].append(k)
# print(d1)
#Note: Here defaultdict will creat a dictionary with no key and value of each key will be empty list when put any key.


"""Another way to solve the same problem"""

"""dictionary={'bangalore':'India','delhi':'India','Pune':'India','San Francisco':'US','LA':'US','Seoul':'Korea'}

d={}
for k,v in dictionary.items():
    d.setdefault(v,[]).append(k)
print(d)

#Note: setdefault will set the default value of key if that key is not present in the dictionary
#else it will return the key value."""

#######################################################################################################################

"""Program that will convert the list of integer in to dictionary where every one digit number will be under key value 1
 two digit number will be under key value 2"""

# li=[1,2,3,4,5,6,7,11,12,13,14,15,111,222,333,444,1111,2222,3333,11111,2222222,33333,44444,22222]
# dictionay={}
# for value in li:
#     dictionay.setdefault(len(str(value)),[]).append(value)
# print(dictionay)

#Dictionary can not have more then one key if it has it will overwrite the previous value
#Dictionary key should be immutable that means it can have string,integer,tupple as key but can not have list as key
#dict.has_key(key) will return true if dictionary has that key otherwise false
#dict.update(another dictionary) it will add value from another dictionary to the original one






