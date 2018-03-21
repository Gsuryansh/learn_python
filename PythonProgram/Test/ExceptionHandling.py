import  sys
# random_list=['a',0,2.0]
# for value in random_list:
#     try:
#         r=1/value
#     except:
#         print(sys.exc_info()[0])#this will print the type of error
# print("Reciprocal is",r)
"""The above code will catch all the exception"""

"""Catching specific exception the below code will catch the specific exception"""

"""try:
   # do something
   pass

except ValueError: #value error means if you get other value the expected
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass"""

"""a=10
b="abc"
try:
    print(a+b)#This will throw TypeError because we are adding int and string
except:
    print(sys.exc_info()[0])#type error means if u do operation with two different type of values"""

"""Raising exception from ourself for rasing exception we will use raise"""

# try:
#     a = int(input("Enter a positive integer: "))
#     if a <= 0:
#        raise ValueError("That is not a positive number!")
# except ValueError as ve:
#     print(ve)


"""Finally block"""

"""try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()#finally block will always execute wheather try will raise an exception or not."""

"""Else with try and except"""
"""try:
        operation_that_can_throw_ioerror()
    except IOError:
        handle_the_exception_somehow()
    else:
         # we don't want to catch the IOError if it's raised
        another_operation_that_can_throw_ioerror()
    finally:
        something_we_always_need_to_do()"""

#Note else block run only when there is no exception raised in try block.


"""User define exception"""
"""class error(Exception):#This is the base class we have created for exception
    pass
class ValueIsToSmall(error):#This inherit the base class error and raise the exception if value is small
    pass
class ValueIsTooLarge(error):#This inherit the base class error and raise the exception if value is lagre
    pass

number=10
while True:
    try:
        i_number=int(input("Enter a number"))
        if i_number<number:
            raise ValueIsToSmall
        elif i_number>number:
            raise ValueIsTooLarge
        break

    except ValueIsTooLarge:
        print("Value is too large")
    except ValueIsToSmall:
        print("Value is too small")
print("Congratulation you guess correctly")"""


