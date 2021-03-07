'''Biggest of Three Numbers'''
class BiggestNumber:
        a=b=c=0
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
            
        def findbiggest(self):
            
            a= self.a
            b= self.b
            c= self.c
            
            if a>b and a>c:
                print(a)
            elif b>a and b>c:
                print(b)
            else:
                print(c)
a,b,c = float(input("Enter First Number:")),float(input("Enter Second Number:")),float(input("Enter Third Number:"))
abc = BiggestNumber(a,b,c)
abc.findbiggest()