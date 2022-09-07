n=int(input())
s=0
dc=0
alt=n
while n>0:
    n//=10
    dc+=1
n=alt
p=dc
while n>0:
    d=n%10
    n=n//10
    s=s+d**p
    p-=1
if s==alt:
    print("True")
else:
    print("False")