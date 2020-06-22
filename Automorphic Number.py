a=int(input())
b=str(a**2)
c=len(str(a))
if a>=4:
    if b[-c:]==str(a):
        print("YES")
    else:
        print("NO")
        
else:
    print("Invalid Input")
