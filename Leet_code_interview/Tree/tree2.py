# Validate Binary Search Tree
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,minval,maxval):
            if not node: return True
            if minval < node.val < maxval:
                return (valid(node.left,minval,node.val) 
                        and valid(node.right,node.val,maxval))
            return False
        
        return valid(root,float('-inf'),float('inf'))
            