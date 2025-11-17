# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if not head or not head.next:
            return True

        # 1. Find middle using slow & fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev = head of reversed half

        # 3. Compare both halves
        left = head
        right = prev
        while right:  # only need to check second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
