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
        stack = [[root,1]]
        res = 0 

        while stack:
            node, depth = stack.pop()

            if node:
                res= max(res,depth)
                stack.append([node.left,depth +1])
                stack.append([node.right,depth +1])
        
        return res 

        