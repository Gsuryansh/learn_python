"""Below program will convert a list in to dictionary using dictionary comprehension"""

# li=[1,2,3,4,5,1]
# dic={x:x*2 for x in li}
# print(dic)
#######################################################################################################
"""Creating dictionary using dictionary comprihension if key and value comes from different list example below"""

# key=['a','b','c']
# value=[1,2,3]
#
# new_dictionary={x:k for x,k in zip(key,value)}
# print(new_dictionary)

###########################################################################################################

"""Initialising dictionary usnig different method"""
# key=['a','b','c','a']
# dictionary={}.fromkeys(key,0)#It will creat a dictionary with key in sequence and default
#                                # value is None if we will not provide any value
# print(dictionary)

#Note: fromkeys will creat a dictionary with key taken from the sequence and default value will be whatever we will
#provide in the second parameter if we provide noting then default value will be None

"""Program to count number of word in a sentence"""

"""sentence="my name is suryansh gupta my name is"
word=sentence.split(" ")
count_dict={}.fromkeys(word,0)
for value in word:
    count_dict[value]+=1
print(count_dict)"""

#####################################################################################

"""Another to creat same program"""

"""sentence="my name is suryansh gupta my name is"
word=sentence.split(" ")
count_dict={}
for value in word:
    count_dict[value]=count_dict.get(value,0)+1#here get will give you the value of key in dictionary if present
                                               #if not present then it will give whatever u will give in second parameter
print(count_dict)
print(count_dict.keys())#It will return the list of keys in the dictionary
print(count_dict.values())#It will return the list of values"""

"""Another way to create same program"""
# sentence="my name is suryansh gupta my name is"
# word=sentence.split(" ")
# count_dict={x:0 for x in word}
# for value in word:
#     count_dict[value]+=1
# print(count_dict)
# print(count_dict.items())



