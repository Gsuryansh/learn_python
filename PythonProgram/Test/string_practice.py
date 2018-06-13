# a = "Suryansh"
#
# a = a[::-1]
# print(a.capitalize())

"""Programe to reverse the string"""
# st = "welcome"
# li = list(st)
# start = 0
#
# end = len(st)-1
#
# while start<end:
#     temp = st[start]
#     li[start] = li[end]
#     li[end] = temp
#     start+=1
#     end-=1
# st = ''.join(li)
# print(st)

""" First way to extract gmail from the string """
st = "gupta.surya123@gmail.com"

print(st.split("@")[1].split(".")[0])

""" Second way to extract gmail from the string """
st1 = "gupta.surya123@gmail.com"
start_index = st1.find("gmail")
print(st1[start_index:start_index+5])