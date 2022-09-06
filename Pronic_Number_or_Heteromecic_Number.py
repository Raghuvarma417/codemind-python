n=int(input())
for i in range(n+1):
    if i*(i+1)==n:
        print("YES")
        break
else:
    print("NO")