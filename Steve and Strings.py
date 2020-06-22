s=input()
l=[]
for i in s:
    if l and l[-1]==i:
        l.pop()
    else:
        l.append(i)
        
if(len(l)==0):
    print("Empty String")
else:
    print("".join(l))



        
