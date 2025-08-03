def Subarray_Sum_Equals_K(nums:list, k:int):
    sums = {0:1}
    previous_sum = 0
    count = 0
    for num in nums:
        previous_sum += num
        x = previous_sum - k
        if x in sums:
            count += 1

        sums[previous_sum] = 1

    return count


nums = [1, 2, 3]
k = 3
print("TEST 1:")
print(Subarray_Sum_Equals_K(nums, k), end="\n\n")

nums = [2, 3]
k = 1
print("TEST 2:")
print(Subarray_Sum_Equals_K(nums, k), end="\n\n")

nums = [2, 3, 3, 4, 4, 1, 3]
k = 8
print("TEST 3:")
print(Subarray_Sum_Equals_K(nums, k), end="\n\n")

nums = [1, 1, 2, 3, -1]
k = 2
print("TEST 4:")
print(Subarray_Sum_Equals_K(nums, k), end="\n\n")