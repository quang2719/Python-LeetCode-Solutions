# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #nomal ver
    
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     count = 0
    #     cur = head
    #     while cur:
    #         if count%2 ==0 and cur.next:
    #             cur.val,cur.next.val = cur.next.val,cur.val
    #         count+=1
    #         cur = cur.next
    #     return head
    
    
    #recursive ver
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def swapP(head):
            if head and head.next:
                head.val,head.next.val = head.next.val,head.val
                swapP(head.next.next)
        swapP(head)
        return head
    