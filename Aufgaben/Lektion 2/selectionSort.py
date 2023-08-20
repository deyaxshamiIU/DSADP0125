arr = [64, 34, 25, 12, 22, 11, 90, 11, 11 ,-2 ,-1000]

for indexOut in range(len(arr)):

    min = arr[indexOut]

    for indexIn in range(len(arr) - indexOut):

        if min > arr[indexIn + indexOut]:
            bigger = min
            min = arr[indexIn + indexOut]
            arr[indexIn + indexOut] = bigger

    arr[indexOut] = min


print(arr)