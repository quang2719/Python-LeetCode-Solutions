# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue


class Solution:
    #bfs
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0
        res = 1
        q = queue.Queue()
        q.put([root,1])
        while not q.empty():
            node,depth = q.get()
            if node:
                res = max(res,depth)
                q.put([node.left,depth+1])
                q.put([node.right,depth+1])
        return res

            