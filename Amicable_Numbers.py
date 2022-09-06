x=int(input())
y=int(input())
s=0
p=0
for i in range(1,x):
    if x%i==0:
        s+=i
for j in range(1,y):
    if y%j==0:
        p+=j
if x==p and y==s:
    print("Amicable")
else:
    print("Not Amicable")
            