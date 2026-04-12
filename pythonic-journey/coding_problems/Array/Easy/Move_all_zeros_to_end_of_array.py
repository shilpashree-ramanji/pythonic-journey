

def pushZeroToEnd(arr):
    n = len(arr)
    print(f"Length of an array is : {n}")

    temp = []

    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
        else:
            print("No NON-Zero Found")

    print(temp)

    count_zero = len(arr) - len(temp)
    print(count_zero)

    for i in range (0, count_zero):
        temp.append(0)

    return temp






arr = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZeroToEnd(arr))