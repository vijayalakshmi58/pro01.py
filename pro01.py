# pro01.py
viji = int(input())
s=[]
for i in range(0,viji):
 lan=input()
 s.append(lan)
vg=[]
for i in zip(*s):
 if(i.count(i[0])==len(i)):
  vg.append(i[0])
 
 else:
  break
print(''.join(vg))
