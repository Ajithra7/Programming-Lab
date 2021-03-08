file1 = open("file.txt","r") 
file_string = file1.read().split('\n')
file_odd = open("odd.txt","a+") 
file_even = open("even.txt","a+") 
for i in asd: 
    if i: 
        if int(i)%2==0: 
            file_even.write(i) 
            file_even.write('\n') 
        else: 
            file_odd.write(i) 
            file_odd.write('\n')
file_odd.close() 
file_even.close() 
