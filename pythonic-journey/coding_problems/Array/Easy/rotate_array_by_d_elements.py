'''
Rotate an Array by d - Counterclockwise or Left 

Given an array of integers arr[] of size n, the task is to rotate the array elements to the left by d positions.

Examples:

Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2

Output: {3, 4, 5, 6, 1, 2} 

Explanation: After first left rotation, arr[] becomes {2, 3, 4, 5, 6, 1} and,

after the second rotation, arr[] becomes {3, 4, 5, 6, 1, 2}

Input: arr[] = {1, 2, 3}, d = 4

Output: {2, 3, 1}

Explanation: The array is rotated as follows:

After first left rotation, arr[] = {2, 3, 1}

After second left rotation, arr[] = {3, 1, 2}

After third left rotation, arr[] = {1, 2, 3}

After fourth left rotation, arr[] = {2, 3, 1}

'''

def RotateArray(arr, d):
    n = len(arr)

    for i in range(d):
        first = arr[0]
        print(f"First Element is : {first}")

        for j in range(n-1):
            arr[j] = arr[j+1]
            print(f"Array {j} element is : {arr[j]}")
        arr[n-1] = first
        print(f"Print Last elements which is appending in the last place : {arr[n-1]}")
    
        print(f"Printing array fo {i} th ietration of {d} iteration.")
        print(arr)
    return arr


if __name__ == "__main__":

    arr = [1,2,3,4,5,6]
    d = 2

    RotateArray(arr, d)

