def sort012(arr, n):
    start = 0
    end = n-1
    mid = 0

    while mid <= end:
        if arr[mid] == 0:
            arr[start], arr[mid] = arr[mid], arr[start]
            start = start  + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end = end - 1
    return arr



arr= [0,2,1,2,0]
N = len(arr)
print(sort012(arr, N))