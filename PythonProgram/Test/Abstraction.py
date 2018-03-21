"""Interface is basically a tempelate that tells ur class how to behave In python we will achive it through Abstraction
we can not creat the object of interface i.e if a class contain abstract method then we can not create the object of that
class"""

#Example
from abc import ABCMeta , abstractmethod
class shape(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
