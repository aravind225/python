def pali(s):
    if s==s[::-1]:
        return True
    return False
for _ in range(int(input())):
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if pali(str(i)):
            c=c+1
    print(c)
