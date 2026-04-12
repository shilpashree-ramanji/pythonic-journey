'''
Given an integer array, find a maximum product of a triplet in the array.

Examples: 

Input:  arr[ ] = [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6 and 20

Input:  arr[ ] =  [-10, -3, -5, -6, -20]



'''

# Python program to find a maximum product of a
# triplet in array of integers using nestd loops

# Function to find a maximum product of a triplet
# in array of integers of size n
def maxProduct(arr):
    n = len(arr)

    maxProduct = -10**9

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                maxProduct = max(maxProduct, arr[i] * arr[j] * arr[k])

    return maxProduct


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 20]
    print(maxProduct(arr))



# A Python3 program to find a maximum
# product of a triplet in an array of integers 
# using sorting

# Function to find a maximum product of a triplet
# in array of integers of size n
def maxProduct(arr):
    n = len(arr)
    
    # Sort the array in ascending order
    arr.sort()

    # Return the maximum of product of last three
    # elements and product of first two elements
    # and last element
    return max(arr[0] * arr[1] * arr[n - 1],
               arr[n - 1] * arr[n - 2] * arr[n - 3])

if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -20]
    max = maxProduct(arr)
    print(max)