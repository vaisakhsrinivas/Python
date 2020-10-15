def ReturnPairs (a):
    n = len(a)
    d = dict()
    s = 0
    result = []
    for i in range (0,n):
        for j in range(i+1,n):

            s = a[i] +  a[j]

            if  s not in d:

                d[s] = [a[i], a[j]]

            else:

                prev = d.get(s)
                result.append(prev)
                result.append([a[i],a[j]])
                return result

    return result





my_list = [3, 4, 7, 1, 12, 9]

print(ReturnPairs(my_list))