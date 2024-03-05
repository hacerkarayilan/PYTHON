def max_value(nums):
    max=nums[0]
    for i in range(0,len(nums)-1):
        if max<nums[i+1]:
            max=nums[i+1]
    return max
max_value([17, 7, -1, 26, 3, 9])