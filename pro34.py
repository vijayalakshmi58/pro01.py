vg,ts = map(int,input().split())
costs=0
lat = []
for i in range(vg):
      lat.append(input())
for i in range(vg):
      for j in range(ts-1):
            if lat[i][j] != 'R' and lat[i][j+1] != 'R' :
                  costs+=3
            elif lat[i][j] != 'G' and lat[i][j+1] != 'G':
                  costs+=5
print(costs)
