# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#maxVal: the running best-so-far - threaded down thru each recursive call as an argument 

# "running best-so-far" : highest node.val seen on the path from the root down to (but not including) the current
#node's own value

#res: the good-node count for that subtree 




class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxVal):
            if not node:
                return 0 
            
            res = 1 if node.val >= maxVal else 0 
            maxVal = max(maxVal,node.val)
            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)

            return res 
        return dfs(root,root.val)