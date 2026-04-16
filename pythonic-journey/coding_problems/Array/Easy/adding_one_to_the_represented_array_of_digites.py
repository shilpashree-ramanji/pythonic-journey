'''
Given a non-negative number represented as an array of digits. The task is to add 1 to the number (increment the number represented by the digits by 1). The digits are stored such that the most significant digit is the first element of the array.

Examples :

Input : [1, 2, 4]
Output : 125
Explanation: 124 + 1 = 125 

Input : [9, 9, 9]
Output: 1000
Explanation: 999 + 1 = 1000 


'''

# Python program to add 1 to a
# number represented as an array

def addOne(arr):

  
    carry = 1

    for i in range(len(arr) - 1, -1, -1):
        sum = arr[i] + carry
        arr[i] = sum % 10
        carry = sum // 10

    if carry:
        arr.insert(0, carry)

    return arr

# Driver code
if __name__ == "__main__":
    arr = [9, 9, 9]
    res = addOne(arr)
    for i in res:
        print(i, end="")