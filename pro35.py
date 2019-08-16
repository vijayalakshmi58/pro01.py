cad=input()
l21=list(set(cad))
xens=1
antt=0
check=False
while True:
    ch=l21[antt]
    for y in range(0,len(cad)-xens):
        if ch in cad[y:y+xens]:
            check=True
        else:
            check=False
            antt=antt+1
            if antt>=len(l1):
             antt=0
             xens=xens+1
            break

    if check==True:
        break
print(xens)
