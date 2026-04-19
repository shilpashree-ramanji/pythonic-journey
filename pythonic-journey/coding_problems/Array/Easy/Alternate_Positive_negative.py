'''
Given an array arr[] of size n, the task is to rearrange it in alternate positive and negative manner without changing the relative order of positive and negative numbers. In case of extra positive/negative numbers, they appear at the end of the array.

Note: The rearranged array should start with a positive number and 0 (zero) should be considered as a positive number.

Examples: 

Input:  arr[] = [1, 2, 3, -4, -1, 4]
Output: arr[] = [1, -4, 2, -1, 3, 4]

Input:  arr[] = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
Output: arr[] = [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]

The idea is to separate the numbers into positive and negative arrays. Then, alternately place numbers from each array back into the original array. Also place any remaining positive or negative numbers at the end.
'''

def rearrange_pos_neg(arr):
    pos = []
    neg = []

    for num in arr:
        if num >=0:
            pos.append(num)
        else:
            neg.append(num)

    posIndx = 0
    negIndx = 0
    i= 0

    while posIndx < len(pos) and negIndx <len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIndx]
            posIndx += 1
        else:
            arr[i] = neg[negIndx]
            negIndx += 1
        i += 1
    
    while posIndx < len(pos):
        arr[i] = pos[posIndx]
        posIndx +=1
        i += 1
    
    while negIndx < len(neg):
        arr[i] = neg[negIndx]
        i += 1

arr = [1,2,3,-4,-1,4]

rearrange_pos_neg(arr)

print(' '.join(map(str, arr)))