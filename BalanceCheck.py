LH = ["(", "{", "["]
RH = [")", "}", "]"]

def check (s):

    stack = []

    for i in s:
        if not stack:
            stack.append(i)
        elif i in LH:
            stack.append(i)
        elif i in RH:
            p = RH.index(i)

            if (len(stack) > 0 and (LH[p] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"

    if (len(stack) == 0):
        return "Balanced"




s = "[]"
print(check(s))