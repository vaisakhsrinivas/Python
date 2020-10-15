def permutation (s1, s2):


    l1 = len(s1)

    l2 = len(s2)


    if l1 != l2:

        return False

    for i in s1:

        if i in s2:
            s2 = s2.replace(i, "")

            if len(s2) == 0:
                return True


    return False




str1 = "test"
str2 = "ttes"

print(permutation(str1, str2))




