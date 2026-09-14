class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        #every node starts out as its own parent 
        par =[i for i in range(n)]
        rank = [1] * n 

        #returns the root of a node -  the group it belongs to - his boss 
        def find(n1):
            res = n1 

            while res != par[res]:
                #path halving 
                par[res] = par[par[res]]
                res = par[res]
            return res 
        
        # union returns either 0 or 1
        # this gets subtracted from res, which is the amount of TEAMS that are left after a pass of union  
        def union(n1,n2):
            p1, p2 = find(n1) , find(n2)

            #n1 and n2 are already in  the same group : do nothing 
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2 
                rank[p2] += rank[p1]
            else:
                par[p2]  = p1 
                rank[p1] += rank[p2]
        
            return 1 
        
        res = n 

        for n1, n2 in edges: 
            res -= union(n1,n2)
        return res 

            


