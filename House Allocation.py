for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if k and k-i>=0:
            k=k-i
            c=c+1
    print(c)
