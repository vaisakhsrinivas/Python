def removeVowels(s):

    v = ["a", "e", "i", "o", "u"]

    result = ""

    for i in s:
        if i not in v:
            result = result + i

    return result



print(removeVowels("asertyuikjhgc"))
