# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #nomal ver
        # rev_head = None
        # node = head
        # while node:
        #     next_node = node.next
        #     node.next = rev_head
        #     rev_head = node
        #     node = next_node
        # return rev_head
        
        #recursion ver
        def reverse(head):
            if not head or not head.next:
                return head
            re_list = reverse(head.next)
            head.next.next = head
            head.next = None
            return re_list
        return reverse(head)
            
        