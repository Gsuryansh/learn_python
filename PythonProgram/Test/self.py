class TestSelf(object):
    def __init__(self):
        print("Inside the init function")

    def abc(self):
        print("Inside the abc function")


obj=TestSelf()
#obj.abc()
TestSelf.abc(obj) # this statement and the above statment are the same that means self recive the object itself.