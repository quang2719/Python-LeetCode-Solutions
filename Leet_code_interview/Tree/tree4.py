# Binary Tree Level Order Traversal
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def count_lv(node,level):
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                count_lv(node.left,level+1)
                count_lv(node.right,level+1)
        count_lv(root,0)
        return res