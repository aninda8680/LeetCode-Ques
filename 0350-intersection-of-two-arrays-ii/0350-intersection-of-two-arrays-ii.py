class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        count = {}
        result = []

        # Count frequency of nums1
        for n in nums1:
            count[n] = count.get(n, 0) + 1

        # Match with nums2
        for n in nums2:
            if n in count and count[n] > 0:
                result.append(n)
                count[n] -= 1

        return result

