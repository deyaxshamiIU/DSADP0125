import math
import random

arr = []

for x in range(100):
    arr.append([])
    for y in range(100):
        arr[x].append()
        
        
for x in range(100):
    for y in range(100):
        if x == y:
            arr[x][y]=0
        else:
            z = random.gauss(50, math.sqrt(50))
            arr[x][y]= z
            arr[y][x]= z

pathLength=0

for x in range(50):
    shortPath=1000
    for y in range(100):
        if arr[x][y]!=0:
            if shortPath > arr[x][y]:
                shortPath= arr[x][y]
    pathLength+=shortPath

print(pathLength)