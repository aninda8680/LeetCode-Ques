class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)

        total = 0
        for i in range(k):
            total += nums[i]

        maxSum = total

        for i in range(k, n):
            total += nums[i]
            total -= nums[i-k]
            maxSum = max(maxSum, total)

        return float (maxSum) / k 