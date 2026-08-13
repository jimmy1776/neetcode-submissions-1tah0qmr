# perms stores the result (the return value, a plain list of lists), never the frame itself. The frame is a temporary bookkeeping thing the interpreter uses while the call is in progress, and it's destroyed the instant the call returns, before the assignment on line 6 even happens.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) +1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res 
        

        