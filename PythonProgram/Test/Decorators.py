"""def parent():
    print("Printing from the parent() function")

    def First_child():
        print("Printing from the Frist_child() function")

    def Second_child():
        print("printing from the Secon_chid() function")

    First_child()
    Second_child()



parent()
#First_child() # This line will show error 'First_child' is not defined because the scope of the function is inside the parent function
#Second_child() #Same error"""




"""Returning a Function"""


"""def parent(num):

    def first_child():
        print("Printing form the first child")
    def second_child():
        print("Printing from the second child")


    if num==10:
        return first_child
    else:
        return second_child
fun=parent(100)
print(fun)
fun()"""

#DECORATORS

# def My_decorators(somefunction): # This is the decorator function
#
#     def wrapper():
#         print("Inside wrapper")
#
#         somefunction()
#         print("After some function call")
#
#     return wrapper
# def my_function():
#     print ("Inside my function")
#
# decotrator=My_decorators(my_function)
# decotrator()



#Another Example of decorators

# def My_decorators(somefunction): # This is the decorator function
#
#     def wrapper():
#         print("Inside wrapper")
#         val=10
#         if val ==10:
#             print("Yes")
#         else:
#             print("No")
#         somefunction()
#         print("After some function call")
#
#     return wrapper
#
# def my_function():
#     print ("Inside my function")
# decotrator=My_decorators(my_function)
# decotrator()

#Proper Example of decorator

"""def My_decorators(somefunction): # This is the decorator function

    def wrapper():
        print("Inside wrapper")
        val=10
        if val ==10:
            print("Yes")
        else:
            print("No")
        somefunction(6)
        print("After some function call")

    return wrapper
@My_decorators
def my_function():
    print ("Inside my function")
my_function()"""

#Real world Example of decorators

"""import time

def timing (function):
    def wrapper():
        t1=time.time()
        print(time.time())
        function()
        print(time.time())
        t2=time.time()
        print(t2-t1)
    return wrapper
@timing
def some_function():
    li=[]
    for num in range(12343456):
        li.append(num)
    print(sum(li))
some_function()"""

# Above decorators example will calculate the time taken by some_function()
