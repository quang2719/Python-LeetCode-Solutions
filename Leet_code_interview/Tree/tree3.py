# Symmetric Tree
# 
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symetric(nodeA,nodeB):
            if not nodeA and not nodeB:
                return True
            if not nodeA or not nodeB:
                return False
            if nodeA.val != nodeB.val:
                return False
            return (symetric(nodeA.left,nodeB.right) 
                    and symetric(nodeA.right,nodeB.left))
        return symetric(root.left,root.right)