def Longest_Substring_with_At_Most_K_Distinct_Characters(s:str, k:int):
    chars = dict()
    left = 0
    chars_counter = 0
    max_length = 0
    indexes = (len(s), len(s))
    for i in range(len(s)):
        if s[i] not in chars or chars[s[i]] == 0:
            chars[s[i]] = 1
            chars_counter += 1
        else:
            chars[s[i]] += 1

        while chars_counter > k:
            chars[s[left]] -= 1
            if chars[s[left]] == 0:
                chars_counter -= 1
            left += 1

        if i - left + 1 > max_length:
            max_length = i - left + 1
            indexes = (left, i)

    if indexes == (len(s), len(s)):
        return "Didnt find a sub string"
     
    return s[indexes[0]:indexes[1]+1]


s = "eceba"
k = 2  
print("TEST 1:")
print(Longest_Substring_with_At_Most_K_Distinct_Characters(s, k), end="\n\n")

s = "eceba"
k = 3 
print("TEST 2:")
print(Longest_Substring_with_At_Most_K_Distinct_Characters(s, k), end="\n\n")

s = "aaabbcccccbbb"
k = 2  
print("TEST 3:")
print(Longest_Substring_with_At_Most_K_Distinct_Characters(s, k), end="\n\n")

s = "aaabbcccccbbb"
k = 4  
print("TEST 4:")
print(Longest_Substring_with_At_Most_K_Distinct_Characters(s, k), end="\n\n")