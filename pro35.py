vg=input()
l1=list(set(vg))
xen1=1
antt=0
check=False
while True:
    ch=l1[antt]
    for y in range(0,len(vg)-xen1):
        if ch in vg[y:y+xen1]:
            check=True
        else:
            check=False
            antt=antt+1
            if antt>=len(l1):
             antt=0
             xen1=xen1+1
            break

    if check==True:
        break
print(xen1)
