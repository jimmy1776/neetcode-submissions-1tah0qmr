class Solution: 
    def subsets(self,nums: List[int]) -> List[List[int]]: 
        res = []
        subset = []
        def dfs(i):
            #base case 
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #recursive case 
            subset.append(nums[i])
            dfs(i +1)
            #backtrack
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res 

        