# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        Returns the node at which two singly linked lists intersect, or None.
        """
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        
        # Traverse both lists; when reaching the end, switch to the other head
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a  # Could be None or intersection node
