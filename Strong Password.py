def isup(s):
    for i in s:
        if i.isupper():
            return True
    return False
def islp(s):
    for i in s:
        if i.islower():
            return True
    return False
def issym(s):
    sc="!@#$%^&*()-+"
    for i in s:
        if i in sc:
            return True
    return False
def isnum(s):
    for i in s:
        if i.isdigit():
            return True
    return False
s=input()
c=0
if isup(s):
    c=c+1
if islp(s):
    c+=1
if issym(s):
    c+=1
if isnum(s):
    c+=1
print(max(4-c,6-len(s)))
