class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = list(s)

        # Process the string in chunks of size 2k
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in this block
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)
