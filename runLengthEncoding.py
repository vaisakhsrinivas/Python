def runLengthEncoding(s):

    l = len(s)

    i = 0
    j = 0

    result = ""

    while i <= l-1:

        count = 1
        j = i

        while j < l-1:

            if s[j] == s[j+1]:

                count = count + 1
                j = j + 1

            else:

                break

        result = result + str(count) + s[i]

        i = j+1

    return result



print(runLengthEncoding("aaabbcc"))

