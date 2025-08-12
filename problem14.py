def Two_Sum(nums:list, target:int):
    nums_hash = dict()
    for i in range(len(nums)):
        if target - nums[i] in nums_hash:
            return (nums_hash[target - nums[i]], i)
        else:
            nums_hash[nums[i]] = i

    return (-1, -1)


nums = [2, 7, 11, 15] 
target = 9 
print("TEST 1:")
print(Two_Sum(nums, target), end="\n\n")

nums = [2, 7, 11, 15] 
target = 22 
print("TEST 2:")
print(Two_Sum(nums, target), end="\n\n")

nums = [2, 7, 11, 15] 
target = 30
print("TEST 3:")
print(Two_Sum(nums, target), end="\n\n")
