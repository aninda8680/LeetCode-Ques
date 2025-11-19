class Solution:
    def findFinalValue(self, nums, original):
        seen = set(nums)
        while original in seen:
            original *= 2
        return original

