class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0 

        while r < len(nums):
            #pop smallers values from deck
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if(r+1) >= k: 
                l += 1 
                output.append(nums[q[0]])
            r += 1 
        return output 







#q[0] is the leftmostelement (the front) and q[-1] is the rightmost element (the back/tail)