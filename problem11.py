def Longest_Substring_Without_Repeating_Characters(s:str):
    letters = dict()
    left = 0
    max_length = 0
    indexes = (len(s), len(s))
    for i in range(len(s)):
        if s[i] not in letters:
            letters[s[i]] = 1
        else:
            letters[s[i]] += 1
        
        while letters[s[i]] > 1:
            letters[s[left]] -= 1
            left += 1

        if i - left + 1 > max_length:
                max_length = i - left + 1
                indexes = (left, i)

    if indexes == (len(s), len(s)):
        return "Didnt find a sub string"
     
    return s[indexes[0]:indexes[1]+1]


s = "abcabcbb"
print("TEST 1:")
print(Longest_Substring_Without_Repeating_Characters(s), end="\n\n")

s = "abc"
print("TEST 2:")
print(Longest_Substring_Without_Repeating_Characters(s), end="\n\n")

s = "bbbbbbb"
print("TEST 3:")
print(Longest_Substring_Without_Repeating_Characters(s), end="\n\n")

s = "bcbcbcbcbcbacb"
print("TEST 4:")
print(Longest_Substring_Without_Repeating_Characters(s), end="\n\n")