class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None. Do not return anything, modify nums in-place instead.
        """

        last_non_zero = 0  # Pointer to place the next non-zero element

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1

        # Fill the rest with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0
