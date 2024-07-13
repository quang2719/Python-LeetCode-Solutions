#  Convert Sorted Array to Binary Search Tree
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildBST(left, right):  # Recursive helper function
            if left > right:
                return None
            
            mid = (left + right) // 2  
            root = TreeNode(nums[mid])  # Create the root node
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            
            return root

        return buildBST(0, len(nums) - 1)  # Start building from the entire array
