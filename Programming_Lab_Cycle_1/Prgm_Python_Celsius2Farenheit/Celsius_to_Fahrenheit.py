'''Program for Temperature conversion to Fahrenheit'''

class temperature:
    celsius = 0
    def __init__(self,celsius):
        self.celsius = celsius
        
    def find_fahrenheit(self):
        print("Temperature in Fahrenheit is:",(self.celsius*1.8)+32)

temp = float(input("Enter Celsius Value:"))
temp = temperature(temp)
temp.find_fahrenheit()