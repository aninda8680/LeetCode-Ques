class Solution(object):
    def findIntegers(self, n):
        dp = [0] * 32
        dp[0], dp[1] = 1, 2

        for i in range(2, 32):
            dp[i] = dp[i-1] + dp[i-2]

        result = 0
        prev_bit = 0
        bit_index = 31 

        while bit_index >= 0:
            if n & (1 << bit_index):
                result += dp[bit_index]
                if prev_bit == 1:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0

            bit_index -= 1
        return result+1       