# Remove Nth Node From End of List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 2 3 4 5
# n = 4
# 1 _ 3 4 5
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        padding_node = ListNode(0,head)
        left = padding_node
        righ = head
        # common sliding windows
        for _ in range(n-1):
            righ = righ.next
        
        while(righ.next):
            left = left.next
            righ = righ.next
        
        left.next = left.next.next
        return padding_node.next

        
        
            
            