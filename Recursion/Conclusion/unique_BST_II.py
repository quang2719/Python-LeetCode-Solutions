# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(n):
            if n ==0: return []
            return Built_SubTree(1,n)
        
        def Built_SubTree(start,end):
            trees = []
            if start>end:
                trees.append(None)
                return trees
            for i in range(start, end + 1):
                left_subtrees = Built_SubTree(start, i - 1)
                right_subtrees = Built_SubTree(i + 1, end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        
        return gen(n)