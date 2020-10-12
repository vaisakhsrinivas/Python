def unique(s):

    l = len(s)

    i = 1

    while i < l:

        if s[i] == s[i-1]:

            return False
        i = i + 1
    return True


print(unique("asdfghjklwertyuiopqzxcvbnmm"))