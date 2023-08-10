class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Advance the first pointer by n+1 steps
        for _ in range(n + 1):
            first = first.next
        
        # Move first to the end, maintaining the gap
        while first != None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next
