'''Program to Merge two dictionaries'''

n = int(input("Enter the length of 1st dictionary: "))
dct_input1 = {}
for i in range(0,n):
    key = input("Key: ")
    value = input("Value: ")
    dct_input1.update({key:value})

n = int(input("Enter the length of 2nd dictionary: "))
dct_input2 = {}
for i in range(0,n):
    key = input("Key: ")
    value = input("Value: ")
    dct_input2.update({key:value})

print("First dictionary :",dct_input1)
print("Second dictionary :",dct_input2)
dct_input1.update(dct_input2)
print("Output dictionary :",dct_input1)