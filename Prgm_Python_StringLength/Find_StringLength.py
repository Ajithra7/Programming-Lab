'''Program to find the legth of the string'''

class StringLength:
   s=''
   def __init__(self,s):
       self.s= s
   def showstringlength(self):
       print(len(self.s))

s = input("Enter the string:")
length_str = StringLength(s)
length_str.showstringlength()
