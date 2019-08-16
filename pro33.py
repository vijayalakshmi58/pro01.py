vg=input()
flagg=0
for i in range(0,len(vg)-1):
  for j in range(i+1,len(vg)):
    if vg[i]<vg[j]:
      flagg=1
      print(vg[j:])
      break
  if flagg==1:
    break
else:
  print(vg)
