# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# deque (deck): Basically allows you to add and remove elemnts from bothy ends in O(1) It combines 
# a queue and a stack 



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        