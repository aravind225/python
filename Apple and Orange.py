s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
lm=list(map(int,input().split()))
ln=list(map(int,input().split()))
la=[a+i for i in lm]
lz=[b+i for i in ln]
ca,co=0,0
for i in la:
    if i in range(s,t+1):
        ca=ca+1
for i in lz:
    if i in range(s,t+1):
        co=co+1
print(ca)
print(co)
