# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        # Count the number of nodes
        count = 0
        while curr:
            count += 1
            curr = curr.next

        while count >= k:
            curr = prev.next
            nex = curr.next
            for _ in range(1, k):
                curr.next = nex.next
                nex.next = prev.next
                prev.next = nex
                nex = curr.next
            prev = curr
            count -= k

        return dummy.next
