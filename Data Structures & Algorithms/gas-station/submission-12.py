class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if it's impossible 
        if sum(gas) < sum(cost):
            return -1 
        
        total = 0 
        startPosition = 0 
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0 
                startPosition = i + 1 
        return startPosition
