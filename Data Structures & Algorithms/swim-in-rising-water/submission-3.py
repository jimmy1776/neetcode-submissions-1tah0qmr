class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minH = [[grid[0][0],0,0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]] #r,c: right,left, down, up 

        visit.add((0,0))
        while minH:
            t,r,c = heapq.heappop(minH)

            if r == n - 1 and c == n -1:
                return t 
            for dr,dc in directions:
                neiR,neiC = r + dr, c + dc 
                if (neiR < 0 or neiC < 0 or 
                    neiR == n or neiC ==n or 
                    (neiR,neiC) in visit):
                    continue 
                visit.add((neiR,neiC))
                heapq.heappush(minH,[max(t,grid[neiR][neiC]),neiR,neiC])

# max(t, grid[neiR][neiC]) carries that tallest value forward one step at a time:
# t is the tallest square on the way to where you're standing now 
# grid[neiR][neiC] is the height of the square you are stepping onto 
# The larger of the two is the tallest square on the route to the new square. 

        


