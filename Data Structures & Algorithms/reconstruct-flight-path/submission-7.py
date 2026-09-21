class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets):
            adj[src].append(dst)
        
        res = []

        def dfs(src):
            while adj[src]:
                nxt = adj[src].pop(0) #rush to the end 
                dfs(nxt)
            res.append(src)
        
        dfs("JFK")
        #return a reversed copy of the entire list 
        return res[::-1]

        