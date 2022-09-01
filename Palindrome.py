Num = int(input()) 
Temp = Num  
rev = 0  
while(Num > 0):  
    dig = Num % 10  
    rev = rev * 10 + dig  
    Num = Num // 10  
if(Temp == rev):  
    print("True")  
else:  
    print("False")  