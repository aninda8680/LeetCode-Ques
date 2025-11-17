class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Traverse from the last digit
        for i in range(len(digits) - 1, -1, -1):
            # If digit < 9, just add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If digit is 9 → it becomes 0 and carry continues
            digits[i] = 0

        # If all digits were 9, example: 999 → 1000
        return [1] + digits
