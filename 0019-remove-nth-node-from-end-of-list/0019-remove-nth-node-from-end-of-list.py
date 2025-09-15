# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        index = 0
        dummy = prev = ListNode()
        prev.next = s = f = head 
        

        while index < n:
            f = f.next
            index += 1

        while f :
            prev = prev.next
            s = s.next
            f = f.next
        prev.next = s.next
        s.next = None
        return dummy.next