class Solution(object):
    def singleNumber(self, nums):
        qwert = 0
        for n in nums:
            qwert ^= n
        return qwert