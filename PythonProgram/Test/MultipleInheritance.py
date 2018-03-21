class shroom(object):
    def __init__(self):
        print("Inside shroom")
    def move(self):
        print("Big mario is moving")
class mario(object):
    def __init__(self):
        super(mario,self).__init__()#this will call custructor of shroom class
        print("Inside mario")
    def move(self):
        super(mario, self).move()# this will call move method of shroom class
        print("I am moving")

class BigMarion(mario,shroom):
   pass

Bm=BigMarion()
Bm.move()