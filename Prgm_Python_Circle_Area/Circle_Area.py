'''Area of the Circle'''

class Circle:
        r=0
        def __init__(self,radius):
            self.r=radius
        def area(self):
            return 3.14*self.r*self.r
            
radius = float(input("Enter Radius:"))
asd = Circle(radius)
area = asd.area()
print(area)