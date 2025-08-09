def first_nonRepeating_character(s:str):
    letters = dict()
    for i in range(len(s)):
        if s[i] not in letters:
            letters[s[i]] = 1
        else:
            letters[s[i]] += 1

    for key, value in letters.items():
        if value == 1:
            return key
        
    return "all the characters are repeated"
        

s = "abcbcdbfbjfdshf"
print("TEST 1:")
print(first_nonRepeating_character(s), end="\n\n")

s = "afgbcafg"
print("TEST 2:")
print(first_nonRepeating_character(s), end="\n\n")

s = "abcabcabcfghg"
print("TEST 1:")
print(first_nonRepeating_character(s), end="\n\n")

s = "abcbca"
print("TEST 1:")
print(first_nonRepeating_character(s), end="\n\n")