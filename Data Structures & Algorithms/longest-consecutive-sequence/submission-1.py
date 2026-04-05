class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        #check if a number is the start of a sequence
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
        


        