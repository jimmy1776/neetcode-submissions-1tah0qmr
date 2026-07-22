class Solution:
    def productExceptSelf(self, nums : List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        postfix = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res 
        





#range(start,stop,step) 
#start: first value produced
# stop: the loop stops before reaching this value(exclusive - never actually visited)
# step: how muych to add each iteraton(negative = count downward)
