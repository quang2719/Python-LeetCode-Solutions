# Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []
        while(head):
            val_list.append(head.val)
            head = head.next
        l,r = 0,len(val_list)-1
        while(l<r):
            if val_list[l] != val_list[r]:
                return False
            l+=1
            r-=1
        return True
        
        