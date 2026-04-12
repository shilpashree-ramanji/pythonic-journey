def max_consective(arr):
    max_cnt = 1
    curr_cnt = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            curr_cnt += 1
        else:
            max_cnt = max(max_cnt, curr_cnt)
            curr_cnt = 1
    return max(max_cnt, curr_cnt)

arr= [0, 1, 0, 1, 1, 1, 1]
print(max_consective(arr))

arr= [0, 0, 1, 0, 1, 0]
print(max_consective(arr))

arr= [0, 0, 0, 0]
print(max_consective(arr))