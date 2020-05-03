def SumLength(arr, n, k):
    sum = 0

    for i in range(n):

        count = 0
        maxsubelementfound = 0

        while i < n and arr[i] <= k:
            count = count + 1
            if arr[i] == k:
                maxsubelementfound = 1
            i = i + 1

        if maxsubelementfound == 1:
            sum = sum + count

        while i < n and arr[i] > k:
            i = i + 1

    return sum


arr = [4, 5, 7, 1, 2, 9, 8, 4, 3, 1]
maxsubelement = 4
size = len(arr)

ans = SumLength(arr,size,maxsubelement)
print(ans)

