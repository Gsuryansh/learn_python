# value = 7
# total = 0
# for i in range(1,value+1):
#     total = total + sum(range(i+1))
# print(total)

# def seriessum(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i * (i + 1) / 2
#     return sum
#
#
# class abc(object):
#     class_variable = 10# class variable
#
#     def __init__(self):
#         self.class_variable =11 # it will creat instance variable because we are accessing it through instance
#         abc.class_variable = 12 # it will change the class_variable to 12 because it is accessing through class
#
#
# obj = abc()
# print(obj.class_variable)# it will print 11 because under __init__ we have creat a instance variable by accessing class_variable through self
# print(abc.class_variable) # it will print 12 because we are accessing it through class ie abc

# NOTE: if we comment out self.class_variable in __init__ then obj.class_variable will access the class variable itself

def reverse_number(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n /= 10
    return r

print(reverse_number(12004))