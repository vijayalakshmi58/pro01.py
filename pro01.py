# pro01.py
viji = int(input())
sg=[]
for i in range(0,viji):
 lan1=input()
 sg.append(lan1)
tsp=[]
for i in zip(*sg):
 if(i.count(i[0])==len(i)):
  tsp.append(i[0])
 
 else:
  break
print(''.join(tsp))
