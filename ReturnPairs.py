def ReturnPairs (a,s):
    n = len(a)
    count = 0
    for i in range (0,n):
        for j in range(i+1,n):
            if a[i] + a[j] == s:
                print("The numbers are", a[i], a[j])



arr = [1, 5, 7, -1, 5]
sum = 6
ReturnPairs(arr,sum)
