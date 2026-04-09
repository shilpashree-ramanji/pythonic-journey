'''
REVERSE ARRAY IN GROUPS

Given an array arr[] and an integer k, find the array after reversing every subarray of consecutive k elements in place. If the last subarray has fewer than k elements, reverse it as it is. Modify the array in place, do not return anything.

Examples: 

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8], k = 3 
Output: [3, 2, 1, 6, 5, 4, 8, 7]

Explanation: Elements is reversed: [1, 2, 3] → [3, 2, 1], [4, 5, 6] → [6, 5, 4], and the last group [7, 8](size < 3) is reversed as [8, 7]. 

Input: arr[] = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]

Explanation: First group consists of elements 1, 2, 3. Second group consists of 4, 5.

Input: arr[] = [5, 6, 8, 9], k = 5
Output: [9, 8, 6, 5]

Explanation: Since k is greater than array size, the entire array is reversed.

Fixed-Size Group Reversal–Time O(n) and Space O(1)
Edge Cases:

When k = 1, the array stays the same
When k is greater than or equal to the array size
Approach

We begin from index 0 and find the size of the current subarray to be reversed. If the number of remaining elements at the end is less than k, reverse all of them.
Each subarray is reversed using two pointers that start from the two corners of the subarray.

'''

def reverseInGrou(arr, k):
    n = len(arr)
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)

        while(left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    print("Reversed array in groups is:", reverseInGrou(arr, k))

    arr = [10, 20, 30, 40, 50]
    k = 2
    print("Reversed array in groups is:", reverseInGrou(arr, k))

    arr = [10, 20, 30]
    k = 4
    print("Reversed array in groups is:", reverseInGrou(arr, k))