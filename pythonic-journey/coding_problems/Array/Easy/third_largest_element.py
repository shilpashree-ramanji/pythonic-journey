'''

THIRD LARGEST ELEMENT IN AN ARRAY OF DISTINCT ELEMENTS

Given an array of 'n' integers, the task is to find the "Third Largest Element". 
All the elements in an array are distinct integers
array can have negative values

Examples : 

Input: arr[] = {1, 14, 2, 16, 10, 20}
Output: 14
Explanation: Largest element is 20, second largest element is 16 and third largest element is 14

Input: arr[] = {19, -10, 20, 14, 2, 16, 10}
Output: 16
Explanation: Largest element is 20, second largest element is 19 and third largest element is 16 

'''

def third_largest_num(arr):
    n = len(arr)
    first, second, third = float('-inf'), float('-inf'), float('-inf')

    for i in range(n):
        if arr[i] > first:
            third=second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]
    return third

if __name__ == "__main__":
    arr = [19, -10, 20, 14, 2, 16, 10]
    print("Third largest number is:", third_largest_num(arr))

    arr = [1, 14, 2, 16, 10, 20]
    print("Third largest number is:", third_largest_num(arr))


    arr = [10, 10, 10]
    print("Third largest number is:", third_largest_num(arr))

    arr = [10, 10]
    print("Third largest number is:", third_largest_num(arr))