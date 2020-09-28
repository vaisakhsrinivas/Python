def balancedStrings(s):
    l = 0
    r = 0

    count = 0

    for i in s:
        if i == 'L':
            l = l + 1
        elif i == "R":
            r = r + 1
        if l == r:
            count = count + 1
            l = 0
            r = 0

    return count


print(balancedStrings("RLRRLLRLRL"))