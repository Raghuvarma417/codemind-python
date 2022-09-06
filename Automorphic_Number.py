n=int(input())
s=n**2
if s%10==n or s%100==n or s%1000==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")