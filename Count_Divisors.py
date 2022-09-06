x,y,m=map(int,input().split())
c=0
s=0
for i in range(x,y+1):
    if i%m==0:
        s+=i
        c+=1
print(c)