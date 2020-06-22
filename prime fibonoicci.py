def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n,m=map(int,input().split())
l=[i for i in range(n,m+1) if isprime(i) and i!=1]
z=[]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]!=l[j] and int(str(l[i])+str(l[j]))not in z:
            z.append(int(str(l[i])+str(l[j])))
l=[i for i in z if isprime(i) and i!=1]
b=[min(l),max(l)]
for i in range(len(l)-2):
    b.append(b[-1]+b[-2])
print(b[-1])
