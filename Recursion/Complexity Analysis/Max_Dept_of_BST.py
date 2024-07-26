# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    #dfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if not root:
            return 0
        res = 1
        stack.append([root,1])
        while stack:
            node,depth = stack.pop()
            if node:
                res = max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])  
        return res


