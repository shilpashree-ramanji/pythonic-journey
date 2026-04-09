'''
ARRAY REVERSE

Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

Examples:

Input: arr[] = [1, 4, 3, 2, 6, 5]  
Output:  [5, 6, 2, 3, 4, 1]
Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

Input: arr[] = [4, 5, 1, 2]
Output: [2, 1, 5, 4]
Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

'''

def reverse_array(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Reversed array is:", reverse_array(arr))

    arr = [10, 20, 30, 40]
    print("Reversed array is:", reverse_array(arr))

    arr = [10]
    print("Reversed array is:", reverse_array(arr))


