import random

arr = [50]

for x in range(50):
    num = random.randrange(0, 1000)
    arr.append(num)

print(arr)
print("\n")

links = arr.copy()
rechts = arr.copy()

for x in range(25):
    links.remove(links[x])
    links.append(0)

print(links)
print("\n")

for x in range(1, 26):
    rechts[x-1] = 0

print(rechts)
print("\n")
