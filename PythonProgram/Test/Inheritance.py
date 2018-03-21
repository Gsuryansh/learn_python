class polygon(object):
    def __init__(self,no_of_sides):
        self.n = no_of_sides         # n is the number of side and sides are the value of the side initially it
                                      #it is the list and values is 0
        self.sides = [0 for i in range(self.n)]

    def inputSides(self):
        self.sides =[float(input("Enter the sides")) for i in range(self.n)] # here user enter the value of sides


    def displaySides(self):  # it will display the value of each sides

        for i in range(self.n):
            print(self.sides[i])


class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)

    def area(self):
        a,b,c = self.sides

        s = (a+b+c)/2
        ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print( ar)

ob = triangle()
ob.inputSides()
ob.displaySides()
ob.area()



