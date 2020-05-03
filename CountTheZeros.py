sizeoflist = int(input())
l = []
count = 0

for i in range (sizeoflist):
    l.append((input()))

for i in l:
    if (i == '0'):
        count = count + 1
    else:
        pass
print(count)

#alternative

n = int(input())
arr = [int(i) for i in input().split()]
print(len(arr) - sum(arr))



