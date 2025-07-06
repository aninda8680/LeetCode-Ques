def missingNumber( nums):
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
        
nums = [1, 6, 3]
print(missingNumber(nums))