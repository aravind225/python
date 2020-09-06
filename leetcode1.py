nums=list(map(int,input().split()))
target=int(input())
z=[]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)
            z.append(i)
            break
    if len(z)!=0:
        break
    
        
