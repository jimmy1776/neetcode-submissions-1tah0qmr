class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        deck = collections.deque()
        l = r = 0 

        while r < len(nums):
            while deck and nums[deck[-1]] < nums[r]:
                deck.pop()
            deck.append(r)
        
            if l > deck[0]:
                deck.popleft()
        
            if (r+1) >= k:
                l += 1
                output.append(nums[deck[0]])

            r += 1

        return output 


#q[0] is the leftmostelement (the front) and q[-1] is the rightmost element (the back/tail)