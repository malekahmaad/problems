def longest_sequence(nums: list):
    visited = dict()
    current_num_plus = 0
    current_num_minus = 0
    current_size = 0
    max_size = 0
    for i in range(len(nums)):
        visited[nums[i]] = False

    # print(visited)
    for num in nums:
        if visited[num] is False:
            current_size += 1
            visited[num] = True
            current_num_plus = num + 1
            current_num_minus = num - 1
            while current_num_plus in visited:
                current_size += 1
                visited[current_num_plus] = True
                current_num_plus += 1
            
            while current_num_minus in visited:
                current_size += 1
                visited[current_num_minus] = True
                current_num_minus -= 1

            if current_size > max_size:
                max_size = current_size

            current_size = 0

    return max_size
             
            
nums = [100, 4, 200, 1, 3, 2]
print("TEST 1:")
print(longest_sequence(nums), end="\n\n")

nums = [100, 4, 200]
print("TEST 2:")
print(longest_sequence(nums), end="\n\n")

nums = [100, 200, 1, 3, 7, 9, 8, 6, 5]
print("TEST 3:")
print(longest_sequence(nums), end="\n\n")

nums = [100, 200, 101, 104, 102, 105]
print("TEST 3:")
print(longest_sequence(nums), end="\n\n")
