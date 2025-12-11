class Solution(object):
    def minSteps(self, n):
        steps = 0
        i = 2

        while i<= n:
            while n % i == 0:
                steps += i
                n //= i
            i += 1
        return steps
        