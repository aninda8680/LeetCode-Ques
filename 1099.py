def twoSumLessThank(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_sum = -1
    pairs = (0, 0)
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            max_sum = max(max_sum, current_sum)
            left += 1
        else:
            right -= 1
    return max_sum
    
    
    
nums = [34, 23, 1, 24, 75, 33, 54, 8]
k = 60
print(twoSumLessThank(nums, k))


# The pairs of the closest sum is:  (24, 34)
# The Closest Sum is:  58





def twoSumLessThanK(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1
    max_sum = -1
    pairs = (-1, -1)
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < k:
            if current_sum > max_sum:
                max_sum = current_sum
                pairs = (nums[left], nums[right])
            left += 1
        else:
            right -= 1
    print("The pair is: ", pairs)
    return max_sum
    
    
nums = [34,23,1,24,75,33,54,8]
k = 60
result = twoSumLessThanK(nums, k)
print("The closest sum is: ", result)


# The pair is:  (24, 34)
# The closest sum is:  58