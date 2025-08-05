def Longest_Palindromic_Substring(word:str):
    max_length = 0
    max_substring = ""
    for i in range(len(word)):
        odd_substring, odd_substring_length = find_palindrome(i, i, word)
        even_substring, even_substring_length = find_palindrome(i, i+1, word)
        if odd_substring_length > even_substring_length:
            sub_string_length = odd_substring_length
            sub_string = odd_substring
        else:
            sub_string_length = even_substring_length
            sub_string = even_substring
        
        if sub_string_length > max_length:
            max_length = sub_string_length
            max_substring = sub_string

    return max_substring

def find_palindrome(start:int, end:int, word:str):
    sub_string = ""
    sub_string_length = 0
    while start >= 0 and end < len(word) and word[start] == word[end]:
        temp_string = ""
        if start == end:
            sub_string_length += 1
            sub_string += word[start]
        else:
            sub_string_length += 2
            temp_string = word[start] + sub_string + word[end]
            sub_string = temp_string
        
        start -= 1
        end += 1

    return sub_string, sub_string_length


s = "babad"
print("TEST 1:")
print(Longest_Palindromic_Substring(s), end="\n\n")


s = "babab"
print("TEST 2:")
print(Longest_Palindromic_Substring(s), end="\n\n")


s = "afbcd"
print("TEST 3:")
print(Longest_Palindromic_Substring(s), end="\n\n")


s = "abcddcbasd"
print("TEST 4:")
print(Longest_Palindromic_Substring(s), end="\n\n")


s = "bbaacc"
print("TEST 5:")
print(Longest_Palindromic_Substring(s), end="\n\n")