def find_gcd(N,M):
    while M:
        if N>M:
            N,M=M,N
        M=M%N
    return N
N,M=map(int,input().split())
res=find_gcd(N,M)
print(res)