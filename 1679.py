class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            target = nums[left] + nums[right]
            
            if target == k:
                count += 1
                left += 1
                right -= 1
            elif target < k:
                left += 1
            else:
                right -= 1
        return count
            