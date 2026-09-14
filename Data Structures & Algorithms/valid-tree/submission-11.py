class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(curr,prev):
            if curr in visit:
                return False 
            
            visit.add(curr)
            for j in adj[curr]:
                if j == prev:
                    continue 
                if dfs(j,curr) == False:
                    return False 
            return True 
        
        return dfs(0,-1) and n == len(visit)
