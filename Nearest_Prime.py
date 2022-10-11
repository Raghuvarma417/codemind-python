for _ in range(int(input())):
    n=int(input())
    next_p=n
    while True:
        fc=0
        for i in range(1,next_p+1):
            if next_p%i==0:
                fc+=1
        if fc==2:
            break
        next_p+=1
    pp=n
    while True:
        fc=0
        for i in range(1,pp+1):
            if pp%i==0:
                fc+=1
        if fc==2:
            break
        pp-=1
    if n-pp<=next_p-n:
        print(pp)
    else:
        print(next_p)
           