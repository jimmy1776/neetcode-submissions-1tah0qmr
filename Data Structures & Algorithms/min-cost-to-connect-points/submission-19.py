class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #adjencecy list 
        n = len (points)
        adj = {i:[] for i in range(n)} #cost - neighbor(node)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        visit = set()
        minH =[[0,0]]
        res = 0 

        while len(visit) < n:
            cost ,i  = heapq.heappop(minH)
            if i in visit:
                continue 
            visit.add(i)
            res += cost 
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res 








