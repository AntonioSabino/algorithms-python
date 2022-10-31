def find_duplicate(nums):
    for num in nums:
        if type(num) is not int or num < 0:
            return False

    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return False
