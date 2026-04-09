'''
SECOND LARGEST ELEMENT IN AN ARRAY

Given an array of positive integers arr[] of size n, The task is to find second largest distinct element in an array.

Note: If the second largest element does not exist, return -1

1. Input: arr[] = [12, 35, 1, 10, 34, 1]
    output: 34

2. Input: arr[] = [10,1,10]
    output : 1

3. Input: arr[] = [10,10,10]
    output : -1

'''

def sec_largest_num(arr):
    n = len(arr)
    largest = -1
    second_large = -1

    # let us find out first largets number
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    # Let us find out the second largest number
    for i in range(n):
        if arr[i] > second_large and arr[i] != largest:
            second_large = arr[i]
    return second_large

if __name__ == "__main__":
    arr = [12,35,1,10,34,1]
    print("Second largest number is:", sec_largest_num(arr))

    arr = [10,5,10]
    print("Second largest number is:", sec_largest_num(arr))

    arr = [10,10,10]
    print("Second largest number is:", sec_largest_num(arr))

    arr = [10,10]
    print("Second largest number is:", sec_largest_num(arr))


    arr = [10]
    print("Second largest number is:", sec_largest_num(arr))   

