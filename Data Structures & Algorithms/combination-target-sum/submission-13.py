class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur,total):
            #base case 
            if total == target:
                res.append(cur.copy())
                return 
            if total > target or i >= len(nums):
                return 
            cur.append(nums[i])
            dfs(i,cur,total +nums[i])
            #backtrack
            cur.pop()
            dfs(i +1, cur , total)
        dfs(0,[],0)
        return res 
    

    #i = index, cur = [] current subarray, total : running total of the cur subarray  

































