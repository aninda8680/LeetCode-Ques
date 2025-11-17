class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        # Add digits from the end
        while i >= 0 or j >= 0 or carry:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = x + y + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1
            j -= 1

        # Digits added in reverse order
        return ''.join(result[::-1])
