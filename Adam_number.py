n=int(input())
r=0
i=0
z=0
s=n**2
while n>0:
    d=n%10
    n=n//10
    r=r*10+d
a=r**2 
while a>0:
    q=a%10
    a=a//10
    z=z*10+q
if s==z:
    print("True")
else:
    print("False")