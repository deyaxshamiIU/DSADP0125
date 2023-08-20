arr = [64, 34, 25, 12, 22, 11, 90, 11, 11 ,-2 ,-1000]

for indexOut in range(len(arr)):

    for indexIn in range(0, len(arr) - indexOut -1):
        if arr[indexIn] > arr[indexIn+1]:
            y = arr[indexIn]
            arr[indexIn] = arr[indexIn+1]
            arr[indexIn+1] = y


print(arr)