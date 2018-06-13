class obj_representation(object):

    def __init__(self):
        pass
    def add(self,a,b):
        print(a+b)
    def __str__(self):
        return "This is object representation"
obj = obj_representation()
print(obj)
obj.add(12,23)