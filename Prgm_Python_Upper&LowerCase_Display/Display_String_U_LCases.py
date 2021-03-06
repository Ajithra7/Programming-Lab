'''Program that takes input from the user & display in uppercase & lowercase'''

class StringCase:
   s=''
   def __init__(self,s):
       self.s= s
   def string_case(self):
       print("Upper Case:"+(self.s).upper())
       print("Lower Case:"+(self.s).lower())

s = input("Enter the string:")
str_case = StringCase(s)
str_case.string_case()