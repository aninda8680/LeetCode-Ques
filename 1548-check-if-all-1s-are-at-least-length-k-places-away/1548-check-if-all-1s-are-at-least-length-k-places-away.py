class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        last_pos = -1  # to track previous 1's position

        for i in range(len(nums)):
            if nums[i] == 1:
                if last_pos != -1 and (i - last_pos - 1) < k:
                    return False
                last_pos = i
        
        return True
