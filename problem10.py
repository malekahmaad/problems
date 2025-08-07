def min_window(s:str, t:str):
    letters_count = dict()
    size = len(t)
    for i in range(len(t)):
        if t[i] in letters_count:
            letters_count[t[i]] += 1
        else:
            letters_count[t[i]] = 1

    # print(letters_count)
    right = 0
    left = 0
    required_letters_visited = 0
    letters_visited = dict()
    min_size = len(s)
    indexes = (len(s), len(s))
    while right < len(s):
        if s[right] in letters_visited:
            letters_visited[s[right]] += 1
        else:
            letters_visited[s[right]] = 1

        if s[right] in letters_count and letters_visited[s[right]] <= letters_count[s[right]]:
            required_letters_visited += 1

        while required_letters_visited == size:
            letters_visited[s[left]] -= 1
            if s[left] in letters_count:
                if letters_visited[s[left]] < letters_count[s[left]]:
                    required_letters_visited -= 1

            if right - left < min_size:
                min_size = right - left
                indexes = (left, right)

            left += 1

        right += 1
    
    if indexes == (len(s), len(s)):
        return "Didnt find a window"
     
    return s[indexes[0]:indexes[1]+1]


s = "abbcsdfganocbc"
t = "abbc"
print("TEST 1:")
print(min_window(s, t), end="\n\n")

s = "abcsdfganocbc"
t = "abbc"
print("TEST 2:")
print(min_window(s, t), end="\n\n")

s = "abbcsdfganocbc"
t = "abbcc"
print("TEST 3:")
print(min_window(s, t), end="\n\n")

s = "abbcsdfabgc"
t = "abcdf"
print("TEST 4:")
print(min_window(s, t), end="\n\n")

s = "abbcsdfganocbc"
t = "aaa"
print("TEST 5:")
print(min_window(s, t), end="\n\n")