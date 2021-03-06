'''Program for Temperature conversion to Farenheit'''

class temperature:
    celsius = 0
    def __init__(self,celsius):
        self.celsius = celsius
        
    def find_farenheit(self):
        print("Temperature in Farenheit is:",(self.celsius*1.8)+32)

temp = float(input("Enter Celsius Value:"))
temp = temperature(temp)
temp.find_farenheit()