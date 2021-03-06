'''
To accept number and compute the value of n+n*n+n*n*n
'''

class NumberSum:
   n=0
   def __init__(self,n):
       self.n= n
   def calculation(self):
       n= self.n
       print(n+n*n+n*n*n)
n = float(input("Enter Number:"))
sum = NumberSum(n)
sum.calculation()