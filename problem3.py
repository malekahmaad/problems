def k_most_frequent_elements(nums:list, k:int):
    count_table = dict()
    for i in range(len(nums)):
        if nums[i] in count_table:
            count_table[nums[i]] += 1
        else:
            count_table[nums[i]] = 1

    # print(count_table)
    max_count = 0
    for _, count in count_table.items():
        if count > max_count:
            max_count = count

    # print(max_count)
    frequency_table = [[] for _ in range(max_count)]
    # print(frequency_table)
    for num, count in count_table.items():
        frequency_table[count-1].append(num)

    # print(frequency_table)
    result = list()
    for numbers in reversed(frequency_table):
        for number in numbers:
            result.append(number)
            k -= 1
            if k == 0:
                return result

nums = [4,4,4,5,5,6]
k = 2
print("test 1:")
print(k_most_frequent_elements(nums, k), end="\n\n")

nums = [4,5,4,5,6,4,6,6]
k = 2
print("test 2:")
print(k_most_frequent_elements(nums, k), end="\n\n")

nums = [4,5,4,5,4,5,6,7,6,7]
k = 3
print("test 3:")
print(k_most_frequent_elements(nums, k), end="\n\n")

nums = [4,5,4,5,6,8,6,7,4,7,8]
k = 3
print("test 4:")
print(k_most_frequent_elements(nums, k), end="\n\n")