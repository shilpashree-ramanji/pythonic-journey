
arr = [30, 23, 16, 79, 20, 15, 5]

arr.sort()

for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)