def CountPairs (a,s):
    n = len(a)
    count = 0
    for i in range (0,n):
        for j in range(i+1,n):
            if a[i] + a[j] == s:
                count = count + 1
    return count



arr = [1, 5, 7, -1, 5]
sum = 6
ans = CountPairs(arr,sum)
print (ans)