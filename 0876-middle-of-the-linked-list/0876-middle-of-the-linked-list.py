# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        current = head
        
        while current:
            current = current.next
            length += 1
        
        middle_index = length // 2
        current = head
        
        for _ in range(middle_index):
            current = current.next
        
        return current