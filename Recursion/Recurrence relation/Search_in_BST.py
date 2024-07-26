# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        check = False
        def travel(root,val):
            nonlocal check
            if not root: return
            if root.val == val:
                check= True
                return root
            if root.val > val:
                return travel(root.left,val)
            if root.val < val:
                return travel(root.right,val)
        res = travel(root,val)
        if not check:
            return None
        return res
        