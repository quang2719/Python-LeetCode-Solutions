#Reverse link list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_nodes = None
        node = head
        while node:
            next_node = node.next
            node.next = rev_nodes
            rev_nodes = node
            node = next_node
        return rev_nodes
        
        