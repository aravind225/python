s=input()
z=[]
for i in s:
    if len(z)>0 and z[-1]==i:
        z.pop()
    else:
        z.append(i)
if z:
    print("".join(z))
else:
    print("Empty String")
