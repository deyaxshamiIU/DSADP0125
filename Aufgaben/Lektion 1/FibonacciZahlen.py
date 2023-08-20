NumberFibonacci = 10
arr=[1,1]

for index in range(NumberFibonacci-2):
    arr.append(arr[index] + arr[index+1])

print(arr)