'''Program to find the area of the rectangle and triangle'''

class Triangle:
   a=b=c=s=0
   def __init__(self,a,b,c):
       self.a= a
       self.b= b
       self.c= c
       self.s=(a+b+c)/2
   def find_triangle_area(self):
       area=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
       print("Area of Triangle is:",area)
       
class Rectangle:
     b=l=0
     def __init__(self,b,l):
         self.l = l
         self.b = b
     def find_rectangle_area(self):
        area = self.b*self.l
        print("Area of The Rectangle is:",area)

rectangle = Rectangle(float(input("Enter depth and Length of Rectangle:")),float(input()))
rectangle.find_rectangle_area()
triangle = Triangle(float(input("Enter value 3 sides of Triangle:")),float(input()),float(input()))
triangle.find_triangle_area()
