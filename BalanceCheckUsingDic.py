def check (s):
    stack = []
    table = {
    ")": "(",
    "}": "{",
    "]": "[",
    }
    for char in s:
        if not stack:
            stack.append(char)
        elif char not in table:
            stack.append(char)
        elif table[char] == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        print("NO")
    else:
        print("YES")


s = "[]"
check(s)