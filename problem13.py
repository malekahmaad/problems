def closest_sum_to_zero(nums:list):
    nums.sort()
    left = 0
    right = len(nums) - 1
    closest_to_zero = float("inf")
    indexes = (len(nums), len(nums))
    while left < right:
        if abs(nums[right] + nums[left]) < closest_to_zero:
            closest_to_zero = abs(nums[right] + nums[left])
            indexes = (left, right)

        if nums[right] + nums[left] < 0:
            left += 1
        elif nums[right] + nums[left] > 0:
            right -= 1
        else:
            return nums[left], nums[right]
        
    return nums[indexes[0]], nums[indexes[1]]


nums = [-8, 10, 6, -6]
print("TEST 1:")
print(closest_sum_to_zero(nums), end="\n\n")

nums = [-8, 10, 6, -5]
print("TEST 2:")
print(closest_sum_to_zero(nums), end="\n\n")

nums = [-8, 10, 6, 7]
print("TEST 3:")
print(closest_sum_to_zero(nums), end="\n\n")

nums = [-8, 10, 6, 2, 4]
print("TEST 4:")
print(closest_sum_to_zero(nums), end="\n\n")